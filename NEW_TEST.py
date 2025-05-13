import Massma
import os
import re

result_test = Massma.Display.Result()

print(F"TESTING, HELLO THERE!")
for color in Massma.Display.Color.GROUPS:
    print(f"{color}TESTING, HELLO THERE!{Massma.Display.Color.RESET}")

result_test.set_source_length("CHANGED\\bedrock-samples-1.21.50.7\\CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd())

print(f"{Massma.Display.Color.NOTIFY}TESTING, THIS IS A NOTIFICATION!{Massma.Display.Color.RESET}")
print(f"{Massma.Display.Color.ERROR}TESTING, THIS IS A ERROR!{Massma.Display.Color.RESET}")
print(f"{Massma.Display.Color.WARNING}TESTING, THIS IS A WARNING!{Massma.Display.Color.RESET}")

result_test.result("CHANGED\\bedrock-samples-1.21.50.7\\CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd(), "NORMAL", 0, 1)
result_test.result("CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd(), "NORMAL", 20, 0)
result_test.result("CHANGED\\bedrock-samples-1.21.50.7\\CHANGED\\bedrock-samples-1.21.50.7\\CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd(), "NORMAL", 5, 5)
result_test.result_warning("CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd(), "WARN", "this is a warning\nMORE WARNINGS")
result_test.result_notify("CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd(), "NOTIFY", "have a good day")
print("YES DONE")

"""
Massma.Display.filter.set_source_length(25)
Massma.Display.filter.set_source_compression(True)
swapping = Massma.Filter.Swap([(os.getcwd() + "\\ONE.txt", os.getcwd() + "\\THREE.txt"), (os.getcwd() + "\\TWO.txt", os.getcwd() + "\\FOUR.txt")])
swapping()
ignoring = Massma.Filter.Ignore(["CHANGED\\bedrock-samples-1.21.50.7\\CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd(), "bedrock-samples-1.21.50.7\\CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd()])
ignoring("CHANGED\\bedrock-samples-1.21.50.7\\CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd())
ignoring("bedrock-samples-1.21.50.7\\CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd())
swapping()

print("EXCLUDING")

exclude = Massma.Filter.Exclude(os.getcwd() + "\\ONE.txt", ["TWO", "SIX"], test_files=[os.getcwd() + "\\TWO.txt", os.getcwd() + "\\SIX.txt"],
                                logic_files=Massma.Logic.OR, logic_strings=Massma.Logic.OR)
exclude(os.getcwd() + "\\ONE.txt")

print("INPUT")

inputting = Massma.Filter.Input(os.getcwd() + "\\ONE.txt", ["111", "222", "333", "111"], logic_inputs=Massma.Logic.XNOR)
inputting(os.getcwd() + "\\ONE.txt", "111")

print("ALTER")
alter_path = os.getcwd() + "\\OTHERS - Copy"
altering = Massma.Filter.Alter([alter_path + "\\camel.json", alter_path + "\\goat.json", alter_path + "\\sheep.json"]
                               , [r'"is_spawnable": true', r'"is_summonable": false'], [(r'"entity_type": "minecraft:skeleton"', r'"entity_type": "minecraft:booba"'), (r'"weight": 80', r'"weight": 999')], logic_files=Massma.Logic.OR, logic_strings=Massma.Logic.OR,
                               replace_files=alter_path + "\\spider.json")
altering(alter_path + "\\goat.json")

print("SEARCH")

Massma.Display.search.set_raw_error(True)
Massma.Display.search.set_flatten_output(False)
Massma.Search.full(os.getcwd() + "\\SEARCH", deep_search=True)
files = Massma.Search.content(os.getcwd() + "\\SEARCH", ["monster", "overworld"], logic=Massma.Logic.OR, deep_search=True)
print(files)
"""

#ignoring = Massma.Filter.Ignore(os.getcwd() + "\\IMAGES\\eye.jpg")
#Massma.Display.image.set_raw_error(True)
#Massma.Display.image.set_flatten_output(False)
#Massma.Image.noise([os.getcwd() + "\\IMAGES\\eye - Copy.jpg", os.getcwd() + "\\IMAGES\\camera - Copy.png"], 0, 100, resampling=0, masks=[os.getcwd() + "\\IMAGES\\long.png", os.getcwd() + "\\IMAGES\\circle.png"])

Massma.Display.outer.set_flatten_output(True)
Massma.Display.outer.set_raw_error(True)
flowers = Massma.Search.full("OUTER_TEST - Copy")
#Massma.Outer.normal(flowers, preshuffle=[0, 1, 2, 3, 4, 5, 6, 12, 10, 11, 8, 9, 7], preset=['OUTER_TEST - Copy\\1.png', 'OUTER_TEST - Copy\\2.png', 'OUTER_TEST - Copy\\3.png', 'OUTER_TEST - Copy\\4.png', 'OUTER_TEST - Copy\\5.png', 'OUTER_TEST - Copy\\6.png', 'OUTER_TEST - Copy\\7.png', 'OUTER_TEST - Copy\\8.png', 'OUTER_TEST - Copy\\9.png', 'OUTER_TEST - Copy\\10.png', 'OUTER_TEST - Copy\\11.png', 'OUTER_TEST - Copy\\12.png', 'OUTER_TEST - Copy\\13.png'])
Massma.Outer.group(flowers, ['rose', 'tulip', 'double'], preset=['robert', 'penis', 'sigma'])