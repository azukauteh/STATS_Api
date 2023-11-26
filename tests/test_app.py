#!/usr/bin/python3
""" unittest  app class"""
import unittest
from flask import Flask
from app import create_app


class TestAppCreation(unittest.TestCase):
    def test_create_app(self):
        app = create_app()

        """Check if the app is an instance of Flask"""
        self.assertIsInstance(app, Flask)
        """ Check if the app has the correct configuration"""
        self.assertTrue(app.config['TESTING'])
        self.assertEqual(app.config['SQLALCHEMY_DATABASE_URI'],
                         '_test_database_uri')

        """ Check if database and login_manager are initialized"""
        with app.app_context():
            self.assertIsNotNone(app.extensions['sqlalchemy'].db)
            self.assertIsNotNone(app.extensions['login_manager'])
        """ Confirm registered blueprints """
        self.assertTrue(any(bp.url_prefix == '/api'
                            for bp in app.blueprints.values()))


if __name__ == '__main__':
    unittest.main()
