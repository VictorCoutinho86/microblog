import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'V3i7C0t7or%&C6o1u4T9iNho'

    # SQLAlchemy Configuration!
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Send Mail Configuration!
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['victormelo@id.uff.br']

    POSTS_PER_PAGE = 5

    #MS TRANSLATOR KEY
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    DETECT_URL = os.environ.get('DETECT_URL')
    TRANSLATE_URL = os.environ.get('TRANSLATE_URL')


    # Languages available
    LANGUAGES = ['en', 'es', 'pt', 'de', 'fr']

    # Elasticsearch configuration
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
