import falcon

import users
import posts

app = falcon.API()
app.add_route('/users', users.Collection())
app.add_route('/users/{username}', users.Item())
app.add_route('/posts', posts.Collection())
app.add_route('/posts/{id}', posts.Item())
app.add_route('/posts/timeline', posts.Timeline())
