"""Main entry point for module. Starts up oauth listening server."""
import fitbit_api.OAuth2ResponseServer


if __name__ == '__main__':
    fitbit_api.OAuth2ResponseServer.start()
