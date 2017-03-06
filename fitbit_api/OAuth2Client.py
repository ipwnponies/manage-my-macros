from requests_oauthlib import OAuth2Session


class OAuth2Client(object):
    # URI for the authrorization server
    AUTHORIZE_ENDPOINT = 'https://www.fitbit.com/oauth2/authorize'

    # URI for the resource server
    TOKEN_REFRESH_ENDPOINT = 'https://api.fitbit.com/oauth2/token'

    def __init__(self, client_id, client_secret, redirect_uri):
        # Credentials are generated after registering to fitbit API
        self.client_id = client_id
        self.client_secret = client_secret

        self.oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
        self.oauth.redirect_uri = redirect_uri

    def generate_authorization_url(self, scope=['weight', 'profile']):
        '''
        Generate the url used to request authorization.

        This is the url that points to FitBit
        authorization server. The user will open this page in a browser.
        The redirect uri will point to the client's response server that will receive the access
        tokens.
        '''

        self.oauth.scope = scope
        authorization_url, _ = self.oauth.authorization_url(
            OAuth2Client.AUTHORIZE_ENDPOINT)
        return authorization_url

    def fetch_access_token(self, code, redirect_url):
        '''
        Retrieve access token from resource server.

        Pass the authorization code from the authorization server to receive an access token. The
        access token is what is used to query resources.
        '''

        return self.oauth.fetch_token(
            self.TOKEN_REFRESH_ENDPOINT,
            code=code,
            username=self.client_id,
            password=self.client_secret
        )
