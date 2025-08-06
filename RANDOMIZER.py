import random

import Massma
import os
import re


# setup methods
base = os.getcwd()
original_base = base + "\\FILES_ORIGINAL"
altered_base = base + "\\FILES_ALTERED"
log_base = "Massma_logs.txt"
system = Massma.Display.Result()

# clears data out of log file
with open(log_base, 'w') as f:  # opens file
    pass # removes all data in file, making a fresh log file
# enables and sets the log files for each display
Massma.Display.inner.set_log_output(False)
Massma.Display.outer.set_log_output(False)
Massma.Display.methods.set_log_output(False)
Massma.Display.filter.set_log_output(False)
Massma.Display.search.set_log_output(False)
Massma.Display.audio.set_log_output(False)
Massma.Display.inner.set_log_name(log_base)
Massma.Display.outer.set_log_name(log_base)
Massma.Display.methods.set_log_name(log_base)
Massma.Display.filter.set_log_name(log_base)
Massma.Display.search.set_log_name(log_base)
Massma.Display.audio.set_log_name(log_base)

#EDIT THIS TO CHANGE WHAT AND HOW DATA IS SHUFFLED
Massma.Methods.seed(159)

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
Massma.Display.inner.set_flatten_output(False)
Massma.Display.outer.set_flatten_output(False)
Massma.Display.methods.set_flatten_output(False)
Massma.Display.filter.set_flatten_output(False)
Massma.Display.search.set_flatten_output(False)
Massma.Display.audio.set_flatten_output(False)

# creates new file to be altered
if os.path.exists(altered_base):
    system.result_warning(altered_base, "RANDOMIZER", "Delete/Remove CHANGED files before rerunning code")
else:
    Massma.Methods.copy(original_base, altered_base)

# BEHAVIOR PACKS BEHAVIOR PACKS BEHAVIOR PACKS
# BEHAVIOR PACKS BEHAVIOR PACKS BEHAVIOR PACKS
# BEHAVIOR PACKS BEHAVIOR PACKS BEHAVIOR PACKS


# entities
entities_path = altered_base + "\\behavior_pack\\entities"
entities_list = []

"""
# spawn_rules
spawn_rules_path = altered_base + "\\behavior_pack\\spawn_rules"
spawn_rules_filter = [] # store each filtered list
slime_replace = [r'{"test": "has_biome_tag", "operator": "==", "value": "monster"},','{"test": "has_biome_tag", "operator": "==", "value": "swamp"},','{"test": "has_biome_tag", "operator": "==", "value": "mangrove_swamp"},','{"test": "has_biome_tag", "operator": "==", "value": "frozen"}'] # strings that will be swapped in slime replace
slime_filter = Massma.Filter.Alter(spawn_rules_path + "\\slime.json", slime_replace[0], [(slime_replace[0], ""),(slime_replace[2], ""),(slime_replace[3], slime_replace[2].replace('},','}'))], flags=[re.M, re.S]) # makes slime spawning seme more natural and similar to real minecraft
spawn_rules_list = Massma.Search.full(spawn_rules_path)
# filters (its excluded if it does not contain the text in "")
spawn_rules_filter.append([Massma.Filter.Exclude(spawn_rules_list,r'"minecraft:spawns_underwater":', logic_strings=Massma.Logic.AND)]) # if it does not spawn in water
spawn_rules_filter.append([Massma.Filter.Exclude(spawn_rules_list, r'"minecraft:spawns_underwater":', logic_strings=Massma.Logic.NAND)]) # if it spawns in water
for filter in spawn_rules_filter:
    Massma.Inner.group(spawn_rules_list, [r'"identifier": ".*"', r'"population_control": ".*"'], excludes=filter, alters=slime_filter)  # shuffles what mobs are effects by each spawn rule
Massma.Inner.normal(spawn_rules_list, r'"minecraft:herd": \{.*?\}', flags=[re.M, re.S])  # shuffles the size of mob spawn groups
Massma.Inner.offset(spawn_rules_list, r'"minecraft:herd": \{.*?\}',(-2, 2), flags=[re.M, re.S], decimals=False, zeros=False)  # allowing values of 1 to be effect by scale
Massma.Inner.scale(spawn_rules_list, r'"minecraft:herd": \{.*?\}',(0.5, 2), flags=[re.M, re.S], minmaxing=True, decimals=False, zeros=False)  # multiplies and divides the size of mob spawn groups
Massma.Inner.normal(spawn_rules_list, r'"minecraft:weight": \{.*?\}', flags=[re.M, re.S]) # shuffles the chance of that mob spawning
Massma.Inner.scale(spawn_rules_list, r'"minecraft:weight": \{.*?\}', (0.33, 3), flags=[re.M, re.S], decimals=False, zeros=False)
Massma.Inner.normal(spawn_rules_list, r'"minecraft:density_limit": \{.*?\}', flags=[re.M, re.S]) # shuffles how many can spawn in a given area
Massma.Inner.scale(spawn_rules_list, r'"minecraft:distance_filter": \{.*?\}', (0.5, 2), flags=[re.M, re.S], minmaxing=True ,decimals=False, zeros=True) # how close each spawn group can be from each other
Massma.Inner.normal(spawn_rules_list, r'"minecraft:brightness_filter": \{.*?\}', flags=[re.M, re.S]) # shuffles what brightness mobs can spawn
"""
"""
# spawn_groups
spawn_groups_path = altered_base + "\\behavior_pack\\spawn_groups"
spawn_groups_list = Massma.Search.full(spawn_groups_path)
# no section exclusive shuffling and altering
Massma.Inner.normal(spawn_groups_list, r'"identifier": ".*"')
Massma.Inner.normal(spawn_groups_list, r'"entity_type": ".*"')
Massma.Inner.normal(spawn_groups_list, r'"minecraft:herd": {.*?},')
Massma.Inner.scale(spawn_groups_list, [r'"minecraft:herd": {.*?},'], (0.5, 2), zeros=False, decimals=False, minmaxing=True) # multiplies or divides the min and max values of data
"""
"""
# trading
trading_path = altered_base + "\\behavior_pack\\trading"
trading_list = [] # stores each villager trade type
wandering_filter = Massma.Filter.Ignore(Massma.Search.name(trading_path + "\\economy_trades","wandering_trader")) # ignores wandering trader
trading_list.append(Massma.Search.full(trading_path, ignores=wandering_filter)) # the list of v1 villager trades
trading_list.append(Massma.Search.full(trading_path + "\\economy_trades", ignores=wandering_filter)) # the list of v2 villager trades
trading_list.append(Massma.Search.name(trading_path + "\\economy_trades","wandering_trader")) # separates wandering trader do to its size of trades quantity
# shuffles data all together
for list in trading_list:
    Massma.Outer.normal(list) # shuffles the names of files, changing what types of trades are attached to each villager type
    Massma.Inner.normal(list, r'"levels": \{"min": -?\d*\.?\d+,"max": -?\d*\.?\d+\}', flags=[re.M, re.S])  # shuffles the quality of given item's enchantments during trade
    Massma.Inner.scale(list, r'"levels": \{"min": -?\d*\.?\d+,"max": -?\d*\.?\d+\}', (0.3, 33), flags=[re.M, re.S], decimals=False, minmaxing=True, zeros=False)  # multiplies or divides the quality of given item's enchantments during trade
# only for v1 villagers
Massma.Inner.normal(trading_list[0], r'"quantity": \{"min": -?\d*\.?\d+,"max": -?\d*\.?\d+\}', flags=[re.M, re.S])  # shuffles how much of an item villagers will give you in trade
Massma.Inner.scale(trading_list[0], r'"base_cost": -?\d*\.?\d+', (0.33, 3), decimals=False, minmaxing=True, zeros=False)  # multiplies or divides librarian villager's base cost for books
Massma.Inner.scale(trading_list[0], r'"base_random_cost": -?\d*\.?\d+', (0.33, 3), decimals=False, zeros=False)  # multiplies or divides librarian villager's base cost for books randomly added or subtracted
Massma.Inner.scale(trading_list[0], r'"per_level_random_cost": -?\d*\.?\d+', (0.33, 3), decimals=False, zeros=False)  # multiplies or divides librarian villager's cost based on per level added, randomly adding or subtracting
Massma.Inner.scale(trading_list[0], r'"per_level_cost": -?\d*\.?\d+', (0.33, 3), decimals=False, zeros=False)  # multiplies or divides librarian villager's cost based on per level added
#only for v2 villagers
for list in [trading_list[1], trading_list[2]]:
    Massma.Inner.scale(list, r'"quantity: -?\d*\.?\d+', (0.33, 3), decimals=False, zeros=False, clamps_outer=(0,1))  # multiplies or divides the quality of given item during trade
    Massma.Inner.normal(list, r'"price_multiplier": -?\d*\.?\d+')  # shuffles how much a price is multiplied by based on in game scenarios
    Massma.Inner.scale(list, r'"price_multiplier": -?\d*\.?\d+', (0.33, 3), decimals=True)  # multiplies or divides how much a price is multiplied by based on in game scenarios
    Massma.Inner.normal(list, r'"max_uses": -?\d*\.?\d+') # shuffles the amount of times you can trade for an item
    Massma.Inner.scale(list, r'"max_uses": -?\d*\.?\d+', (0.33, 3), decimals=False, zeros=False) # multiplies or divides the amount of times you can trade for an item
    Massma.Inner.normal(list, r'"gives": \[.*?\],"wants": \[.*?\],', flags=[re.M, re.S]) # shuffles what a village gives for each trade
"""
"""
# loot
loot_list = [] # the list of each section of loot_tables
loot_path = altered_base + "\\behavior_pack\\loot_tables"
# sets up the groups for each section of loot tables to be shuffled
loot_list.append([Massma.Search.full(loot_path + "\\chests", deep_search=True)]) # chests

loot_list.append([Massma.Search.full(loot_path + "\\dispensers", deep_search=True)]) # dispensers
loot_list[-1].append(Massma.Search.name(loot_path + "\\chests", contains="dispenser" ,deep_search=True))  # dispensers
dispenser_filter = Massma.Filter.Ignore(loot_path + "\\chests\\dispenser_trap.json") # used to ignore changes within chests

loot_list.append([Massma.Search.full(loot_path + "\\entities")]) # entities

loot_list.append([Massma.Search.name(loot_path + "\\entities", "gear")]) # raiding

loot_list.append([Massma.Search.name(loot_path + "\\entities", "gear")]) # gear

loot_list.append([Massma.Search.name(loot_path + "\\entities", "brushing")]) # brushing

loot_list.append([Massma.Search.full(loot_path + "\\equipment", deep_search=False)]) # equipment and armor
loot_list[-1].append(Massma.Search.name(loot_path + "\\gameplay\\entities", "armor_set")) # equipment and armor
loot_list[-1].append(Massma.Search.name(loot_path + "\\entities", "armor_set")) # equipment and armor
armor_filter = Massma.Filter.Ignore(Massma.Search.name(loot_path + "\\gameplay\\entities", "armor_set")) # used to ignore changes within entities

loot_list.append([Massma.Search.full(loot_path + "\\gameplay")]) # fishing
loot_list[-1].append(Massma.Search.full(loot_path + "\\gameplay\\fishing")) # fishing

loot_list.append([Massma.Search.full(loot_path + "\\gameplay\\entities")]) # gameplay

loot_list.append([Massma.Search.full(loot_path + "\\pots", deep_search=True)]) # pots

loot_list.append([Massma.Search.full(loot_path + "\\spawners", deep_search=True)])
"""
"""
# biomes
biomes_path = altered_base + "\\behavior_pack\\biomes"
biomes_list = Massma.Search.full(biomes_path)
biome_filters = [] # stores all biome filters
# filters (its excluded if it does not contain the text in "")
biome_filters.append([Massma.Filter.Exclude(biomes_list,r'"nether"', logic_strings=Massma.Logic.NAND)])
biome_filters.append([Massma.Filter.Exclude(biomes_list, r'"caves"', logic_strings=Massma.Logic.NAND)])
biome_filters.append([Massma.Filter.Exclude(biomes_list, r'"the_end"', logic_strings=Massma.Logic.NAND)])
biome_filters.append([Massma.Filter.Exclude(biomes_list, [r'"overworld"',r'"caves'], logic_strings=Massma.Logic.NOR)])
# shuffling based on filters
for filter in biome_filters:
    #Massma.Inner.normal(biomes_list, r'"identifier": ".*"', excludes=filter) # shuffles how biomes are identified in the system
    Massma.Inner.normal(biomes_list, r'"sea_floor_material": ".*"', excludes=filter) # shuffles the block used for the sea floor of a biome
    Massma.Inner.normal(biomes_list, r'"minecraft:multinoise_generation_rules": \{.*?\}', flags=[re.M, re.S], excludes=filter) # shuffles how and where nether biomes are created
    Massma.Inner.normal(biomes_list, r'"weight": -?\d*\.?\d+', excludes=filter) # shuffles the likelihood a biome is created
# no section exclusive shuffling and altering
Massma.Inner.normal(biomes_list, r'"sea_material": ".*"', duplicate=True) # changes the liquids to either water or lava
Massma.Inner.normal(biomes_list, [r'"blue_spores": .*', r'"ash": .*', r'"red_spores": .*', r'"white_ash": .*']) # shuffles the particles from nether biomes
Massma.Inner.scale(biomes_list, [r'"blue_spores": .*', r'"ash": .*', r'"red_spores": .*', r'"white_ash": .*'], (0.5,2.0), zeros=False, rounding=2, decimals=True) # multiplies and divides the particles from nether biomes
Massma.Inner.group(biomes_list, [r'"downfall": -?\d*\.?\d+',r'',r'"snow_accumulation": \[.*?\]','"temperature": -?\d*\.?\d+'], flags=[re.M, re.S]) # shuffles the climate of all biomes
Massma.Inner.normal(biomes_list, r'"minecraft:overworld_height": \{.*?\}', flags=[re.M, re.S]) # shuffles the terrain type of each biome
Massma.Inner.normal(biomes_list, r'"minecraft:overworld_generation_rules": \{.*?\}', flags=[re.M, re.S]) # shuffles the terrain type of each biome
Massma.Inner.normal(biomes_list, r'"sea_floor_depth": -?\d*\.?\d+', duplicate=True) # shuffles how far biome seas reach in oceans and rivers
Massma.Inner.scale(biomes_list, r'"sea_floor_depth": -?\d*\.?\d+', (0.33, 3)) # multiplies and devices how far biome seas reach in oceans and rivers
Massma.Inner.normal(biomes_list, r'"minecraft:mesa_surface": \{.*?\}', flags=[re.M, re.S]) # shuffles how each mesa biome generates
Massma.Inner.normal(biomes_list, [r'"bryce_pillars": true',r'"bryce_pillars": false'], duplicate=True) # shuffles if mesa biomes generate with giant pillars
Massma.Inner.normal(biomes_list, [r'"has_forest": true',r'"has_forest": false'], duplicate=True) # shuffles if mesa biomes generate with forests
Massma.Inner.group(biomes_list, [r'"noise_frequency_scale": -?\d*\.?\d+', r'"noise_range": \[ -?\d*\.?\d+, -?\d*\.?\d+ \]']) # shuffles sand will be normal or red
Massma.Inner.normal(biomes_list, [r'"north_slopes": true', r'"north_slopes": false', r'"east_slopes": true', r'"east_slopes": false', r'"south_slopes": true', r'"south_slopes": false', r'"west_slopes": true', r'"west_slopes": false'], duplicate=True) # shuffles which way slopes face
Massma.Inner.normal(biomes_list, [r'"top_slide": \{.*?\}'], flags=[re.M, re.S]) # shuffles if mountains have peaks
"""
"""
# recipes
recipes_path = altered_base + "\\behavior_pack\\recipes"
recipes_filter = [] # store each filtered list
recipes_list = Massma.Search.full(recipes_path)
# filters (its excluded if it does not contain the text in "")
recipes_filter.append([Massma.Filter.Exclude(recipes_list,r'"tags": \[\s*"crafting_table"\s*\]', logic_strings=Massma.Logic.NAND, flags=[re.M, re.S])])
recipes_filter.append([Massma.Filter.Exclude(recipes_list, r'"tags": \[\s*"brewing_stand"\s*\]', logic_strings=Massma.Logic.NAND, flags=[re.M, re.S])])
recipes_filter.append([Massma.Filter.Exclude(recipes_list, r'"tags": \["furnace"', logic_strings=Massma.Logic.NAND, flags=[re.M, re.S])])
recipes_filter.append([Massma.Filter.Exclude(recipes_list, r'"tags": \[\s*"deprecated"\s*\]', logic_strings=Massma.Logic.NOR, flags=[re.M, re.S])]) # LOOK MORE INTO THIS ON
recipes_filter.append([Massma.Filter.Exclude(recipes_list, r'"tags": \[\s*"stonecutter"\s*\]', logic_strings=Massma.Logic.NAND, flags=[re.M, re.S])])
recipes_filter.append([Massma.Filter.Exclude(recipes_list, r'"tags": \[\s*"smithing_table"\s*\]', logic_strings=Massma.Logic.NAND, flags=[re.M, re.S])])
# shuffling based on filters
for filter in recipes_filter:
    Massma.Inner.normal(recipes_list, r'"result": \{.*?\}', flags=[re.M, re.S], excludes=filter) # shuffles the results of each recipe
    Massma.Inner.normal(recipes_list, r'"output": ".*"', flags=[re.M, re.S], excludes=filter)  # shuffles the outputs of furnaces
    Massma.Inner.normal(recipes_list, r'"count": -?\d*\.?\d+', excludes=filter)  # shuffles the amount of items crafted
# shuffling only within each file
for file in recipes_list:
    Massma.Inner.normal(file, r'".": \{', flags=[re.M, re.S])  # shuffles assigned item amounts and placement for a recipe
"""
"""
# feature_rules
feature_rules_path = altered_base + "\\behavior_pack\\feature_rules"
feature_rules_list = Massma.Search.full(feature_rules_path)
distribution_filter = Massma.Filter.Ignore(Massma.Search.name(feature_rules_path, ["seagrass", "vines"], logic=Massma.Logic.OR)) # filters out files that break during distribution shuffle
# no section exclusive shuffling and altering
Massma.Inner.normal(feature_rules_list, r'[x-z][x-z][x-z]', duplicate=True) #coordinate_eval_order, or the order in which operation will happen
Massma.Inner.normal(feature_rules_list, r'"distribution": ".*"', duplicate=True, ignores=distribution_filter)
Massma.Inner.normal(feature_rules_list, r'"iterations": -?\d*\.?\d+')
Massma.Inner.offset(feature_rules_list, r'"iterations": -?\d*\.?\d+',(-2, 2),  zeros=True, decimals=False)  # allowing values of 1 to be effect by scale
Massma.Inner.scale(feature_rules_list, r'"iterations": -?\d*\.?\d+', (0.5, 2), zeros=True, decimals=False)
# extents with negatives
Massma.Inner.normal(feature_rules_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]')
Massma.Inner.offset(feature_rules_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]',(-2, 2),  zeros=True, decimals=False, minmaxing=True)  # allowing values of 1 to be effect by scale
Massma.Inner.scale(feature_rules_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]', (0.5, 2), zeros=True, decimals=False, minmaxing=True)
# extents without negatives
Massma.Inner.normal(feature_rules_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]')
Massma.Inner.offset(feature_rules_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]',(-2, 2),  zeros=True, decimals=False, minmaxing=True)  # allowing values of 1 to be effect by scale
Massma.Inner.scale(feature_rules_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]', (0.5, 2), zeros=True, decimals=False, minmaxing=True)
# PLACE FEATURE
# FEATURE PASS
"""

# features
features_path = altered_base + "\\behavior_pack\\features"
features_list = Massma.Search.full(features_path)
cocoa_filters = [] # used for filtering out coco in distribution
cocoa_filters.append([Massma.Filter.Exclude(features_list, r'cocoa', logic_strings=Massma.Logic.NAND)]) # if it has coco in the name
cocoa_filters.append([Massma.Filter.Exclude(features_list, r'cocoa', logic_strings=Massma.Logic.AND)]) # if it does not have coco in the name
# no section exclusive shuffling and altering
#Massma.Inner.normal(features_list, r'"iterations": -?\d*\.?\d+')
#Massma.Inner.offset(features_list, r'"iterations": -?\d*\.?\d+',(-2, 2), decimals=False, zeros=True)  # allowing values of 1 to be effect by scale
#Massma.Inner.scale(features_list, r'"iterations": -?\d*\.?\d+', (0.5, 2), zeros=True, decimals=False)
#Massma.Inner.normal(features_list, r'"count": -?\d*\.?\d+')
#Massma.Inner.scale(features_list, r'"count": -?\d*\.?\d+', (0.5, 2), zeros=False, decimals=False)
###Massma.Inner.normal(features_list, [r'"numerator": -?\d*\.?\d+,.*? "denominator": -?\d*\.?\d+'], flags=[re.M, re.S]) # FIX THIS FOR SOME REASOn
###Massma.Inner.offset(features_list, [r'"numerator": -?\d*\.?\d+,.*? "denominator": -?\d*\.?\d+'], (-2, 2), flags=[re.M, re.S], zeros=False, decimals=False, minmaxing=True)
###Massma.Inner.scale(features_list, [r'"numerator": -?\d*\.?\d+,.*? "denominator": -?\d*\.?\d+'], (0.5, 2), flags=[re.M, re.S], zeros=False, decimals=False, minmaxing=True)
###Massma.Inner.normal(features_list, r'"range_min": -?\d*\.?\d+, "range_max": -?\d*\.?\d+', flags=[re.M, re.S])
###Massma.Inner.scale(features_list, r'"range_min": -?\d*\.?\d+, "range_max": -?\d*\.?\d+', (0.5,2), flags=[re.M, re.S], zeros=False, decimals=False, minmaxing=True)
###Massma.Inner.normal(features_list, r'"min": -?\d*\.?\d+, "max": -?\d*\.?\d+',  flags=[re.M, re.S])
###Massma.Inner.scale(features_list, r'"min": -?\d*\.?\d+, "max": -?\d*\.?\d+', (0.5,2), flags=[re.M, re.S], zeros=False, decimals=False, minmaxing=True)
###Massma.Inner.normal(features_list, r'"min": \[ -?\d*\.?\d+, -?\d*\.?\d+, -?\d*\.?\d+\], "max": \[ -?\d*\.?\d+, -?\d*\.?\d+, -?\d*\.?\d+\]',  flags=[re.M, re.S])
###Massma.Inner.scale(features_list, r'"min": \[ -?\d*\.?\d+, -?\d*\.?\d+, -?\d*\.?\d+\], "max": \[ -?\d*\.?\d+, -?\d*\.?\d+, -?\d*\.?\d+\]', (0.5,2), flags=[re.M, re.S], zeros=True, decimals=False, minmaxing=True)
###Massma.Inner.normal(features_list, r'"search_range": -?\d*\.?\d+')
###Massma.Inner.scale(features_list, r'"min": -?\d*\.?\d+, "max": -?\d*\.?\d+', (0.5,2), zeros=False, decimals=False)
#Massma.Inner.normal(features_list, r'[x-z][x-z][x-z]', duplicate=True) #coordinate_eval_order, or the order in which operation will happen
#Massma.Inner.normal(features_list, r'"distribution": ".*"', duplicate=True, excludes=cocoa_filters[1]) # does not affect coco
#Massma.Inner.normal(features_list, r'"distribution": ".*"', duplicate=True, excludes=cocoa_filters[0], preset=['"distribution": "fixed_grid"', '"distribution": "jittered_grid"']) # does effect coco
#Massma.Inner.normal(features_list, r'"iterations": -?\d*\.?\d+')
#Massma.Inner.offset(features_list, r'"iterations": -?\d*\.?\d+',(-2, 2),  zeros=True, decimals=False)  # allowing values of 1 to be effect by scale
#Massma.Inner.scale(features_list, r'"iterations": -?\d*\.?\d+', (0.5, 2), zeros=True, decimals=False)
# extents with negatives
#Massma.Inner.normal(features_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]')
#Massma.Inner.offset(features_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]',(-2, 2),  zeros=True, decimals=False, minmaxing=True)  # allowing values of 1 to be effect by scale
#Massma.Inner.scale(features_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]', (0.5, 2), zeros=True, decimals=False, minmaxing=True)
# extents without negatives
#Massma.Inner.normal(features_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]')
#Massma.Inner.offset(features_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]',(-2, 2),  zeros=True, decimals=False, minmaxing=True)  # allowing values of 1 to be effect by scale
#Massma.Inner.scale(features_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]', (0.5, 2), zeros=True, decimals=False, minmaxing=True)
# trees
Massma.Inner.normal(features_list, r'"canopy_height": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"canopy_height": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"canopy_radius": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"canopy_radius": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"leaf_placement_attempts": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"leaf_placement_attempts": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"one_branch": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"one_branch": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"two_branches": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"two_branches": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"two_branches_and_trunk": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"two_branches_and_trunk": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"height": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"height": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"radius": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"radius": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"wide_bottom_layer_hole_chance": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"wide_bottom_layer_hole_chance": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"corner_hole_chance": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"corner_hole_chance": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"hanging_leaves_chance": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"hanging_leaves_chance": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"hanging_leaves_extension_chance": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"hanging_leaves_extension_chance": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"variance": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"variance": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"scale": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"scale": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"density": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"density": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"min_altitude_factor": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"min_altitude_factor": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"width_scale": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"width_scale": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"foliage_altitude_factor": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"foliage_altitude_factor": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"min_width": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"min_width": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"rise": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"rise": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"run": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"run": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"decoration_chance": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"decoration_chance": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"core_width": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"core_width": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"base_radius": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"base_radius": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"radius_step_modifier": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"radius_step_modifier": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"num_clusters": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"num_clusters": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'"cluster_radius": -\d*\.?\d+')
Massma.Inner.scale(features_list, r'"cluster_radius": -\d*\.?\d+', (0.5,2))
Massma.Inner.normal(features_list, r'')
Massma.Inner.scale(features_list, r'', (0.5,2))
Massma.Inner.normal(features_list, r'')
Massma.Inner.scale(features_list, r'', (0.5,2))
Massma.Inner.normal(features_list, r'')
Massma.Inner.scale(features_list, r'', (0.5,2))
Massma.Inner.normal(features_list, r'')
Massma.Inner.scale(features_list, r'', (0.5,2))
Massma.Inner.normal(features_list, r'')
Massma.Inner.scale(features_list, r'', (0.5,2))
Massma.Inner.normal(features_list, r'')
Massma.Inner.scale(features_list, r'', (0.5,2))
Massma.Inner.normal(features_list, r'')
Massma.Inner.scale(features_list, r'', (0.5,2))
Massma.Inner.normal(features_list, r'')
Massma.Inner.scale(features_list, r'', (0.5,2))
Massma.Inner.normal(features_list, r'')
Massma.Inner.scale(features_list, r'', (0.5,2))
Massma.Inner.normal(features_list, r'')
Massma.Inner.scale(features_list, r'', (0.5,2))
Massma.Inner.normal(features_list, r'')
Massma.Inner.scale(features_list, r'', (0.5,2))
Massma.Inner.normal(features_list, r'')
Massma.Inner.scale(features_list, r'', (0.5,2))
Massma.Inner.normal(features_list, r'')
Massma.Inner.scale(features_list, r'', (0.5,2))
Massma.Inner.normal(features_list, r'')
Massma.Inner.scale(features_list, r'', (0.5,2))
Massma.Inner.normal(features_list, r'')
Massma.Inner.scale(features_list, r'', (0.5,2))


# items
items_path = altered_base + "\\behavior_pack\\items"
items_list = []


# item catalogs
item_catalogs_path = altered_base + "\\behavior_pack\\item_catalog"
item_catalogs_list = []


# aim assists
aim_assists_path = altered_base + "\\behavior_pack\\aim_assist"
aim_assists_list = []


# behavior trees
behavior_trees_path = altered_base + "\\behavior_pack\\behavior_trees"
behavior_trees_list = []


# structures
structures_path = altered_base + "\\behavior_pack\\structures"
structures_list = []


# worldgens
worldgens_path = altered_base + "\\behavior_pack\\worldgens"
worldgens_list = []


# RESOURCE PACKS RESOURCE PACKS RESOURCE PACKS
# RESOURCE PACKS RESOURCE PACKS RESOURCE PACKS
# RESOURCE PACKS RESOURCE PACKS RESOURCE PACKS


# animation controllers
animation_controllers_list = []
animation_controllers_path = altered_base + "\\resource_pack\\animation_controllers"


# animations
animations_path = altered_base + "\\resource_pack\\animations"
animations_list = []


# atmospherics
atmospherics_path = altered_base + "\\resource_pack\\atmospherics"
atmospherics_list = []


# attachables
attachables_path = altered_base + "\\resource_pack\\attachables"
attachables_list = []

"""
# biomes (ATTACH/SYNC TO FOG SHUFFLES)
biomes_path = altered_base + "\\resource_pack\\biomes"
biomes_list = Massma.Search.full(biomes_path)
# shuffles all the data together
Massma.Inner.normal(biomes_list ,r'"identifier": ".*"') # shuffles how biomes are identified for everthing else
Massma.Inner.normal(biomes_list ,r'"sky_color": ".*"') # shuffles the color of the biome
Massma.Inner.normal(biomes_list ,r'"fog_identifier": ".*"') # shuffles what fog the biome uses
Massma.Inner.normal(biomes_list ,r'"surface_color": ".*"') # shuffles how water looks when not in it in that biome
Massma.Inner.normal(biomes_list ,[r'"color": \{.*\}', r'"color": ".*"'], flags=[re.M, re.S]) # shuffles the color assigned to grass and greenery in the biome
Massma.Inner.normal(biomes_list, r'"atmosphere_identifier": ".*"') # shuffles the type of atmosphere the biome will use
Massma.Inner.normal(biomes_list, r'"color_grading_identifier": ".*"') # shuffles the type of color grading the biome will use
Massma.Inner.normal(biomes_list, r'"lighting_identifier": ".*"') # shuffles the type of lighting the biome will use
Massma.Inner.normal(biomes_list, r'"water_identifier": ".*"') # shuffles the type of water the biome will use
Massma.Inner.group(biomes_list, [r'"addition": ".*"' ,r'"loop": ".*"' ,r'"mood": ".*"']) # shuffles the ambient sounds that play when in that biome
"""

# cameras
cameras_path = altered_base + "\\resource_pack\\cameras"
cameras_list = []

"""
# color_gradings
color_gradings_path = altered_base + "\\resource_pack\\color_grading"
color_gradings_list = Massma.Search.full(color_gradings_path)
Massma.Inner.normal(color_gradings_list, r'"identifier": ".*"') # shuffles what biome the color grading is assigned to
Massma.Inner.normal(color_gradings_list, r'"temperature": \{.*\}', flags=[re.M, re.S])  # shuffles the temperature based color grading
Massma.Inner.group(color_gradings_list, [r'"contrast": \[.*\]',r'"": \[.*\]',r'"gain": \[.*\]',r'"gamma": \[.*\]',r'"offset": \[.*\]', r'"saturation": \[.*\]'], flags=[re.M, re.S]) # shuffles groups of color grading, based on how colors, light, and shadows reach to each other
"""

# entities
entities_path = altered_base + "\\resource_pack\\entities"
entities_list = []

"""
# fogs
fogs_list = []
fogs_path = altered_base + "\\resource_pack\\fogs"
fogs_list = Massma.Search.full(fogs_path)
# shuffles all the data together
Massma.Inner.normal(fogs_list, '"identifier": ".*"') # shuffles how fogs are identified for each biome
Massma.Inner.group(fogs_list, [r'"fog_start": -?\d*\.?\d+',r'"fog_end": -?\d*\.?\d+']) # shuffles how close the fog is
Massma.Inner.normal(fogs_list, '"fog_color": ".*"') # shuffles the color of the fog
Massma.Inner.normal(fogs_list, '"render_distance_type": ".*"') # shuffles how the fog's distance is measured
Massma.Inner.group(fogs_list, [r'"min_percent": -?\d*\.?\d+', r'"mid_seconds": -?\d*\.?\d+', r'"mid_percent": -?\d*\.?\d+', r'"max_seconds": -?\d*\.?\d+']) #shuffles how the fog transitions between fogs
Massma.Inner.group(fogs_list,[r'"scattering": \[.*\]',r'"absorption": [.*]']) # shuffles how light is effected by blocks
Massma.Inner.group(fogs_list, [r'"max_density": -?\d*\.?\d+',r'"zero_density_height": -?\d*\.?\d+',r'"max_density_height": -?\d*\.?\d+']) # shuffles the opaqueness and dencity of the fog
Massma.Inner.normal(fogs_list, r'"henyey_greenstein_g": -?\d*\.?\d+')
"""

# fonts
fonts_path = altered_base + "\\resource_pack\\font"
fonts_list = []


# lightings
lightings_path = altered_base + "\\resource_pack\\lighting"
lightings_list = []


# materials
materials_path = altered_base + "\\resource_pack\\materials"
materials_list = []


# models
models_path = altered_base + "\\resource_pack\\models"
models_list = []


# particles
particles_path = altered_base + "\\resource_pack\\particles"
particles_list = []


# pdrs
pdrs_path = altered_base + "\\resource_pack\\pdr"
pdrs_list = []


# render_controllers
render_controllers_path = altered_base + "\\resource_pack\\render_controllers"
render_controllers_list = []

"""
# shadows
shadows_path = altered_base + "\\resource_pack\\shadows"
shadows_list = Massma.Search.full(shadows_path)
# change file data
Massma.Inner.normal(shadows_list, r'"shadow_style": ".*"', preset=[r'"shadow_style": "blocky_shadows"',r'"shadow_style": "soft_shadows"']) # shuffles how shadows are rendered
Massma.Inner.normal(shadows_list, r'"texel_size": -?\d*\.?\d+', preset=[r'"texel_size": 16',r'""texel_size": 32']) # shuffles the resolution of blocky shadows
"""

# sounds
sounds_path = altered_base + "\\resource_pack\\sounds"
sounds_list = []


# text
texts_path = altered_base + "\\resource_pack\\texts"
texts_list = []



# textures
textures_path = altered_base + "\\resource_pack\\textures"
textures_list = []


# uis
uis_path = altered_base + "\\resource_pack\\uis"
uis_list = []


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

"""
Clean up github repository
Fix Logic for Filters, with numbers
Add documentation to methods
Add documentation to the entire library
Get weight to work properly
The ability to do contains in contains (groups)
improve error handling
problems with incorrect source length due to how files are stored (full path or part path)
NOT REQUIRED, but most likely best to clean up inner group, its messy
Image search, allowing users to find images just like file searches but with images metadata, such as the mode or dimensions of the image
Audio search, allowing users to find audios just like file searches but with audio metadata, such as the duration of the audio
Flags showing a warning with expected types of data
Not all source things in outputs align correct to text, some are smaller than the gap is giving
ERROR WITH LOGGING DATA, LOOK AT LATER (LOGGINE UNIQUE CHARACTERS)
add inner shuffling more similar to otter group, alloing users to shuffling evrything of the same data together, in groups
allow for full path searches, instead of only name searches
using scaling and offset, it will never reach the max number or very rarily if on non decimal mode
simple way to directly edit data inside files
in filters make it so when comparing file with files, it is the absolute paths of both files
stop access filters inside method you should not, like accessing swap inside Inner
get sets for filters
HARD: a way to inject shuffled data, allowing you to shuffle data info files that didnt even have that data in the first place
FIX OFFSETS WITH -1, 1 NOT CHANGING ANYTHING
allowing some kind of filter made for altering and controlling numbers
"""