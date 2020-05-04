import json
import logging
import time

from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from app import redis
from blog import blog

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s : %(message)s')


@blog.route('/', methods=['get'])
@login_required
def index():
    keys: list = redis.keys(f'{current_user.id}_*')
    data: list = []
    for key in keys:
        data.append(json.loads(redis.get(key)))

    return render_template('blog/index.html', data=data if data is not None else [])


@blog.route('/create', methods=['post'])
@login_required
def create():
    name: str = request.form.get('name')
    text: str = request.form.get('text')
    key: str = f'{current_user.id}_{int(time.time())}'
    redis.set(key, json.dumps({'name': name, 'text': text, 'key': key}), ex=(5 * 60), nx=True)

    return redirect(url_for('blog.index'))


@blog.route('/add', methods=['get'])
@login_required
def add():
    return render_template('blog/add.html')


@blog.route('/delete/<string:key>/', methods=['get'])
@login_required
def delete(key):
    redis.delete(key)

    return redirect(url_for('blog.index'))
