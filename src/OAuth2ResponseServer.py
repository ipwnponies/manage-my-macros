from flask import Flask
from flask import render_template
from flask import request
from flask import url_for

app = Flask(__name__)
# Configure the listening server and port
app.config.from_object('config')


class OAuth2ResponseServer:

    @app.route('/oauth/')
    def oauth():
        """Listen for the identity provider's authentication response and store credentials if
        successful.
        """
        OAuth2ResponseServer.shutdown()
        return 'Success'

    @app.route('/optparam/')
    @app.route('/optparam/<foo>')
    def optional_parameter(foo=None):
        return render_template('hello.html', bar=foo)

    @app.route('/caseSensitive/')
    def case_sensitive():
        return 'The url is case sensitive'

    @app.route('/type/<int:bar>')
    def type_check(bar):
        return 'bar {}'.format(bar)

    @app.route('/')
    def index():
        return 'hi'

    @app.route('/bye/')
    def bye():
        OAuth2ResponseServer.shutdown()
        return 'bye! shutting down'

    def start():
        app.run(threaded=True)

    def shutdown():
        func = request.environ.get('werkzeug.server.shutdown')
        if func:
            func()
        else:
            raise RuntimeError('Not running with the Werkzeug Server')

    def get_oauth_redirect():
        return app.config['SERVER_NAME'] + url_for('oauth')

if __name__ == '__main__':
    OAuth2ResponseServer.start()
