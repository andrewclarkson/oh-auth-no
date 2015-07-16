from pymongo import MongoClient

db = MongoClient('db')['test']


USERS = [
    {
        'token': None,
        'username': 'jill',
        'role': 'developer',
        'password': 'test',
    },
    {
        'token': None,
        'username': 'jack',
        'role': 'user',
        'password': 'test',
    },
]

user_ids = db.users.insert_many(USERS).inserted_ids

CLIENTS = [
    {
        'user': user_ids[0],
        'name': 'Jill\'s Web App',
        'client_id': '0',
        'client_secret': 'test',
        'redirect_uris': [
            'localhost:8000/',            
        ],
        'grant_type': 'authorization_code',
        'response_type': 'code',
        'scopes': [
            'posts',
            'users',
        ],
        'default_scopes': [
            'posts',
            'users',
        ],
    },        
    {
        'user': user_ids[0],
        'name': 'Jill\'s Browser App',
        'client_id': '1',
        'redirect_uris': [
            'localhost:8000/',            
        ],
        'grant_type': 'implicit',
        'response_types': 'token',
        'default_scopes': [
            'posts',
            'users',
        ],
    },        
    {
        'user': user_ids[0],
        'name': 'Jill\'s CLI App',
        'client_id': '2',
        'grant_type': 'password',
        'response_types': 'token',
        'default_scopes': [
            'posts',
            'users',
        ],
    },        
    {
        'user': user_ids[0],
        'name': 'Jill\'s Master App',
        'client_id': '3',
        'grant_type': 'client_credentials',
        'response_types': 'token',
        'scopes': [
            'admin',
        ],
        'default_scopes': [
            'admin',
        ],
    },        
]

db.clients.insert_many(CLIENTS)
