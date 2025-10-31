
import os
from flask import Flask

"""     
1. app.config is dictionary like object that stores configuration settings for your application
    things like secret keys, database paths, debug mode, etc.

2. app.config in Flask is an instance of Config (a subclass of Python's built-in dict), so it behaves like a 
   dictionary but with extra helper methods designed for loading and managing configuration data efficiently.

3. import os allows your Python (or Flask) program to do things that normally require using your computer's
    file system or environment.

remember the thing: THE APPLICATION FACTORY PATTERN

"""
# .\venv\Scripts\Activate


def create_app(test_config=None):
    app=Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("config.py",silent=True)

    else:
        app.config.from_mapping(test_config)


