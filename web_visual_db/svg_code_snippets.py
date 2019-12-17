import cx_Oracle
import cgi
import cgitb
cgitb.enable()

def printSVGhtml():
    print("Content-Type: text/html\n")

    print("<!DOCTYPE html>")
    print("<head>")
    print("<title>SVG Example</title>")
    print("</head>")

    print("<body>")

    print('<svg width="10cm" height="10cm" viewBox="0 0 16 16">')

    print('<rect x="1" y="7" width="5" height="5" fill="red" stroke="black" stroke-width="0.5" />')

    print('<circle cx="13" cy="3" r="3" fill="yellow" />')

    print('<line x1="0" y1="14" x2="16" y2="14" stroke="green" stroke-width="0.1"/>')

    print('<polyline points="0,7 2,5 3.7,5 3.7,4.5 4,4.5 4,5 5,5 7,7 0,7" fill="brown" stroke="black" stroke-width="0.5" />')

    print ('<text x="1" y="15.5" font-family="Verdana" font-size="1" fill="blue">Hello World!</text>')

    print('</svg>')


    print("</body>")
    print("</html>")
