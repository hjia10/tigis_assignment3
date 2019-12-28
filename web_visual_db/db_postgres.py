import psycopg2


class Field:

    def __init__(self, field_id, lowx, lowy, hix, hiy, area, owner, crop_id):
        self.field_id = field_id
        self.lowx = lowx
        self.lowy = lowy
        self.hix = hix
        self.hiy = hiy
        self.area = area
        self.owner = owner
        self.crop_id = crop_id

        self.width = hix - lowx
        self.height = hiy - lowy
        self.centroidx = (hix - lowx)/2 + lowx
        self.centroidy = (hiy - lowy)/2 + lowy

        self.fill = 'none'

    def __repr__(self):
        return f"Field({self.field_id}, {self.lowx}, {self.lowy}, {self.hix}, {self.hiy})"

    def __str__(self):
        return f"Field {self.field_id} - Bottom Left ({self.lowx}, {self.lowy}) Top Right ({self.hix}, {self.hiy})"

    def show_info(self):
        info=[]
        info.append(f'Field ID : {str(self.field_id)}')
        info.append(f'Lower X : {str(self.lowx)}')
        info.append(f'Upper X : {str(self.hix)}')
        info.append(f'Lower Y : {str(self.lowy)}')
        info.append(f'Upper Y : {str(self.hiy)}')
        return info

    def draw_svg_rectangle(self):
        svg_type = "rect"
        fill = "red"
        stroke = "black"
        stroke_width = "0.5"
        svg_string = f'<{svg_type} x="{str(self.lowx)}" y="{str(self.lowy)}" width="{str(self.width)}" height="{str(self.height)}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>'
        print(svg_string)
        return svg_string


class Find:

    def __init__(self, find_id, xcoord, ycoord, find_type, depth, field_notes):
        self.find_id = find_id
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.find_type = find_type
        self.depth = depth
        self.field_notes = field_notes

        self.fill = get_find_colour(self.find_type)

    def __repr__(self):
        return f"Find({self.find_id}, {self.xcoord}, {self.ycoord})"

    def __str__(self):
        return f"Find {self.find_id} - Coordinates : ({self.xcoord}, {self.ycoord})"

    def show_info(self):
        print('Find ID : ' + str(self.find_id))
        print(f'co-ordinates : ({str(self.xcoord)},{str(self.ycoord)})')

    def draw_svg_circle(self):
        svg_type = "circle"
        fill = '"green"'
        radius = "1"
        svg_string = '<' + svg_type + ' cx = ' + '"' + str(self.xcoord) + '"' + ' cy=' + '"' + str(self.ycoord) + '"' + ' r=' + '"' + str(radius) + '"' + ' fill=' + fill + '/>'
        print(svg_string)
        return svg_string


class myClass:

    def __init__(self, class_type, name, period, use):
        self.class_type = class_type
        self.name = name
        self.period = period
        self.use = use

    def __repr__(self):
        return f"Class({self.class_type}, {self.name}, {self.period}, {self.use})"

    def __str__(self):
        return f"Class # {self.class_type} - {self.name}, Period : {self.period}, Use: {self.use})"


class Crop:

    def __init__(self, crop, name, startseason, endseason):
        self.crop = crop
        self.name = name
        self.startseason = startseason
        self.endseason = endseason

    def __repr__(self):
        return f"Crop({self.crop}, {self.name}, {self.startseason}, {self.endseason})"

    def __str__(self):
        return f"Crop # {self.crop} - {self.name}, Start of Season: {self.startseason}, End of Season: {self.endseason})"


def get_field_colour(field_crop):
    if field_crop == 'TURNIPS':
        return 'purple'
    elif field_crop == 'OIL SEED RAPE':
        return 'yellow'
    elif field_crop == 'STRAWBERRIES':
        return 'red'
    elif field_crop == 'PEAS':
        return 'green'
    elif field_crop == 'POTATOES':
        return 'white'
    else:
        return 'none'


def get_find_colour(find_class):
    if find_class == 1:
        return 'blue'
    elif find_class == 2:
        return 'gray'
    elif find_class == 3:
        return 'turquoise'
    elif find_class == 4:
        return 'brown'
    else:
        return 'none'


def print_svg(width, height, viewbox):
    return f'<svg width="{width}" height="{height}" viewBox="{viewbox}">'


def getDBdata(select_term, table_name):
    results = []
    conn = psycopg2.connect(host="localhost", database="tigis", user="robwebster", password="1emedente0486", port=5431)
    c = conn.cursor()
    c.execute(f"SELECT {select_term} FROM {table_name}")

    if table_name == '"MY_FIELDS"':
        fields_list = []
        for row in c:
            (a, b, c, d, e, f, g, h) = row
            field_name = table_name[:-1] + str(a)
            # print('Field Name is : ' + field_name)
            field_name = Field(a, b, c, d, e, f, g, h)
            fields_list.append(field_name)
            results = fields_list

    elif table_name == '"MY_FINDS"':
        finds_list = []
        for row in c:
            (a, b, c, d, e, f) = row
            find_name = table_name[:-1] + str(a)
            # print('Field Name is : ' + field_name)
            find_name = Find(a, b, c, d, e, f)
            finds_list.append(find_name)
            results = finds_list

    elif table_name == '"MY_CLASS"':
        classes_list = []
        for row in c:
            (a, b, c, d) = row
            my_class = myClass(a, b, c, d)
            classes_list.append(my_class)
            results = classes_list

    elif table_name == '"MY_CROPS"':
        crops_list = []
        for row in c:
            (a, b, c, d) = row
            my_crop = Crop(a, b, c, d)
            crops_list.append(my_crop)
            results = crops_list
    else:
        print("Table Name not supported...")

    conn.close()
    return results

