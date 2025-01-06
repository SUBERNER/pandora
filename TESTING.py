import Buffle
import os

base = os.getcwd()
path = base + "\\entities"


Buffle.Inner.group(Buffle.Search.full(path, True, False), [r'"identifier": ".*",', r'"width": .*,', r'"height": .*'])