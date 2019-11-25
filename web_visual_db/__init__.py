from flask import Flask
from web_visual_db.forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '24cd206ec1356cbf2a296cd28d989281'

from web_visual_db import routes