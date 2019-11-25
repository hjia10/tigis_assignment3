import cx_Oracle


def getDBdata(select_term, table_name):
    conn = cx_Oracle.connect("student/train@geosgen")
    c = conn.cursor()
    c.execute("SELECT " + select_term + " FROM " + table_name + '\"')
    html = ''
    for row in c:
        html = html + row[0] + " - " + row[1] + " (" + row[4] + ") "'<br>'
    conn.close()
    return html


data = getDBdata('*', 'ancient_castles')
print(data)