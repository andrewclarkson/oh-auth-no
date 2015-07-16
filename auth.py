import falcon

from oauthlib.oauth2 import Server, RequestValidator
from templates import env
from db import db

class Validator(RequestValidator):
    """
    A dummy validator
    """

    def validate_client_id(self, client_id, request):
        client = db.clients.find_one({'client_id': client_id}) 
        if client == None:
            return False
        else:
            return True

    def validate_redirect_uri(self, client_id, redirect_uri, request):
        client = db.clients.find_one({
            'client_id': client_id,
            'redirect_uris': redirect_uri,    
        }) 
        if client == None:
            return False
        else:
            return True

    def validate_response_type(self, client_id, response_type, client, request):
        client = db.clients.find_one({
            'client_id': client_id,
            'response_types': response_type,
        }) 
        if client == None:
            return False
        else:
            return True

    def validate_scopes(self, client_id, scopes, client, request):
        return True

    def get_default_scopes(self, client_id, request):
        client = db.clients.find_one({'client_id': client_id}) 
        if client == None:
            return False
        else:
            return client['default_scopes']

    def get_default_redirect_uri(self, client_id, request):
        client = db.clients.find_one({'client_id': client_id}) 
        if client == None:
            raise "Bad client id"
        
        else:
            return client['redirect_uris'][0]

    def save_authorization_code(self, client_id, code, request):
        client = db.clients.find_one({'client_id': client_id}) 
        if client == None:
            raise "Bad client id"

        db.authorization_codes.insert_one({
            'client': client,
            'user':  request.user,
            'redirect_uri': request.redirect_uri,
            'scopes': request.scopes,
        })

        return client['redirect_uris'][0]

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

        if not 'user' in request.cookies:
            response.status = falcon.HTTP_302
            redirect = request.uri
            
            redirect = falcon.util.uri.encode(redirect)
            
            response.location = '/users/login?redirect=' + redirect
            return

        user = db.users.find_one({'token': request.cookies['user']})
        if not user:
            response.status = falcon.HTTP_401
            response.location = '/users/login'
            return

        scopes, credentials = self.oauth.validate_authorization_request(
            uri = request.uri, 
            http_method = 'GET', 
            headers = request.headers
        )
        template = env.get_template('authorize.html')
        body = template.render(scopes=scopes)
        response.status = falcon.HTTP_200 
        response.content_type = 'text/html'
        response.body = body
        
    def on_post(self, request, response):
        if not 'user' in request.cookies:
            response.status = falcon.HTTP_302
            redirect = request.uri
            
            redirect = falcon.util.uri.encode(redirect)
            
            response.location = '/users/login?redirect=' + redirect
            return

        user = db.users.find_one({'token': request.cookies['user']})
        if not user:
            response.status = falcon.HTTP_401
            response.location = '/users/login'
            return
        
        headers, body, status = self.oauth.create_authorization_response(
            uri = request.uri,
            http_method = 'POST',
            headers = request.headers,
            scopes = request.get_param_as_list('scopes'),
            credentials = {'user': user}, 
        )

        response.status = falcon.HTTP_302
        response.location = 'http://' + headers['Location']
        response.body = ''

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
