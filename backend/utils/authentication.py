#!/usr/bin/python3
"""Defines class Authenticatiom"""
from app.models.user_model import User
from flask_login import LoginManager, UserMixin, login_user,
login_required, logout_user, current_user

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class AuthenticationService:
    def login(self, user):
        login_user(user)

    def logout(self):
        logout_user()

    @login_required
    def get_current_user(self):
        return current_user
