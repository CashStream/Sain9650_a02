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


from Food import Food
from Food_utilities import read_foods, by_origin

file = open('food.txt', "r")

foods = read_foods(file)

file.close()

origin = int(input(f"Enter a origin as an "))

origins = by_origin(foods, origin)

for food in origins:
    print(food, end="\n\n")
