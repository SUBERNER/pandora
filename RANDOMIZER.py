import Massma
import os
import re

# setup methods
base = os.getcwd()
original_base = base + "\\FILES_ORIGINAL"
altered_base = base + "\\FILES_ALTERED"
system = Massma.Display.Result()

#EDIT THIS TO CHANGE WHAT AND HOW DATA IS SHUFFLED
#Massma.Methods.seed(439853598)

# editing displays to make outputs cleaner
Massma.Display.inner.set_source_compression(True)
Massma.Display.outer.set_source_compression(True)
Massma.Display.methods.set_source_compression(True)
Massma.Display.filter.set_source_compression(True)
Massma.Display.search.set_source_compression(True)
Massma.Display.audio.set_source_compression(True)
Massma.Display.inner.set_raw_error(True)
Massma.Display.outer.set_raw_error(True)
Massma.Display.methods.set_raw_error(True)
Massma.Display.filter.set_raw_error(True)
Massma.Display.search.set_raw_error(True)
Massma.Display.audio.set_raw_error(True)
Massma.Display.inner.set_flatten_output(True)
Massma.Display.outer.set_flatten_output(True)
Massma.Display.methods.set_flatten_output(True)
Massma.Display.filter.set_flatten_output(True)
Massma.Display.search.set_flatten_output(True)
Massma.Display.audio.set_flatten_output(True)

# creates new file to be altered
if os.path.exists(altered_base):
    system.result_warning(altered_base, "RANDOMIZER", "Delete/Remove CHANGED files before rerunning code")
else:
    Massma.Methods.copy(original_base, altered_base)

# BEHAVIOR PACKS BEHAVIOR PACKS BEHAVIOR PACKS
# BEHAVIOR PACKS BEHAVIOR PACKS BEHAVIOR PACKS
# BEHAVIOR PACKS BEHAVIOR PACKS BEHAVIOR PACKS


# entities
entities_list = []
entities_path = altered_base + "\\behavior_pack\\entities"


# spawn_rules
spawn_rules_list = []
spawn_rules_path = altered_base + "\\behavior_pack\\spawn_rules"


# spawn_groups
spawn_groups_list = []
spawn_groups_path = altered_base + "\\behavior_pack\\spawn_groups"


# trading
trading_list = []
trading_path = altered_base + "\\behavior_pack\\trading"


# loot
loot_list = []
loot_path = altered_base + "\\behavior_pack\\loot_tables"


# biomes
biomes_list = []
biomes_path = altered_base + "\\behavior_pack\\biomes"
biomes_list = Massma.Search.full(biomes_path)
# filters (its excluded if it does not contain the text in "")
nether_filter = Massma.Filter.Exclude(biomes_list,r'"nether"', logic_strings=Massma.Logic.NAND)
cave_filter = Massma.Filter.Exclude(biomes_list, r'"caves"', logic_strings=Massma.Logic.NAND)
end_filter = Massma.Filter.Exclude(biomes_list, r'"the_end"', logic_strings=Massma.Logic.NAND)
overworld_filter = Massma.Filter.Exclude(biomes_list, [r'"overworld"',r'"caves'], logic_strings=Massma.Logic.NOR)
# main shuffling and altering
Massma.Inner.normal(biomes_list, r'"identifier": ".*"', excludes=[nether_filter]) # nether
Massma.Inner.normal(biomes_list, r'"identifier": ".*"', excludes=[cave_filter]) # caves
Massma.Inner.normal(biomes_list, r'"identifier": ".*"', excludes=[end_filter]) # the_end
Massma.Inner.normal(biomes_list, r'"identifier": ".*"', excludes=[overworld_filter]) # overworld
# no section exclusive shuffling and altering
Massma.Inner.normal(biomes_list, r'"sea_material": ".*"', duplicate=True)
Massma.Inner.normal(biomes_list, r'"sea_floor_depth": -?\d*\.?\d+', duplicate=True, flatten=True)
Massma.Inner.scale(biomes_list, r'"sea_floor_depth": -?\d*\.?\d+', (-2.0, 2.0), decimals=False, mode= 1)
Massma.Inner.normal(biomes_list, r'"minecraft:overworld_height": {.*?},', duplicate=True, flatten=True, flags=[re.M, re.S])
#Massma.Inner.normal(biomes_list, r'"noise_type": ".*"', duplicate=True, flatten=True)
#Massma.Inner.normal(biomes_list, r'"noise_params": \[\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*\]', duplicate=True, flatten=True)
Massma.Inner.normal(biomes_list, [r'"blue_spores": .*', r'"ash": .*', r'"red_spores": .*', r'"white_ash": .*'])
Massma.Inner.scale(biomes_list, [r'"blue_spores": .*', r'"ash": .*', r'"red_spores": .*', r'"white_ash": .*'], (0.5, 2.0), decimals=True, rounding=2)
Massma.Inner.normal(biomes_list, r'"has_forest": .*', duplicate=True, flatten=True)
Massma.Inner.normal(biomes_list, r'"bryce_pillars": .*', duplicate=True, flatten=True)



# recipes
recipes_list = []
recipes_path = altered_base + "\\behavior_pack\\recipes"


# feature_rules
feature_rules_list = []
feature_rules_path = altered_base + "\\behavior_pack\\feature_rules"


# features
features_list = []
features_path = altered_base + "\\behavior_pack\\features"


# items
items_list = []
items_path = altered_base + "\\behavior_pack\\items"


# item catalogs
item_catalogs_list = []
item_catalogs_path = altered_base + "\\behavior_pack\\item_catalog"


# aim assists
aim_assists_list = []
aim_assists_path = altered_base + "\\behavior_pack\\aim_assist"


# behavior trees
behavior_trees_list = []
behavior_trees_path = altered_base + "\\behavior_pack\\behavior_trees"


# structures
structures_list = []
structures_path = altered_base + "\\behavior_pack\\structures"


# worldgens
worldgens_list = []
worldgens_path = altered_base + "\\behavior_pack\\worldgens"


# RESOURCE PACKS RESOURCE PACKS RESOURCE PACKS
# RESOURCE PACKS RESOURCE PACKS RESOURCE PACKS
# RESOURCE PACKS RESOURCE PACKS RESOURCE PACKS


# animation controllers
animation_controllers_list = []
animation_controllers_path = altered_base + "\\resource_pack\\animation_controllers"


# animations
animations_list = []
animations_path = altered_base + "\\resource_pack\\animations"


# atmospherics
atmospherics_list = []
atmospherics_path = altered_base + "\\resource_pack\\atmospherics"


# attachables
attachables_list = []
attachables_path = altered_base + "\\resource_pack\\attachables"


# biomes
biomes_list = []
biomes_path = altered_base + "\\resource_pack\\biomes"


# cameras
cameras_list = []
cameras_path = altered_base + "\\resource_pack\\cameras"


# color_gradings
color_gradings_list = []
color_gradings_path = altered_base + "\\resource_pack\\color_grading"


# entities
entities_list = []
entities_path = altered_base + "\\resource_pack\\entities"


# fogs
fogs_list = []
fogs_path = altered_base + "\\resource_pack\\fogs"


# fonts
fonts_list = []
fonts_path = altered_base + "\\resource_pack\\font"


# lightings
lightings_list = []
lightings_path = altered_base + "\\resource_pack\\lighting"


# materials
materials_list = []
materials_path = altered_base + "\\resource_pack\\materials"


# models
models_list = []
models_path = altered_base + "\\resource_pack\\models"


# particles
particles_list = []
particles_path = altered_base + "\\resource_pack\\particles"


# pdrs
pdrs_list = []
pdrs_path = altered_base + "\\resource_pack\\pdr"


# render_controllers
render_controllers_list = []
render_controllers_path = altered_base + "\\resource_pack\\render_controllers"


# shadows
shadows_list = []
shadows_path = altered_base + "\\resource_pack\\shadows"


# sounds
sounds_list = []
sounds_path = altered_base + "\\resource_pack\\sounds"


# text
texts_list = []
texts_path = altered_base + "\\resource_pack\\texts"


# textures
textures_list = []
textures_path = altered_base + "\\resource_pack\\textures"


# uis
uis_list = []
uis_path = altered_base + "\\resource_pack\\uis"


# waters
waters_list = []
waters_path = altered_base + "\\resource_pack\\water"


# displays edits made by code
Massma.Display.methods.result_stats()
Massma.Display.search.result_stats()
Massma.Display.filter.result_stats()
Massma.Display.inner.result_stats()
Massma.Display.outer.result_stats()
Massma.Display.image.result_stats()
Massma.Display.audio.result_stats()

Massma.Search.content()

"""
Clean up github repository
Finish the audio method, to a good state, or scrap it
Get sprite sheets to be editable and working within the image method
Fix Logic for Filters, with numbers
Add documentation to methods
Add documentation to the entire library
Get output listing/listing to a satisfiable state
Get weight to work properly
The ability to do contains in contains (groups)
ints and floats with scale and offset when changing values types (319)
Methods to only return the data that would be shuffled in inner methods, for preshuffles and weight
improve error handling
"""