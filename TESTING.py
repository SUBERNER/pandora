import random

import Buffle

import os

path = os.getcwd() + "\\IMAGES - Copy"

files = Buffle.Search.full(path, False, False)
Buffle.Texture.noise(files, 50)

