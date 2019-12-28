from flask import Flask, render_template
from web_visual_db import db_postgres

app = Flask(__name__)

author = "Rob"

my_classes = db_postgres.getDBdata('"TYPE", "NAME", "PERIOD", "USE"', '"MY_CLASS"')
my_crops = db_postgres.getDBdata('"CROP", "NAME", "STARTSEASON", "ENDSEASON"', '"MY_CROPS"')

field_objects = db_postgres.getDBdata('"FIELD_ID", "LOWX", "LOWY", "HIX", "HIY", "AREA", "OWNER", "CROP"', '"MY_FIELDS"')
find_objects = db_postgres.getDBdata('"FIND_ID", "XCOORD", "YCOORD", "TYPE", "DEPTH", "FIELD_NOTES"', '"MY_FINDS"')

for field in field_objects:
    for crop in my_crops:
        if field.crop_id == crop.crop:
            field.fill = db_postgres.get_field_colour(crop.name)
        else:
            continue

for find in find_objects:
    for cls in my_classes:
        if find.find_type == cls.class_type:
            print('match...')
            print(find.find_type)
            print(cls.class_type)
            find.fill = db_postgres.get_find_colour(cls.class_type)
            print(find.fill)
        else:
            continue



class GraphicsArea:

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


#print_all_info()
graphics_area_for_svg = GraphicsArea(15, 15, 0, 0, 16, 16)


@app.route("/")
def home():
    return render_template('index.html', info=author, fields=field_objects, finds=find_objects, classes=my_classes,
                           crops=my_crops, g=graphics_area_for_svg)
