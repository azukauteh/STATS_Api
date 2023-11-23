# initializing Flask app with configurations from config.py
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

