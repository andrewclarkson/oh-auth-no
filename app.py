import falcon

import auth

import users
import posts

app = falcon.API()
app.add_route('/oauth2/authorize', auth.Authorize())
app.add_route('/oauth2/token', auth.Token())
app.add_route('/oauth2/revoke', auth.Revoke())
app.add_route('/oauth2/client', auth.Client())
app.add_route('/users', users.Collection())
app.add_route('/users/{username}', users.Item())
app.add_route('/posts', posts.Collection())
app.add_route('/posts/{id}', posts.Item())
app.add_route('/posts/timeline', posts.Timeline())
