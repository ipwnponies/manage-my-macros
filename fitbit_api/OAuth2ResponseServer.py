"""Oauth response server"""
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for

APP = Flask(__name__)
# Configure the listening server and port
APP.config.from_object('fitbit_api.config')

authorization_token = None


@APP.route('/access')
def oauth_access():
    access_token = request.args.get('access_token')
    print('Access token is {}'.format(access_token))
    pass


@APP.route('/oauth')
def oauth():
    """Listen for the identity provider's authentication response and store credentials if
    successful.
    """
    global authorization_token
    authorization_token = request.args.get('code')

    shutdown()
    return "Success, we got a token!"

    # The access token your application should use to make requests on behalf
    # of the user.
    access_token = request.args.get('access_token')

    # How long in seconds the access token will be valid for
    expires_in = request.args.get('expires_in')

    # A space-separated list of scopes the user authorized. May be fewer than
    # the application requested.
    scope = request.args.get('scope')

    # Provides any state that might be useful to your application when the user is redirected back
    # to your application. This parameter will be added to the redirect URI exactly as your
    # application specifies in the authorization request. Fitbit strongly recommend including an
    # anti-forgery token in this parameter and confirming its value in the redirect to mitigate
    # against cross-site request forgery (CSRF).
    state = request.args.get('state')

    # Will always be Bearer.
    token_type = request.args.get('token_type')

    # The id (sometimes referred to as encoded_id)of the Fitbit user that
    # authorized your application
    user_id = request.args.get('user_id')

    shutdown()

    oauth_info = {
        'access_token': access_token,
        'expires': expires_in,
        'scope': scope,
        'state': state,
        'token_type': token_type,
        'user': user_id,
    }
    return "The input was {}".format(repr(oauth_info))


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


def start_server(oauth_client):
    oauth_client = oauth_client
    APP.run()


def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func:
        func()
    else:
        raise RuntimeError('Not running with the Werkzeug Server')


def get_oauth_redirect():
    with APP.app_context():
        return url_for('oauth')


def get_oauth_access_redirect():
    with APP.app_context():
        return url_for('oauth_access')
