#!/usr/bin/env python
import os

from app import create_app, db


#from flask_script import Manager, Shell
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
application = app
#manager = Manager(app)
migrate = Migrate(application, db)

@app.shell_context_processor
def make_shell_context():
    return dict(app=application, db=db)

"""
def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run() """

if __name__ == '__main__':
    application.run()