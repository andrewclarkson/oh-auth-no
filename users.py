import falcon

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
