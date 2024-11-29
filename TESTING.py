import Buffle

import os

path = os.getcwd()
print(Buffle.Search.full(path + "\\EGG", False, False))
print(len(Buffle.Search.full(path + "\\EGG", False, False)))

Buffle.Outer.reverse(Buffle.Search.full(path + "\\EGG", False, False))

