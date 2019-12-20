from flask import Flask, render_template
from web_visual_db import db_postgres

app = Flask(__name__)

author = "Rob"

field_objects = db_postgres.getDBdata('field_id, lowx, lowy, hix, hiy', 'fields')
find_objects = db_postgres.getDBdata('find_id, x_coord, y_coord', 'finds')


class graphicsArea:

    def __init__(self, width, height, viewBox_x, viewBox_y, viewBox_width, viewBox_height):
        self.width = f"{width}cm"
        self.height = f"{height}cm"
        self.viewBox_x = viewBox_x
        self.viewBox_y = viewBox_y
        self.viewBox_width = viewBox_width
        self.viewBox_height = viewBox_height
        self.viewBox_custom = f"{viewBox_x} {viewBox_y} {viewBox_width} {viewBox_height}"


def print_all_info():
    for field in field_objects:
        field.show_info()
        field.draw_svg_rectangle()

    for find in find_objects:
        find.show_info()
        find.draw_svg_circle()


box = graphicsArea(15, 15, 0, 0, 16, 16)

@app.route("/")
def home():
    return render_template('index.html', info=author, fields=field_objects, finds=find_objects, g=box)
