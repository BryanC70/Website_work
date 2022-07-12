import unittest, sys, os

sys.path.append('../flask-example-2')
from hello import app, db

class UsersTests(unittest.TestCase):
    #executed prior to each test

    def setUp(self):
        app.config("SQLALCHEMY_DATABASE_URL") + 'sqlite:///test.db'
        self.app= app.test_client()
        db.drop_all()


    def register(self,username, email,password):
         return sefl.app.post('/register', 
        data=dict(username=username,
        email=email,
        password=password,
        confirm_password=password),
        follow_redirects=True)
    
    def test_invalid_username_registration(self):
        response= self.register('t', 'test@example.com', 'FlaskIsAwesome')
        response= self.register('thisIsmorethan20characters', )
        