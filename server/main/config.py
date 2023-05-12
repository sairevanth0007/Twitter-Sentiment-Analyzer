# project/server/config.py
import os

class BaseConfig:
    """Base configuration."""
    FLASK_APP="main/__init__.py"
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    DEBUG = False
    CONSUMER_KEY = 'Your_Cunsumer_Key'
    CONSUMER_SECRET = 'Your_Cunsumer_Secret'
    ACCESS_TOKEN = 'Your_Access_Token'
    ACCESS_TOKEN_SECRET = 'Your_Access_Token_Secret'

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
