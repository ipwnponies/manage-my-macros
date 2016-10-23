"""Oauth response server"""
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for

APP = Flask(__name__)
# Configure the listening server and port
APP.config.from_object('fitbit_api.config')


@APP.route('/oauth/')
def oauth():
    """Listen for the identity provider's authentication response and store credentials if
    successful.
    """
    shutdown()
    return 'Success'


@APP.route('/optparam/')
@APP.route('/optparam/<foo>')
def optional_parameter(foo=None):
    return render_template('hello.html', bar=foo)


@APP.route('/caseSensitive/')
def case_sensitive():
    return 'The url is case sensitive'


@APP.route('/type/<int:bar>')
def type_check(bar):
    return 'bar {}'.format(bar)


@APP.route('/')
def index():
    return 'hi'


@APP.route('/bye/')
def bye():
    shutdown()
    return 'bye! shutting down'


def start():
    APP.run(threaded=True)


def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func:
        func()
    else:
        raise RuntimeError('Not running with the Werkzeug Server')


def get_oauth_redirect():
    return APP.config['SERVER_NAME'] + url_for('oauth')
