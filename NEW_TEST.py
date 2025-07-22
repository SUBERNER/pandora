import Massma
import os
import re

print(os.getcwd())

# SETTING UP LOGGERS
log_name_value = None
log_output_value = True

Massma.Display.methods.set_log_output(log_output_value)
Massma.Display.outer.set_log_output(log_output_value)
Massma.Display.inner.set_log_output(log_output_value)
Massma.Display.image.set_log_output(log_output_value)
Massma.Display.audio.set_log_output(log_output_value)
Massma.Display.filter.set_log_output(log_output_value)
Massma.Display.search.set_log_output(log_output_value)

Massma.Display.methods.set_log_name(log_name_value)
Massma.Display.outer.set_log_name(log_name_value)
Massma.Display.inner.set_log_name(log_name_value)
Massma.Display.image.set_log_name(log_name_value)
Massma.Display.audio.set_log_name(log_name_value)
Massma.Display.filter.set_log_name(log_name_value)
Massma.Display.search.set_log_name(log_name_value)

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

Massma.Display.outer.set_flatten_output(False)
Massma.Display.outer.set_raw_error(True)

Massma.Display.inner.set_flatten_output(False)
Massma.Display.inner.set_raw_error(True)

Massma.Display.methods.set_flatten_output(False)
Massma.Display.methods.set_raw_error(True)


# SETS UP TEST FILES HERE
# deletes old folders
#Massma.delete("OUTER_NORMAL - Copy")
#Massma.delete("OUTER_GROUP - Copy")
#Massma.delete("ENTITIES - Copy")
# copies all files in one folder to newly created folders
if not os.path.exists("OUTER_NORMAL - Copy"):
    Massma.copy("OUTER_NORMAL","OUTER_NORMAL - Copy")
if not os.path.exists("OUTER_GROUP - Copy"):
    Massma.copy("OUTER_GROUP","OUTER_GROUP - Copy")
if not os.path.exists("ENTITIES - Copy"):
    Massma.copy("ENTITIES", "ENTITIES - Copy")
if not os.path.exists("FEATURES - Copy"):
    Massma.copy("FEATURES", "FEATURES - Copy")
# OUTER NORMAL

normal = Massma.Search.full("OUTER_NORMAL - Copy")
#preshuffle = list(range(len(normal)))
#print(preshuffle)
#preshuffle.reverse()
#print(preshuffle)
#Massma.Outer.normal(normal, preshuffle=preshuffle)
finds_normal = Massma.Search.outer(normal, False)
print(len(finds_normal))
print(finds_normal)

Massma.seed(123456789)
# OUTER GROUP
group = Massma.Search.full("OUTER_GROUP - Copy")
preshuffle = [0,1,2,3]
preset = ["BROWN","RED","WHITE","BLUE"]
print(preshuffle)
Massma.Outer.group(group, ['double','rose','tulip', "lilly"], preshuffle=preshuffle, preset=preset, chance_contains=0.5)
finds_group = Massma.Search.outer(group, True, contains=['double','rose','tulip', "lilly"])
print(len(finds_group))
print(finds_group)

"""
# INNER NORMAL
Massma.Display.inner.set_source_compression(True)
Massma.Display.inner.set_raw_error(True)
entites_normal = Massma.Search.full(os.path.abspath("ENTITIES - Copy"))
Massma.Inner.normal(entites_normal,[r'"identifier": ".*"', '"format_version": ".*"'], preshuffle=[9,8,7,6,5,4,3,2,1,0], )
#Massma.Inner.offset(entites_normal,[r'"damage": -?\d+\.?\d*'], (0.01, 100), zeros=True, clamps_outer=(1,100), matching=True)
#Massma.Inner.offset(entites_normal,[r'"damage": -?\d+\.?\d*'], (-5, 5))
# ERRORS 266, INTS ON FLOAT VALUES
features_normal = Massma.Search.full(os.path.abspath("FEATURES - Copy"))
#Massma.Inner.scale(features_normal,[r'"numerator": -?\d+\.?\d*,.*"denominator": -?\d+\.?\d*'], (1, 1, minmaxing=True, zeros=False,flags=[re.M, re.S])
#Massma.Inner.group(features_normal,[r'"numerator": -?\d+\.?\d*','"denominator": -?\d+\.?\d*'], duplicate=False)
group_data = Massma.Search.inner(features_normal, True, contains=[r'"numerator": -?\d+\.?\d*','"denominator": -?\d+\.?\d*'])
print(group_data)
normal_data = Massma.Search.inner(features_normal, False, contains=[r'"numerator": -?\d+\.?\d*','"denominator": -?\d+\.?\d*'])
print(normal_data)
"""
#Massma.Audio.volume("MUSIC\\TESTING - Copy.mp3", 3)

#Massma.Display.image.set_raw_error(True)
#Massma.Display.image.set_flatten_output(False)
#Massma.Image.create("SHEET_TEST\\SHEET_test.png", size=(100,100))
#Massma.Image.crop("SHEET_TEST\\SHEET - Copy.png", (0,0,16,16))
#Massma.Image.layer("SHEET_TEST\\SHEET_test.png","SHEET_TEST\\SHEET - Copy.png",(0,16))