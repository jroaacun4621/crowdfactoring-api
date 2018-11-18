from os import environ

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL', 'postgres://postgres@localhost:5432/crowdfactoring_db')