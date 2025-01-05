import Buffle
import os

base = os.getcwd()
path = base + "\\COLOR"

Buffle.Outer.group(Buffle.Search.full(path, True, False), ["_blue", "_brown", "_green", "_pink", "_purple", "_red", "_white", "_yellow"], weight=[1, 1, 1, 1, 1, 1, 1, 1], duplicates=True)