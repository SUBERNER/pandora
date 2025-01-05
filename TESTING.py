import Buffle
import os

base = os.getcwd()
path = base + "\\entities"


Buffle.Inner.normal(Buffle.Search.full(path, True, False), r'"identifier": ".*"')