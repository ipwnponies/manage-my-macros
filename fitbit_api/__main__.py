"""Main entry point for module. Starts up oauth listening server."""
import threading
import webbrowser

import fitbit_api.OAuth2ResponseServer
from fitbit_api.OAuth2Client import OAuth2Client
from fitbit_api.OAuth2ResponseServer import get_oauth_redirect
from fitbit_api.OAuth2ResponseServer import start_server


if __name__ == '__main__':

    client_id = None
    client_secret = None
    client = OAuth2Client(client_id, client_secret, get_oauth_redirect())
    thread = threading.Timer(1, webbrowser.open, args=(
        client.generate_authorization_url(),)).start()
    start_server(client)

    # Get access token
    token = fitbit_api.OAuth2ResponseServer.authorization_token
