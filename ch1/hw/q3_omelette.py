# from math import floor
import math
from math import *

egg_boxes = 2
eggs_per_omelette = 4
eggs_per_box = 6

total_omelettes = math.floor(( egg_boxes * eggs_per_box ) / eggs_per_omelette)  # could also use int(), or round() here

def ceil(num):
    return num + 1

ceil(1)

omelette_word = "omelette"

if (total_omelettes == 1):
    omelette_word = "omelette"
else:
    omelette_word = "omelettes"

print(f'You can make {total_omelettes} {omelette_word} with {egg_boxes} of egg boxes')

