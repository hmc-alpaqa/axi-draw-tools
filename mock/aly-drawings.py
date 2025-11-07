import random
from pyaxidraw import axidraw
from svg.path import parse_path
from xml.dom import minidom

file_name = "my_drawing-2.svg" 
ad = axidraw.AxiDraw()

ad.plot_setup(file_name)

## PEN OPTIONS ##
ad.options.speed_pendown = 50
ad.options.speed_penup = 50
ad.options.pen_pos_up = 60
ad.options.pen_pos_down = 30

## SVG OPTIONS ##
ad.options.scale = 3  # Scale factor (0.25 = quarter size, 0.5 = half size, 2.0 = double size)

# not sure how well these work, apparently the svg file settings override these
ad.options.pos_x = 0  # X position offset in cm
ad.options.pos_y = 0  # Y position offset in cm

ad.options.constrain = True  # Constrain drawing to page bounds

# ad.options.copies = 3 # Draws three copies
# ad.options.page_delay = 0 # Doesn't wait between copies, useful if you wanted to change the page or something

ad.plot_run()

ad.disconnect()