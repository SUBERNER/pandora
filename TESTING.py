import Buffle

import os

path = os.getcwd()

Buffle.Text.multiple_group(path + "\\OTHER", ['"identifier": ".*"', '"population_control": ".*"'], 1)


