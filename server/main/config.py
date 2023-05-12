# project/server/config.py
import os

class BaseConfig:
    """Base configuration."""
    FLASK_APP="main/__init__.py"
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    DEBUG = False
    CONSUMER_KEY = 'DUuBwdcyD1cjnUk6CjdT2H0Z5'
    CONSUMER_SECRET = 'qmkc8pzrYrZSelfTYIw6cFhj1bFQG83TM3vNUU3lLLCESL1nWT'
    ACCESS_TOKEN = '1261152772042289153-wAMD0qGAqOGXlUEmg2kp8FsYblTEsJ'
    ACCESS_TOKEN_SECRET = 'cfWMMC2wTuJRxZPDTCamUIy3IhW9MNyzClRcWHxcNY3Nr'

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    FLASK_ENV="development"

class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    FLASK_ENV="testing"


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
    FLASK_ENV="production"
