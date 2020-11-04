from flask import jsonify, request
from functools import wraps
from app import  app
import jwt

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):

      token = None

      if 'x-tokens' in request.headers:
         token = request.headers['x-tokens']

      if not token:
         return jsonify({'message': 'a valid token is missing'})

      try:
         data = jwt.decode(token, app.config["SECRET_KEY"])
         # current_user = Users.query.filter_by(person_id=request.json['person_id']).first()
      except:
         pass

      return f("current_user", *args, **kwargs)
   return decorator