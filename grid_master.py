title_ascii_art = """
GRID MASTER!!
"""
print title_ascii_art
rows = int(raw_input("rows: "))
columns = int(raw_input("columns: "))
#grid_gaps = raw_input("grid gaps? [y/n]")
horizontal_grid_gap = ""
vertical_grid_gap = ""
#if grid_gaps == "y":
    #horizontal_grid_gap = raw_input("horizontal grid gap size: ")
    #vertical_grid_gap = raw_input("vertical grid gap size: ")
html_file_name = "index.html"
css_file_name = "style.css"
html_file = open(html_file_name, "w")
css_file = open(css_file_name, "w")
#Flexbox centering code.
css = ".centerXY{display:flex;justify-content:center;align-items:center;}\n"
#CSS grid areas spec code.
css += """.grid{
    display:-ms-grid;
    display:grid;
    -ms-grid-rows:"""
for i in range(rows):
    css += " 100px"
css += ";\n    -ms-grid-columns:"
for i in range(columns):
    css += " 100px"
css += ";\n    grid-template:\n"
for i in range(rows):
    css += "    \""
    for j in range(columns):
        if j == columns - 1:
            css += str(i + 1) + "_" + str(j + 1)
        else:
            css += str(i + 1) + "_" + str(j + 1) + "   "
    if i == rows - 1:
        css += "\" 100px /\n    "
    else:
        css += "\" 100px\n"
for i in range(columns):
    if i == columns - 1:
        css += "100px;\n}\n"
    else:
        css += "100px "
#CSS grid cell spec code.
for i in range(rows):
    for j in range(columns):
        css += ".cell-" + str(i + 1) + "_" + str(j + 1) + "{\n"
        css += "    -ms-grid-row: " + str(i + 1) + ";\n"
        css += "    -ms-grid-column: " + str(j + 1) + ";\n"
        css += "    grid-area: " + str(i + 1) + "_" + str(j + 1) + ";\n"
        css += "    height: 100px;\n"
        css += "    width: 100px;\n}\n"
#Code to generate all html grid divs.
grid_divs = ""
for i in range(rows):
    for j in range(columns):
        if i == rows - 1  and j == columns - 1:
            grid_divs += "            <div class=\"cell-" + str(i + 1) + "_" + str(j + 1) + " centerXY\">" + str(i + 1) + "_" + str(j + 1) + "</div>"
        else:
            grid_divs += "            <div class=\"cell-" + str(i + 1) + "_" + str(j + 1) + " centerXY\">" + str(i + 1) + "_" + str(j + 1) + "</div>\n"
html = """<html>
    <head>
        <title>Grid Master</title>
        <link rel="stylesheet" type="text/css" href=\"""" + css_file_name + """\">
    </head>
    <body>
        <div class="grid">
""" + grid_divs + """
        </div>
    </body>
</html>"""
html_file.write(html)
html_file.close()
css_file.write(css)
css_file.close()