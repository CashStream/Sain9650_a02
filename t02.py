"""
-------------------------------------------------------
Food class 
-------------------------------------------------------
Author:  Akaash Saini
ID:      210279650
Email:   sain9650@mylaurier.ca
Section: CP164-L2
__updated__ = "2022-01-15"
-------------------------------------------------------
"""
from Food_utilities import read_food, average_calories

gulab_jamun = read_food('Gulab Jamun|2|True|300')

spanakopita = read_food('Spanakopita|5|True|260')

avg = average_calories([gulab_jamun, spanakopita])

print(f"Average Calories: {avg}")
