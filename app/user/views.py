import logging

from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required, logout_user, login_user
from sqlalchemy.dialects.postgresql import psycopg2

from app import db
from models.user import User
from user import user

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s : %(message)s')


@user.route('/registration', methods=['post', 'get'])
def registration():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect('/')

        return render_template('registrations/index.html')
    else:
        email: str = request.form.get('email')
        if User.query.filter_by(email=email).first() is not None:
            return render_template('registrations/index.html',
                                   request=request,
                                   error=True,
                                   message=f'Пользователь с email: {email} уже есть в базе')

        if request.form.get('password') == request.form.get('confirmation'):
            user = User(name=request.form.get('name'), email=email)
            user.set_password(request.form.get('password'))
        else:
            return render_template('registrations/index.html',
                                   request=request,
                                   error=True,
                                   message='Пароли не совпадают')
        try:
            db.session.add(user)
            db.session.commit()
        except psycopg2.exc.IntegrityError as e:
            logging.error(str(e))
            return render_template('registrations/index.html',
                                   request=request,
                                   error=True,
                                   message=str(e))

        return redirect(url_for('user.registration'))


@user.route('/', methods=['post', 'get'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect('/')

        return render_template('login/index.html')
    else:
        email: str = request.form.get('email')
        password: str = request.form.get('password')
        user: User = User.query.filter_by(email=email).first()
        if user is None:
            return render_template('login/index.html',
                                   request=request,
                                   error=True,
                                   message=f'Пользователь с email: {email} не зарегистрирован')

        if not user.check_password(password):
            return render_template('login/index.html',
                                   request=request,
                                   error=True,
                                   message=f'Не верный пароль')

        login_user(user)
        return redirect('/')


@user.route('/logout', methods=['get'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))
