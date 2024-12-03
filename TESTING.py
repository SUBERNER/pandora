import Buffle

import os



path = os.getcwd()

print(Buffle.Search.full(path + "\\ANVIL", False, False))
print(len(Buffle.Search.full(path + "\\ANVIL", False, False)))

files = Buffle.Search.full(path + "\\ANVIL", False, False)
Buffle.Outer.group(files,["_blue", "_red", "_green"])

