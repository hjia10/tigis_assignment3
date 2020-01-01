#! /usr/bin/env python3

from web_visual_db import db_oracle
from jinja2 import Environment, FileSystemLoader
import cgitb

cgitb.enable(format='text')

'''
my_classes = db_oracle.getDBdata('"TYPE", "NAME", "PERIOD", "USE"', '"MY_CLASS"', '"TYPE"')
my_crops = db_oracle.getDBdata('"CROP", "NAME", "STARTSEASON", "ENDSEASON"', '"MY_CROPS"', '"CROP"')

field_objects = db_oracle.getDBdata('"FIELD_ID", "LOWX", "LOWY", "HIX", "HIY", "AREA", "OWNER", "CROP"', '"MY_FIELDS"', '"FIELD_ID"')
find_objects = db_oracle.getDBdata('"FIND_ID", "XCOORD", "YCOORD", "TYPE", "DEPTH", "FIELD_NOTES"', '"MY_FINDS"', '"FIND_ID"')
'''

my_classes = db_oracle.getDBdata("MY_CLASS", "TYPE")
print(my_classes)
my_crops = db_oracle.getDBdata("MY_CROPS", "CROP")

field_objects = db_oracle.getDBdata("MY_FIELDS", "FIELD_ID")
find_objects = db_oracle.getDBdata("MY_FINDS", "FIND_ID")

db_oracle.assign_field_colours(field_objects, my_crops)
db_oracle.assign_find_colours(find_objects, my_classes)
db_oracle.assign_crop_names(field_objects, my_crops)
db_oracle.assign_class_names(find_objects, my_classes)

graphics_area_for_svg = db_oracle.GraphicsArea(15, 15, -1, 1, 16, 18)


def render_html():
    env = Environment(loader=FileSystemLoader('/web_visual_db/'))
    temp = env.get_template('/web_visual_db/index.html')
    print(temp.render(fields=field_objects, finds=find_objects, classes=my_classes, crops=my_crops, g=graphics_area_for_svg))
