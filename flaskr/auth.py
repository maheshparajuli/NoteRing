import functools # provides functions that act on functions.

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

from argon2 import PasswordHasher
from argon2.exceptions import HashingError


"""   

A Blueprint in Flask is a way to organize your app into reusable and modular components.
It helps when your application grows bigger — instead of putting all routes in app.py, you create sections (blueprints).







"""

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register',methods=('GET',"POST"))
def register():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        db=get_db()
        error=None

        if not username:
            error='username is required'
        elif not password:
            error='password is required'
        elif len(password)<8:
            error='password must be at least 8 characters'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username,password) VALUES(?,?)",(username,ph.hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error=f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))
        flash(error)
    return render_template('auth/register.html')



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


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
