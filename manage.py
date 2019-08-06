#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import code
import sys
import os
import importlib

import click
from flask_alembic import Alembic
from flask_alembic.cli import base as flask_alembic

from utils.file_manage import recurs_find
from utils.crypto import get_random_string

@click.group()
def cli(): pass


# runserver as Development mode
@cli.command("runserver", short_help="usage: runserver\r\nrunserver 8000\r\nrunserver 0.0.0.0:8000\r\n")
@click.argument('address', default='')
def runserver(address):
    host, *port = address.split(':')
    host = host if host else '127.0.0.1'
    port = '8000' if not port else port[0]
    app.run(host=host, port=port, use_reloader=False)


# open interactive shell, just as Django shell
@cli.command('shell', short_help='Run shell with flask app context.')
def shell_command():
    banner = 'Python %s on %s\nApp: %s [%s]\nInstance: %s' % (
            sys.version,       sys.platform,
            app.import_name,   app.env,
            app.instance_path,
    )
    ctx = {}
    startup = os.environ.get('PYTHONSTARTUP')
    if startup and os.path.isfile(startup):
        with open(startup, 'r') as f:
            eval(compile(f.read(), startup, 'exec'), ctx)
    ctx.update(app.make_shell_context())
    code.interact(banner=banner, local=ctx)


# Just as Django shell, but use ipython instead of python
@cli.command('ipython', short_help='Run Ipython shell with flask app context.')
@click.argument('ipython_args', nargs=-1, type=click.UNPROCESSED)
def ipython_shell(ipython_args):
    import IPython
    from IPython.terminal.ipapp import load_default_config
    from traitlets.config.loader import Config
    if 'IPYTHON_CONFIG' in app.config:
        config = Config(app.config['IPYTHON_CONFIG'])
    else:
        config = load_default_config()
    config.TerminalInteractiveShell.banner1 = (
            'Python %s on %s\nIPython: %s\nApp: %s [%s]\nInstance: %s') % (
            sys.version,         sys.platform,
            IPython.__version__, app.import_name,
            app.env,             app.instance_path
    )
    IPython.start_ipython(
        argv=ipython_args,
        user_ns=app.make_shell_context(),
        config=config,
    )


# Flask can't generate SECRET_KEY (a random str)
# Using shell cmd so rough that is dangerous $ python -c 'import os; print(os.urandom(16))'
# Using Django's standard crypto utilities is much better.
# site-packages/django/core/management/commands/startproject.py
@cli.command('secret', short_help='Generate random str for SECRET_KEY.')
def ipython_shell():
    print(
        get_random_string(16, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
    )


# ------- alembic ----------
'''
There is a easier way using Alembic with click, but can't use it as same as Django
```python
from flask_alembic import alembic_click
cli.add_command(alembic_click, 'db')
```
'''


@cli.command('makemigrations')
@click.argument('message', default='Model changed')
def makemigrations(message):
    flask_alembic.revision(message)


@cli.command('migrate')
@click.argument('target', default='heads')
def migrate(target):
    flask_alembic.upgrade(target)


@cli.command('merge')
@click.argument('revisions', default='heads')
def merge(revisions):
    flask_alembic.merge(revisions, message=None, label=None)


@cli.command('downgrade')
@click.argument('target', default=-1)
def downgrade(target):
    flask_alembic.downgrade(target)


@cli.command('current')
@click.argument('verbose', default=True)
def current(verbose):
    flask_alembic.current(verbose=verbose)


'''
@cli.command('heads')
def heads():
    flask_alembic.heads(resolve_dependencies=False, verbose=True)


@cli.command('log')
def log():
    flask_alembic.log(start='base', end='heads', verbose=False)


@cli.command('show')
@click.argument('revisions', default='head')
def show(revisions):
    flask_alembic.show(revisions)


@cli.command('branches')
def branches():
    """Show the list of revisions that have more than one next revision."""
    flask_alembic.branches(verbose=False)


@cli.command('stamp')
@click.argument('target', default='head')
def stamp(target):
    """Set the current revision without running migrations."""
    flask_alembic.stamp(target=target)
'''


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    wsgi = [i for i in recurs_find(base_dir, 'wsgi.py') if 'lib' not in i][0]
    pkg = os.path.split(os.path.dirname(wsgi))[1]
    # import importlib
    # params = importlib.import_module('b.c.c')
    # params_ = importlib.import_module('.c.c',package='b')
    app = getattr(importlib.import_module('{}.wsgi'.format(pkg)), 'app')
    with app.app_context():  # make app_context
        Alembic().init_app(app)   # init Alembic with app context
        cli()  # Start command line Service

