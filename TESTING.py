import Buffle

import os

path = os.getcwd()

S1 = '"value": 20'
S2 = '"value": "player"'
S3 = '"damage": 6'

print(Buffle.Search.content(path + "\\entities", [S1, S2], True, False))
print(len(Buffle.Search.content(path + "\\entities", [S1, S2], True, False)))
print("1--------------------1")
print(Buffle.Search.content(path + "\\entities", [S1, S2], True, True))
print(len(Buffle.Search.content(path + "\\entities", [S1, S2], True, True)))
print("2--------------------2")
print(Buffle.Search.content(path + "\\entities", S1, True, False))
print(len(Buffle.Search.content(path + "\\entities", S1, True, False)))
print("3--------------------3")
print(Buffle.Search.content(path + "\\entities", S1, True, True))
print(len(Buffle.Search.content(path + "\\entities", S1, True, True)))
print("4--------------------4")
print("4--------------------4")
print(Buffle.Search.content(path + "\\entities", [S1, S2], True, False, "any"))
print(len(Buffle.Search.content(path + "\\entities", [S1, S2], True, False, "any")))
print("5--------------------5")
print(Buffle.Search.content(path + "\\entities", [S1, S2], True, True, "any"))
print(len(Buffle.Search.content(path + "\\entities", [S1, S2], True, True, "any")))
print("6--------------------6")
print(Buffle.Search.content(path + "\\entities", S1, True, False, "any"))
print(len(Buffle.Search.content(path + "\\entities", S1, True, False, "any")))
print("7--------------------7")
print(Buffle.Search.content(path + "\\entities", S1, True, True, "any"))
print(len(Buffle.Search.content(path + "\\entities", S1, True, True, "any")))
print("8--------------------8")
print("8--------------------8")
print(Buffle.Search.full(path + "\\entities", True, False))
print(len(Buffle.Search.full(path + "\\entities", True, False)))

