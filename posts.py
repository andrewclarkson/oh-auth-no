import falcon

from db import db

class Collection():
    def on_get(self, request, response):
        """
        Returns a list of posts.
        """
        response.status = falcon.HTTP_200
        response.body = 'TODO'
    
    def on_put(self, request, response):
        """
        Creates a new post
        """
        response.status = falcon.HTTP_200
        response.body = 'TODO'

class Item():
    def on_get(self, request, response, id):
        """
        Returns a specific post.
        """
        response.status = falcon.HTTP_200
        response.body = 'TODO'
    
    def on_put(self, request, response, id):
        """
        Update a post
        """
        response.status = falcon.HTTP_200
        response.body = 'TODO'
    
    def on_delete(self, request, response, id):
        """
        Deletes a post
        """
        response.status = falcon.HTTP_200
        response.body = 'TODO'
        
class Timeline():
    def on_get(self, request, response):
        """
        Gets a users timeline
        """
        response.status = falcon.HTTP_200
        response.body = 'TODO'

