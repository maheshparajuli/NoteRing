import functools # provides functions that act on functions.

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

from argon2 import PasswordHasher
from argon2.exceptions import HashingError
import re


"""   

1. A Blueprint in Flask is a way to organize your app into reusable and modular components.
   It helps when your application grows bigger — instead of putting all routes in app.py, you create sections (blueprints).

2. The name associated with a view is also called the endpoint, and by default it's the same as the name of the view function.

3. When using a blueprint, the name of the blueprint is prepended to the name of the function, so the endpoint for the login 
   function you wrote above is 'auth.login' because you added it to the 'auth' blueprint.

"""

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup',methods=('GET',"POST"))
def register():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        # db=get_db()
        error={}

        if not username:
            errors[username_error]='username is required'
        elif not password:
            errors[password_error]='password is required'
        elif len(password)<8:
            errors[len_error]='password must be at least 8 characters'
        elif re.search(r'[A-Z]', password) and re.search(r'[^A-Za-z0-9]', password):
            errors[strong_error]='Use at least one uppercase and one special charater'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username,password) VALUES(?,?)",(username,ph.hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                errors[db_error]=f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))
        flash(error)
    return render_template('auth/register.html')

"""

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

    
"""


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()



# To log out, you need to remove the user id from the session. Then load_logged_in_user won’t load a user on subsequent requests.

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    """
    this checks if user is logged in or not before every view 
    and @login_required is used to decorate every view 
    function(at the end every view is a function that returns sth)

    """
    @functools.wraps(view) # It is a helper decorator from Python’s built-in functools module.
    def wrapper_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

""" 
    This simple example perfectly explains the use of decorators(for revision)
    
    def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper

    @decorator_name
    def add(a, b):
    return a + b

    print(add(5, 3))


"""