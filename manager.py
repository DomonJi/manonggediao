#!/usr/bin/env python

import os
from manonggediao import app
from flask.ext.script import Manager, Shell

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]


manager = Manager(app)


def make_shell_context():
    return dict(app=app)
manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def deploy():
    pass
if __name__ == '__main__':
    manager.run()
