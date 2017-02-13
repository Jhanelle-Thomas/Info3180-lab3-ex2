from flask import Flask

app = Flask(__name__)
from app import views

app.config['SECRET_KEY'] = "bet you won't guess this"