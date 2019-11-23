from flask import Blueprint
word_routes = Blueprint('word', __name__)
from . import routes
