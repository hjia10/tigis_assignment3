import psycopg2


class Field:

    def __init__(self, field_id, lowx, lowy, hix, hiy):
        self.field_id = field_id
        self.lowx = lowx
        self.lowy = lowy
        self.hix = hix
        self.hiy = hiy
        self.width = hix - lowx
        self.height = hiy - lowy

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

    def __init__(self, find_id, xcoord, ycoord):
        self.find_id = find_id
        self.xcoord = xcoord
        self.ycoord = ycoord

    def show_info(self):
        print('Find ID : ' + str(self.find_id))
        print('Co-ordinates : (' + str(self.xcoord) + ',' + str(self.ycoord) + ')')

    def draw_svg_circle(self):
        svg_type = "circle"
        fill = '"green"'
        radius = "1"
        svg_string = '<' + svg_type + ' cx = ' + '"' + str(self.xcoord) + '"' + ' cy=' + '"' + str(self.ycoord) + '"' + ' r=' + '"' + str(radius) + '"' + ' fill=' + fill + '/>'
        print(svg_string)
        return svg_string


def print_svg(width, height, viewbox):
    print(f'<svg width="{width}" height="{height}" viewBox="{viewbox}">')


def getDBdata(select_term, table_name):
    results = []
    conn = psycopg2.connect(host="localhost", database="tigis", user="robwebster", password="1emedente0486", port=5431)
    c = conn.cursor()
    c.execute("SELECT " + select_term + " FROM " + table_name)

    if table_name == "fields":
        fields_list = []
        for row in c:
            (a, b, c, d, e) = row
            field_name = table_name[:-1] + str(a)
            # print('Field Name is : ' + field_name)
            field_name = Field(a, b, c, d, e)
            fields_list.append(field_name)
            results = fields_list

    elif table_name == "finds":
        finds_list = []
        for row in c:
            (a, b, c) = row
            find_name = table_name[:-1] + str(a)
            # print('Field Name is : ' + field_name)
            find_name = Find(a, b, c)
            finds_list.append(find_name)
            results = finds_list
    else:
        print("Table Name not supported...")

    conn.close()
    return results




