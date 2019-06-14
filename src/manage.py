# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 13:37
# @Author  : llc
# @File    : manage.py

from app import db
from app.webapp import application
from app.models.user import User
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell, prompt_bool

manager = Manager(application)
migrate = Migrate(application, db)


def make_shell_context():
    return dict(app=application, db=db, User=User)


@manager.command
def initialize():
    # initialize database
    if prompt_bool("Warning: the initialization system will drop all data! Are you sure?"):
        db.drop_all(app=application)
        db.create_all(app=application)

    print("init system finish")


@manager.command
def test():
    """run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
