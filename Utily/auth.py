from flask import jsonify , request
from functools import wraps
from app import app
import jwt


def token_required ( f ) :
    @wraps ( f )
    def decorator ( *args , **kwargs ) :

        token = None

        if 'x-token' in request.headers :
            token = request.headers [ 'x-token' ]

        if not token :
            return jsonify ( { 'message' : 'a valid token is missing' } )

        try :
            data = jwt.decode ( token , app.config [ "SECRET_KEY" ] )
        except :
            return jsonify({"Message": "Invalid Token"})

        return f ( *args , **kwargs )

    return decorator
