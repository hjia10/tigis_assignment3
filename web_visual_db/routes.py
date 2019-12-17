from flask import Flask, render_template
from web_visual_db import db_postgres

app = Flask(__name__)

author = "Rob"

field_objects = db_postgres.getDBdata('field_id, lowx, lowy, hix, hiy', 'fields')
find_objects = db_postgres.getDBdata('find_id, x_coord, y_coord', 'finds')

svg_width = '10cm'
svg_height = '10cm'
viewBox = "0 0 16 16"
svg_setup = db_postgres.print_svg(svg_width, svg_height, viewBox)
print(f'SVG Setup Phrase - {svg_setup}')

for field in field_objects:
    field.show_info()
    field.draw_svg_rectangle()

for find in find_objects:
    find.show_info()
    find.draw_svg_circle()


@app.route("/")
def home():
    return render_template('index.html', info=author, fields=field_objects, finds=find_objects, svg_setup=svg_setup)
