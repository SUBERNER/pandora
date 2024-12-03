import Buffle

import os

path = os.getcwd()
print(Buffle.Search.full(path + "\\TEST", False, False))
print(len(Buffle.Search.full(path + "\\TEST", False, False)))

Buffle.Outer.group(Buffle.Search.full(path + "\\TEST", False, False), ["red", "green", "blue"])

