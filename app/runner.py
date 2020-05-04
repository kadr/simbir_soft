from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager, Shell
import view
from app import app, db
from user import user
from blog import blog

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(blog, url_prefix='/blog')

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
