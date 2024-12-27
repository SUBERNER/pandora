import Buffle
import os

base = os.getcwd()
path = base + "\\TEST"
path = Buffle.Search.full(path, True, False)
Buffle.Image.rotate(path, -30)







