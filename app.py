#!/usr/bin/python3
""" Defines app class"""

from flask import Flask
from app.config.config import Config
from app.utils.database import db
from app.utils.authentication import login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    """ Import and register blueprints"""
    from app.controllers.employee_controller import employee_bp
    from app.controllers.dashboard_controller import dashboard_bp

    app.register_blueprint(employee_bp, url_prefix='/api')
    app.register_blueprint(dashboard_bp, url_prefix='/api')

    return app
