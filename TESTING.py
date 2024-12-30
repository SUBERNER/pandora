import Buffle
import os

base = os.getcwd()
path = base + "\\FOOD.png"

Buffle.Image.rotate(path, 50, fillcolor=(255, 255, 255), expand=True)