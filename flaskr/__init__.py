
import os
from flask import Flask

"""     
1. app.config is dictionary like object that stores configuration settings for your application
    things like secret keys, database paths, debug mode, etc.

2. app.config in Flask is an instance of Config (a subclass of Python's built-in dict), so it behaves like a 
   dictionary but with extra helper methods designed for loading and managing configuration data efficiently.

3. import os allows your Python (or Flask) program to do things that normally require using your computer's
    file system or environment.



"""

def create_app(test_config=None):
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(

    )

    if test_config is None:
        # This is often used in create_app() factories to allow the app to run even if a developer hasn’t created a local config file yet.
    
        app.config.from_pyfile('config.py',silent=True) # This is often used in create_app() factories to allow the app to run even if a developer hasn’t created a local config file yet.
    app.config.from_mapping(test_config)
    
    
     #This small block of code is a safety step in many Flask apps — especially when you use instance_relative_config=True.

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/login')
    def login():
        return 'Banaudai xu bro'
    return app


