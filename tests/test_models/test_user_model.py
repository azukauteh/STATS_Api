#!/usr/bin/python3
"""
Contains tests for User
"""
import unittest
from app.models.user_model import User
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


class TestUserModel(unittest.TestCase):
    def setUp(self):
        """ Set up Flask application context, database, and login manager"""
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['SECRET_KEY'] = 'your_secret_key'

        db = SQLAlchemy(self.app)
        db.init_app(self.app)

        self.login_manager = LoginManager(self.app)
        self.login_manager.login_view = 'login'

        """ Create database tables"""
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """ Clean up resources and drop tables"""
        with self.app.app_context():
            db.drop_all()

    def test_to_dict(self):
        """ Create an instance of the User class"""
        user = User(username='test_user', password='test_password')

        """ invoke  to_dict method"""
        user_dict = user.to_dict()

        """ Verify that the dictionary is created correctly"""
        self.assertEqual(user_dict['id'], None)
        self.assertEqual(user_dict['username'], 'test_user')


if __name__ == '__main__':
    unittest.main()
