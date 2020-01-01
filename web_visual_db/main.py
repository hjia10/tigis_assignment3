#!/usr/bin/env python3

from web_visual_db import db_oracle
import cgitb
cgitb.enable(format='text')
from jinja2 import Environment, FileSystemLoader


my_classes = db_oracle.getDBdata('"TYPE", "NAME", "PERIOD", "USE"', '"MY_CLASS"', '"TYPE"')
my_crops = db_oracle.getDBdata('"CROP", "NAME", "STARTSEASON", "ENDSEASON"', '"MY_CROPS"', '"CROP"')

field_objects = db_oracle.getDBdata('"FIELD_ID", "LOWX", "LOWY", "HIX", "HIY", "AREA", "OWNER", "CROP"', '"MY_FIELDS"', '"FIELD_ID"')
find_objects = db_oracle.getDBdata('"FIND_ID", "XCOORD", "YCOORD", "TYPE", "DEPTH", "FIELD_NOTES"', '"MY_FINDS"', '"FIND_ID"')

db_oracle.assign_field_colours(field_objects, my_crops)
db_oracle.assign_find_colours(find_objects, my_classes)
db_oracle.assign_crop_names(field_objects, my_crops)
db_oracle.assign_class_names(find_objects, my_classes)

graphics_area_for_svg = db_oracle.GraphicsArea(15, 15, -1, 1, 16, 18)


def render_html():
    env = Environment(loader=FileSystemLoader('.'))
    temp = env.get_template('index.html')
    print(temp.render(fields=field_objects, finds=find_objects, classes=my_classes, crops=my_crops, g=graphics_area_for_svg))




'''

@app.route("/")
def home():
    return render_template('index.html', info=author, fields=field_objects, finds=find_objects, classes=my_classes,
                           crops=my_crops, g=graphics_area_for_svg)


@app.route("/", methods=['POST'])
def get_form_data():
    option1 = request.form['option1']
    option2 = request.form['option2']
    option3 = request.form['option3']
    option4 = request.form['option4']
    return render_template('index.html', info=author, fields=field_objects, finds=find_objects, classes=my_classes,
                           crops=my_crops, g=graphics_area_for_svg, option1=option1)

'''

if __name__ == '__main__':
    render_html()