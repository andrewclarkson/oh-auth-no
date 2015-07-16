import falcon

from oauthlib.oauth2 import Server, RequestValidator

CLIENTS = [
    {
        'client_id': 'hello',
        'client_secret': 'world',
        'redirect_uris': [
            'localhost:8000/posts',            
        ],
        'response_types': [
            'code',
            'token',
        ],
        'default_scopes': [
            'posts',
            'users',
        ],
    }        
]

class Validator(RequestValidator):
    """
    A dummy validator
    """

    def validate_client_id(self, client_id, request):
        for client in CLIENTS:
            if client['client_id'] == client_id:
                return True
        return False

    def validate_redirect_uri(self, client_id, redirect_uri, request):
        for client in CLIENTS:
            if client['client_id'] == client_id:
                if redirect_uri in client['redirect_uris']:
                    return True
                else:
                    return False
        return False

    def validate_response_type(self, client_id, response_type, client, request):
        for client in CLIENTS:
            if client['client_id'] == client_id:
                if response_type in client['response_types']:
                    return True
                else:
                    return False
        return False

    def validate_scopes(self, client_id, scopes, client, request):
        return True

    def get_default_scopes(self, client_id, request):
        for client in CLIENTS:
            if client['client_id'] == client_id:
                return client['default_scopes']
        return []



server = Server(Validator())

class Token():
    def __init__(self):
        self.oauth = server

    def on_post(self, request, response):
        pass

class Authorize():
    def __init__(self):
        self.oauth = server
    
    def on_get(self, request, response):
        """
        A request to authorize an application
        """
        scopes, credentials = self.oauth.validate_authorization_request(
            uri = request.uri, 
            http_method = 'GET', 
            #body = request.params, 
            headers = request.headers
        )
        print(credentials)
        response.status = falcon.HTTP_200
        response.body = str({'scopes': scopes, 'credentials': credentials})

    def on_post(self, request, response):
        headers, body, status = self.oauth.create_authorization_response(
            uri = request.uri,
            http_method = 'POST',
            body = request.body,
            headers = request.header,
            scopes = ['default'] 
        )
        response.status = status
        response.headers = headers
        response.body = body

class Revoke():
    def __init__(self):
        self.oauth = server
    
    def on_post(self, request, response):
        pass

class Client():
    """
    The route to handle creating a client
    """
    def on_post(self, request, response):
        pass
