import os
import binascii
import falcon
from templates import env
from db import db

class Collection():
    def on_get(self, request, response):
        """
        Returns a list of users.
        """
        response.status = falcon.HTTP_200
        response.body = 'TODO'
    
    def on_put(self, request, response):
        """
        Creates a new user.
        """
        response.status = falcon.HTTP_200
        response.body = 'TODO'

class Item():
    def on_get(self, request, response, id):
        """
        Returns a specific user.
        """
        response.status = falcon.HTTP_200
        response.body = 'TODO'
    
    def on_put(self, request, response, id):
        """
        Updates a user.
        """
        response.status = falcon.HTTP_200
        response.body = 'TODO'
    
    def on_delete(self, request, response, id):
        """
        Deletes a user.
        """
        response.status = falcon.HTTP_200
        response.body = 'TODO'

class Login():
    def on_get(self, request, response):
        """
        Logs a user in
        """
        template = env.get_template('login.html')
        redirect = request.get_param('redirect')
        body = template.render(redirect=redirect)
        response.status = falcon.HTTP_200
        response.content_type = 'text/html'
        response.body = body

    def on_post(self, request, response):
        username = request.get_param('username')
        password = request.get_param('password')
        redirect = request.get_param('redirect')
        if username and password:
            user = db.users.find_one({
                'username': username,
                'password': password,
            })
            if user:
                token = binascii.hexlify(os.urandom(16)).decode('ascii')
                user['token'] = token
                db.users.find_one_and_replace({
                    '_id': user['_id']
                }, user)
                response.set_cookie('user', token, http_only=False, secure=False, path='/')
                response.status = falcon.HTTP_302
                if redirect:
                    response.location = redirect
                else:
                    response.location = '/'
                response.body = 'Test'
                return

        template = env.get_template('login.html')
        body = template.render(redirect=redirect)
        response.status = falcon.HTTP_401
        response.content_type = 'text/html'
        response.body = body
         

