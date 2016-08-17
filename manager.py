#!/usr/bin/env python

import os
if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]
from manonggediao import app
from flask.ext.script import Manager, Shell

manager = Manager(app)
def make_shell_context():
    return dict(app=app)
manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def deploy():
    pass
if __name__ == '__main__':
    manager.run()
