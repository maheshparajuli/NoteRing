import functools # provides functions that act on functions.

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db


"""   

A Blueprint in Flask is a way to organize your app into reusable and modular components.
It helps when your application grows bigger — instead of putting all routes in app.py, you create sections (blueprints).







"""

bp = Blueprint('auth', __name__, url_prefix='/auth')