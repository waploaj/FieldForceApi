from flask import Blueprint, request, jsonify
from app import db
from .model import *
from Utily.auth import token_required
from .serializer import *

comp = Blueprint("comp", __name__ )

#TODO: Add business logic Here.


