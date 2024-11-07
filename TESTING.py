import Buffle

import os

path = os.getcwd()

print(Buffle.display_all_results())
print(Buffle.display_text_results())
print(Buffle.display_texture_results())
print(Buffle.display_file_results())
print(Buffle.display_manual_results())

Buffle.display_file_format(1)


Buffle.Texture.brightness(path + "\\gratisography-cool-cat.jpg", 3)


