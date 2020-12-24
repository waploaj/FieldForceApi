from flask import Blueprint, request, jsonify
from .model import *


pos = Blueprint("pos", __name__)
#TODO: Add Business Logic Here!!