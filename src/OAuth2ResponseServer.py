from flask import Flask, render_template, request

app = Flask(__name__)
# Configure the listening server and port
app.config.from_object('config')

class OAuth2ResponseServer:
    def __init__(self):
        pass

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
        Server.shutdown()
        return 'bye! shutting down'

    def start(self):
        app.run()

    def shutdown(self):
        func = request.environ.get('werkzeug.server.shutdown')
        if func:
            raise RuntimeError('Not running with the Werkzeug Server')
        else:
            func()

if __name__ == '__main__':
    responseServer = OAuth2ResponseServer()
    responseServer.start()
    responseServer.shutdown()
