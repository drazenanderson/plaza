import os
DATA_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(DATA_DIR, 'static')

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# pagination
POSTS_PER_PAGE = 5

