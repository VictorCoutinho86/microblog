# MICROBLOG
### Making the tutorial of Miguel Grinberg [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
For use this project, open a command window, go to source of this project and run:

> pip install -r requeriments.txt

For installation of all dependencies needed for this project.
To do this is necessary that you **already have python and pip installed and configured**.

After, you need to run:

> export FLASK_APP=microblog.py

or, if you using Windows:

> set FLASK_APP=microblog.py

After that you need to create a database with SQLITE, for this just type:

> flask db init

> flask db migrate -m "Some commentary"

If all this will succeed do:

> flask db upgrade

This will create your database, ready for use.

To complete, one more thing is needed, create a config.py file, for use of Flask.
Create this file in the source of this project and put this lines:

```python
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Your Secret Key here!'
    
    # SqlAlchemy configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # SMTP Google configuration
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'youremail@gmail.com'
    MAIL_PASSWORD = 'Your Google Password'
    ADMINS = ['Your email!']
    
    # Limitations of Posts for pagination
    POSTS_PER_PAGE = 5
```

Doing this the project is ready to use, you can do that using:

> flask run

On the command window. 

#### Now Play with the project!
