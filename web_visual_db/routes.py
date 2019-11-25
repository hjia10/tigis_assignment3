from flask import Flask, render_template
from web_visual_db import db, drawSVG

app = Flask(__name__)

data = db.getDBdata('*', 'ancient_castles')

@app.route("/")
def home():
    return render_template('index.html', data=data)
