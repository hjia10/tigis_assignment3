from flask import Flask, render_template
from web_visual_db import db_postgres

app = Flask(__name__)

#data = db_oracle.getDBdata('*', 'ancient_castles')

info = "Rob"

field_objects = db_postgres.getDBdata('field_id, lowx, lowy, hix, hiy', 'fields')
find_objects = db_postgres.getDBdata('find_id, x_coord, y_coord', 'finds')

viewBox = "0 0 16 16"
db_postgres.print_svg(10, 10, viewBox)


for field in field_objects:
    field.show_info()
    print()
    field.draw_svg_rectangle()

for find in find_objects:
    find.show_info()
    print()
    find.draw_svg_circle()


@app.route("/")
def home():
    return render_template('index.html', info=info, fields=field_objects, finds=find_objects)
