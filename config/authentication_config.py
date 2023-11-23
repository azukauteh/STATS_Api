#!/usr/bin/python3
"""Defines authentication class"""
from app.config.authentication_config import AuthenticationConfig


class AuthenticationConfig:
    """
    Change this to a secure, randomly generated key "secret key"
    Change this to a secure, randomly generated key "JWT secret key
    Set the JWT token expiration time in seconds (e.g., 1 hour)
    "JWT token expiration"
    """
    SECRET_KEY = 'your_secret_key'
    JWT_SECRET_KEY = 'your_jwt_secret_key'
    JWT_TOKEN_EXPIRATION = 3600
