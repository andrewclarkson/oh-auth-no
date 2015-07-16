import falcon

from oauthlib.oauth2 import WebApplicationServer, RequestValidator

class Token():
    def on_post(self, request, response):
        pass

class Authorize():
    def on_get(self, request, response):
        pass

class Revoke():
    def on_post(self, request, response):
        pass

class Client():
    """
    The route to handle creating a client
    """
    def on_post(self, request, response):
        pass
