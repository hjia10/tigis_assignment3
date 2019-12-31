from flask import Flask, render_template
from web_visual_db import db_postgres

app = Flask(__name__)

author = "Rob"

my_classes = db_postgres.getDBdata('"TYPE", "NAME", "PERIOD", "USE"', '"MY_CLASS"', '"TYPE"')
my_crops = db_postgres.getDBdata('"CROP", "NAME", "STARTSEASON", "ENDSEASON"', '"MY_CROPS"', '"CROP"')

field_objects = db_postgres.getDBdata('"FIELD_ID", "LOWX", "LOWY", "HIX", "HIY", "AREA", "OWNER", "CROP"', '"MY_FIELDS"', '"FIELD_ID"')
find_objects = db_postgres.getDBdata('"FIND_ID", "XCOORD", "YCOORD", "TYPE", "DEPTH", "FIELD_NOTES"', '"MY_FINDS"', '"FIND_ID"')

db_postgres.assign_field_colours(field_objects, my_crops)
db_postgres.assign_find_colours(find_objects, my_classes)
db_postgres.assign_crop_names(field_objects, my_crops)
db_postgres.assign_class_names(find_objects, my_classes)

graphics_area_for_svg = db_postgres.GraphicsArea(15, 15, -1, 1, 16, 18)


@app.route("/")
def home():
    return render_template('index.html', info=author, fields=field_objects, finds=find_objects, classes=my_classes,
                           crops=my_crops, g=graphics_area_for_svg)
