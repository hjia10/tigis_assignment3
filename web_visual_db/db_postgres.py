import psycopg2


class GraphicsArea:

    def __init__(self, width, height, viewBox_x, viewBox_y, viewBox_width, viewBox_height):
        self.width = f"{width}cm"
        self.height = f"{height}cm"
        self.viewBox_x = viewBox_x
        self.viewBox_y = viewBox_y
        self.viewBox_width = viewBox_width
        self.viewBox_height = viewBox_height
        self.viewBox_custom = f"{viewBox_x} {viewBox_y} {viewBox_width} {viewBox_height}"


class Field:

    def __init__(self, field_id, lowx, lowy, hix, hiy, area, owner, crop_id):

        # Parameters passed in during creation (ie fetched from database)
        self.field_id = field_id
        self.lowx = lowx
        self.lowy = lowy
        self.hix = hix
        self.hiy = hiy
        self.area = area
        self.owner = owner
        self.crop_id = crop_id

        #  Attributes calculated from object properties
        self.width = hix - lowx
        self.height = hiy - lowy
        self.centroidx = (hix - lowx)/2 + lowx
        self.centroidy = (hiy - lowy)/2 + lowy

        # Default value for fill is 'none'.  This property is dynamically added at runtime
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
        self.class_name = 'none'

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


class MyClass:

    def __init__(self, class_type, name, period, use):
        self.class_type = class_type
        self.name = name
        self.period = period
        self.use = use

        self.fill = 'none'

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

        self.fill = 'none'

    def __repr__(self):
        return f"Crop({self.crop}, {self.name}, {self.startseason}, {self.endseason})"

    def __str__(self):
        return f"Crop # {self.crop} - {self.name}, Start of Season: {self.startseason}, End of Season: {self.endseason})"


def get_field_colour(field_crop):
    if field_crop == 'TURNIPS':
        return '#A647FF'  # purple
    elif field_crop == 'OIL SEED RAPE':
        return '#F3FC30'  # pale yellow
    elif field_crop == 'STRAWBERRIES':
        return '#FD5959'  # orangey red
    elif field_crop == 'PEAS':
        return '#91F708'  # light green
    elif field_crop == 'POTATOES':
        return '#F9C89A'  # lightish orange
    else:
        return 'none'


def get_find_colour(find_class):
    if find_class == 1:
        return '#9AA8F9'  # light blue
    elif find_class == 2:
        return '#C8C8C8'  # light grey
    elif find_class == 3:
        return '#ABC349'  # flinty green
    elif find_class == 4:
        return '#D1BB00'  # mustard colour
    else:
        return 'none'


def get_crop_name(crops, crop_id):
    for crop in crops:
        if crop.crop == crop_id:
            return crop.name
        else:
            continue


def get_class_name(my_class, find_type):
    for cls in my_class:
        if cls.class_type == find_type:
            return cls.name
        else:
            continue


def print_svg(width, height, viewbox):
    return f'<svg width="{width}" height="{height}" viewBox="{viewbox}">'


def getDBdata(select_term, table_name, order_column):
    results = []
    conn = psycopg2.connect(host="localhost", database="tigis", user="robwebster", password="1emedente0486", port=5431)
    c = conn.cursor()
    c.execute(f"SELECT {select_term} FROM {table_name} ORDER BY {order_column}")

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
            my_class = MyClass(a, b, c, d)
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


def assign_field_colours(fields, crops):
    for field in fields:
        for crop in crops:
            if field.crop_id == crop.crop:
                field.fill = get_field_colour(crop.name)
                crop.fill = field.fill
            else:
                continue


def assign_find_colours(finds, classes):
    for find in finds:
        for cls in classes:
            if find.find_type == cls.class_type:
                find.fill = get_find_colour(cls.class_type)
                cls.fill = find.fill
            else:
                continue


def assign_crop_names(fields, crops):
    for field in fields:
        field.crop_name = get_crop_name(crops, field.crop_id)


def assign_class_names(finds, classes):
    for find in finds:
        find.class_name = get_class_name(classes, find.find_type)