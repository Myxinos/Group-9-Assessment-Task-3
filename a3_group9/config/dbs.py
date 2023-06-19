import os

basedir = os.path.abspath(os.path.dirname(__file__) + '/../')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
SQLALCHEMY_TRACK_MODIFICATION = True
SQLALCHEMY_COMMIT_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
