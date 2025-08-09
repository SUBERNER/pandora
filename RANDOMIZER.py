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
Massma.Methods.seed(127358492785)

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
entities_list = Massma.Search.full(entities_path)
entities_filter = []  # used for filtering and separating mobs, projectiles, mine carts, and boats
entities_ignore = [] # ignore used based on what should not be shuffled, such as outdated mobs, players, and bosses
entities_filter.append([Massma.Filter.Exclude(entities_list,r'"spawn_category": "(?![^"]*water)[^"]*"', logic_strings=Massma.Logic.NAND)])  # mobs, not including fish
entities_filter.append([Massma.Filter.Exclude(entities_list, r'"minecraft:projectile"', logic_strings=Massma.Logic.NAND)])  # projectiles
entities_filter.append([Massma.Filter.Exclude(entities_list, r'"family": \[ "minecart"', logic_strings=Massma.Logic.NAND)])  # minecart
entities_filter.append([Massma.Filter.Exclude(entities_list, r'"family": \[ "boat"', logic_strings=Massma.Logic.NAND)])  # boats
entities_filter.append([Massma.Filter.Exclude(entities_list, r'"spawn_category": ".*?water', logic_strings=Massma.Logic.NAND)])  # fish
entities_ignore.append(Massma.Filter.Ignore(Massma.Search.name(entities_path,["ender_dragon.json", "wither.json", "elder_guardian.json"], logic=Massma.Logic.OR)))  # bosses
entities_ignore.append(Massma.Filter.Ignore(Massma.Search.name(entities_path,["player.json","zombie_villager.json","villager.json", "npc.json", "armor_stand.json", "fishing_hook.json"], logic=Massma.Logic.OR)))  # non used entities
# shuffling based on filters
for filter in entities_filter:
    Massma.Inner.group(entities_list, [r'"identifier": ".*"', r'"width": -?\d*\.?\d+', r'"height": -?\d*\.?\d+'], ignores=entities_ignore, excludes=filter)  # shuffles how entities act
    # TRANSFORM
    # ENTITY

Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED ENTITIES")

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
Massma.Inner.offset(spawn_rules_list, r'"minecraft:herd": \{.*?\}',(-1, 1), flags=[re.M, re.S], decimals=False, zeros=False)  # allowing values of 1 to be effect by scale
Massma.Inner.scale(spawn_rules_list, r'"minecraft:herd": \{.*?\}',(0.33,3), flags=[re.M, re.S], minmaxing=True, decimals=False, zeros=False, fair_range=True)  # multiplies and divides the size of mob spawn groups
Massma.Inner.normal(spawn_rules_list, r'"minecraft:weight": \{.*?\}', flags=[re.M, re.S]) # shuffles the chance of that mob spawning
Massma.Inner.scale(spawn_rules_list, r'"minecraft:weight": \{.*?\}', (0.33,3), flags=[re.M, re.S], decimals=False, zeros=False, fair_range=True)
Massma.Inner.normal(spawn_rules_list, r'"minecraft:density_limit": \{.*?\}', flags=[re.M, re.S]) # shuffles how many can spawn in a given area
Massma.Inner.scale(spawn_rules_list, r'"minecraft:distance_filter": \{.*?\}', (0.33,3), flags=[re.M, re.S], minmaxing=True ,decimals=False, zeros=True, fair_range=True) # how close each spawn group can be from each other
Massma.Inner.normal(spawn_rules_list, r'"minecraft:brightness_filter": \{.*?\}', flags=[re.M, re.S]) # shuffles what brightness mobs can spawn

Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED SPAWN RULES")

# spawn_groups
spawn_groups_path = altered_base + "\\behavior_pack\\spawn_groups"
spawn_groups_list = Massma.Search.full(spawn_groups_path)
# no section exclusive shuffling and altering
Massma.Inner.normal(spawn_groups_list, r'"identifier": ".*"')
Massma.Inner.normal(spawn_groups_list, r'"entity_type": ".*"')
Massma.Inner.normal(spawn_groups_list, r'"minecraft:herd": {.*?},')
Massma.Inner.scale(spawn_groups_list, [r'"minecraft:herd": {.*?},'], (0.33,3), zeros=False, decimals=False, minmaxing=True, fair_range=True) # multiplies or divides the min and max values of data

Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED SPAWN GROUPS")

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
    Massma.Inner.normal(list, r'"levels": \{"min": -?\d*\.?\d+,.*?"max": -?\d*\.?\d+\}', flags=[re.M, re.S])  # shuffles the quality of given item's enchantments during trade
    Massma.Inner.scale(list, r'"levels": \{"min": -?\d*\.?\d+,.*?"max": -?\d*\.?\d+\}', (0.33,3), flags=[re.M, re.S], decimals=False, minmaxing=True, zeros=False, fair_range=True)  # multiplies or divides the quality of given item's enchantments during trade
# only for v1 villagers
Massma.Inner.normal(trading_list[0], r'"quantity": \{"min": -?\d*\.?\d+,.*?"max": -?\d*\.?\d+\}', flags=[re.M, re.S])  # shuffles how much of an item villagers will give you in trade
Massma.Inner.scale(trading_list[0], r'"base_cost": -?\d*\.?\d+', (0.33,3), decimals=False, minmaxing=True, zeros=False, fair_range=True)  # multiplies or divides librarian villager's base cost for books
Massma.Inner.scale(trading_list[0], r'"base_random_cost": -?\d*\.?\d+', (0.33,3), decimals=False, zeros=False, fair_range=True)  # multiplies or divides librarian villager's base cost for books randomly added or subtracted
Massma.Inner.scale(trading_list[0], r'"per_level_random_cost": -?\d*\.?\d+', (0.33,3), decimals=False, zeros=False, fair_range=True)  # multiplies or divides librarian villager's cost based on per level added, randomly adding or subtracting
Massma.Inner.scale(trading_list[0], r'"per_level_cost": -?\d*\.?\d+', (0.33,3), decimals=False, zeros=False, fair_range=True)  # multiplies or divides librarian villager's cost based on per level added
#only for v2 villagers
for list in [trading_list[1], trading_list[2]]:
    Massma.Inner.scale(list, r'"quantity: -?\d*\.?\d+', (0.33,3), decimals=False, zeros=False, clamps_outer=(0,1), fair_range=True)  # multiplies or divides the quality of given item during trade
    Massma.Inner.normal(list, r'"price_multiplier": -?\d*\.?\d+')  # shuffles how much a price is multiplied by based on in game scenarios
    Massma.Inner.scale(list, r'"price_multiplier": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True)  # multiplies or divides how much a price is multiplied by based on in game scenarios
    Massma.Inner.normal(list, r'"max_uses": -?\d*\.?\d+') # shuffles the amount of times you can trade for an item
    Massma.Inner.scale(list, r'"max_uses": -?\d*\.?\d+', (0.33,3), decimals=False, zeros=False, fair_range=True) # multiplies or divides the amount of times you can trade for an item
    Massma.Inner.normal(list, r'"gives": \[.*?\],"wants": \[.*?\],', flags=[re.M, re.S]) # shuffles what a village gives for each trade

Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED TRADING")
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
Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED LOOT")

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
Massma.Inner.scale(biomes_list, [r'"blue_spores": .*', r'"ash": .*', r'"red_spores": .*', r'"white_ash": .*'], (0.5,2.0), zeros=False, rounding=2, decimals=True, fair_range=True) # multiplies and divides the particles from nether biomes
Massma.Inner.group(biomes_list, [r'"downfall": -?\d*\.?\d+',r'',r'"snow_accumulation": \[.*?\]','"temperature": -?\d*\.?\d+'], flags=[re.M, re.S]) # shuffles the climate of all biomes
Massma.Inner.normal(biomes_list, r'"minecraft:overworld_height": \{.*?\}', flags=[re.M, re.S]) # shuffles the terrain type of each biome
Massma.Inner.normal(biomes_list, r'"minecraft:overworld_generation_rules": \{.*?\}', flags=[re.M, re.S]) # shuffles the terrain type of each biome
Massma.Inner.normal(biomes_list, r'"sea_floor_depth": -?\d*\.?\d+', duplicate=True) # shuffles how far biome seas reach in oceans and rivers
Massma.Inner.scale(biomes_list, r'"sea_floor_depth": -?\d*\.?\d+', (0.33,3), fair_range=True) # multiplies and devices how far biome seas reach in oceans and rivers
Massma.Inner.normal(biomes_list, r'"minecraft:mesa_surface": \{.*?\}', flags=[re.M, re.S]) # shuffles how each mesa biome generates
Massma.Inner.normal(biomes_list, [r'"bryce_pillars": true',r'"bryce_pillars": false'], duplicate=True) # shuffles if mesa biomes generate with giant pillars
Massma.Inner.normal(biomes_list, [r'"has_forest": true',r'"has_forest": false'], duplicate=True) # shuffles if mesa biomes generate with forests
Massma.Inner.group(biomes_list, [r'"noise_frequency_scale": -?\d*\.?\d+', r'"noise_range": \[ -?\d*\.?\d+, -?\d*\.?\d+ \]']) # shuffles sand will be normal or red
Massma.Inner.normal(biomes_list, [r'"north_slopes": true', r'"north_slopes": false', r'"east_slopes": true', r'"east_slopes": false', r'"south_slopes": true', r'"south_slopes": false', r'"west_slopes": true', r'"west_slopes": false'], duplicate=True) # shuffles which way slopes face
Massma.Inner.normal(biomes_list, [r'"top_slide": \{.*?\}'], flags=[re.M, re.S]) # shuffles if mountains have peaks

Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED BIOMES")

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

Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED RECIPIES")

# feature_rules
feature_rules_path = altered_base + "\\behavior_pack\\feature_rules"
feature_rules_list = Massma.Search.full(feature_rules_path)
distribution_filter = Massma.Filter.Ignore(Massma.Search.name(feature_rules_path, ["seagrass", "vines"], logic=Massma.Logic.OR)) # filters out files that break during distribution shuffle
place_filter = [] # filters and categorizes groups of place features
# no section exclusive shuffling and altering
Massma.Inner.normal(feature_rules_list, r'[x-z][x-z][x-z]', duplicate=True) #coordinate_eval_order, or the order in which operation will happen
Massma.Inner.normal(feature_rules_list, r'"distribution": ".*"', duplicate=True, ignores=distribution_filter)
Massma.Inner.normal(feature_rules_list, r'"iterations": -?\d*\.?\d+')
Massma.Inner.offset(feature_rules_list, r'"iterations": -?\d*\.?\d+',(-1, 1), zeros=False, decimals=False)  # allowing values of 1 to be effect by scale
Massma.Inner.scale(feature_rules_list, r'"iterations": -?\d*\.?\d+', (0.33,3), zeros=False, decimals=False, fair_range=True)
# extents with negatives
Massma.Inner.normal(feature_rules_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]')
Massma.Inner.offset(feature_rules_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]',(-1, 1),  zeros=True, decimals=False, minmaxing=True, minmax_matching=False)  # allowing values of 1 to be effect by scale
Massma.Inner.scale(feature_rules_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]', (0.33,3), zeros=True, decimals=False, minmaxing=True, fair_range=True, minmax_matching=False)
# extents without negatives
Massma.Inner.normal(feature_rules_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]')
Massma.Inner.offset(feature_rules_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]',(-1, 1),  zeros=True, decimals=False, minmaxing=True, minmax_matching=False)  # allowing values of 1 to be effect by scale
Massma.Inner.scale(feature_rules_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]', (0.33,3), zeros=True, decimals=False, minmaxing=True, fair_range=True, minmax_matching=False)
# FEATURE PASS

Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED FEATURE RULES")

# features
features_path = altered_base + "\\behavior_pack\\features"
features_list = Massma.Search.full(features_path)
cocoa_filters = [] # used for filtering out coco in distribution
identifier_filters = [] # used for filtering and organizing groups of features that can be shuffled together based on their identifiers
cocoa_filters.append([Massma.Filter.Exclude(features_list, r'cocoa', logic_strings=Massma.Logic.NAND)]) # if it has coco in the name
cocoa_filters.append([Massma.Filter.Exclude(features_list, r'cocoa', logic_strings=Massma.Logic.AND)]) # if it does not have cocoa in the name
identifier_filters.append([Massma.Filter.Exclude(features_list, r'"name": "minecraft:stone"', logic_strings=Massma.Logic.NAND)]) # shuffles features that spawn inside stone
identifier_filters.append([Massma.Filter.Exclude(features_list, r'"tags": "query.any_tag(.*?dirt.*?)"', logic_strings=Massma.Logic.NAND)]) # shuffles features that spawns omn dirt <<<WORK ON THIS>>>
# filter-based shuffling
for filter in identifier_filters:
    Massma.Inner.normal(features_list, r'"identifier": ".*"', excludes=filter) # shuffles the identifiers of features, changing where they are placed
# no section exclusive shuffling and altering
Massma.Inner.normal(features_list, r'"iterations": -?\d*\.?\d+')
Massma.Inner.offset(features_list, r'"iterations": -?\d*\.?\d+',(-1, 1), decimals=False, zeros=True)  # allowing values of 1 to be effect by scale
Massma.Inner.scale(features_list, r'"iterations": -?\d*\.?\d+', (0.33,3), zeros=True, decimals=False, fair_range=True)
Massma.Inner.normal(features_list, r'"count": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"count": -?\d*\.?\d+', (0.33,3), zeros=False, decimals=False)
Massma.Inner.normal(features_list, [r'"numerator": -?\d*\.?\d+,.*? "denominator": -?\d*\.?\d+'], flags=[re.M, re.S]) # FIX THIS FOR SOME REASOn
Massma.Inner.offset(features_list, [r'"numerator": -?\d*\.?\d+,.*? "denominator": -?\d*\.?\d+'], (-1, 1), flags=[re.M, re.S], zeros=False, decimals=False, minmaxing=True, minmax_matching=False)
Massma.Inner.scale(features_list, [r'"numerator": -?\d*\.?\d+,.*? "denominator": -?\d*\.?\d+'], (0.33,3), flags=[re.M, re.S], zeros=False, decimals=False, minmaxing=True, fair_range=True, minmax_matching=False)
Massma.Inner.normal(features_list, r'"range_min": -?\d*\.?\d+, "range_max": -?\d*\.?\d+', flags=[re.M, re.S])
Massma.Inner.offset(features_list, r'"range_min": -?\d*\.?\d+, "range_max": -?\d*\.?\d+', (-1, 1), flags=[re.M, re.S], zeros=False, decimals=False, minmaxing=True, clamps_outer=(3, 2147483647))
Massma.Inner.scale(features_list, r'"range_min": -?\d*\.?\d+, "range_max": -?\d*\.?\d+', (0.33,3), flags=[re.M, re.S], zeros=False, decimals=False, minmaxing=True, fair_range=True, clamps_outer=(3, 2147483647))
Massma.Inner.normal(features_list, r'"min": -?\d*\.?\d+, "max": -?\d*\.?\d+',  flags=[re.M, re.S])
Massma.Inner.scale(features_list, r'"min": -?\d*\.?\d+, "max": -?\d*\.?\d+', (0.33,3), flags=[re.M, re.S], zeros=False, decimals=False, minmaxing=True, fair_range=True)
Massma.Inner.normal(features_list, r'"min": \[ -?\d*\.?\d+, -?\d*\.?\d+, -?\d*\.?\d+\], "max": \[ -?\d*\.?\d+, -?\d*\.?\d+, -?\d*\.?\d+\]', flags=[re.M, re.S])
Massma.Inner.scale(features_list, r'"min": \[ -?\d*\.?\d+, -?\d*\.?\d+, -?\d*\.?\d+\], "max": \[ -?\d*\.?\d+, -?\d*\.?\d+, -?\d*\.?\d+\]', (0.33,3), flags=[re.M, re.S], zeros=True, decimals=False, minmaxing=True, fair_range=True)
Massma.Inner.normal(features_list, r'"search_range": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"min": -?\d*\.?\d+, "max": -?\d*\.?\d+', (0.33,3), zeros=False, decimals=False, fair_range=True)
Massma.Inner.normal(features_list, r'[x-z][x-z][x-z]', duplicate=True) #coordinate_eval_order, or the order in which operation will happen
Massma.Inner.normal(features_list, r'"distribution": ".*"', duplicate=True, excludes=cocoa_filters[1]) # does not affect coco
Massma.Inner.normal(features_list, r'"distribution": ".*"', duplicate=True, excludes=cocoa_filters[0], preset=['"distribution": "fixed_grid"', '"distribution": "jittered_grid"']) # does effect coco
# extents with negatives
Massma.Inner.normal(features_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]')
Massma.Inner.offset(features_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]',(-1, 1),  zeros=True, decimals=False, minmaxing=True)  # allowing values of 1 to be effect by scale
Massma.Inner.scale(features_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]', (0.33,3), zeros=True, decimals=False, minmaxing=True, fair_range=True)
# extents without negatives
Massma.Inner.normal(features_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]')
Massma.Inner.offset(features_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]',(-1, 1),  zeros=True, decimals=False, minmaxing=True)  # allowing values of 1 to be effect by scale
Massma.Inner.scale(features_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]', (0.33,3), zeros=True, decimals=False, minmaxing=True, fair_range=True)
Massma.Inner.normal(features_list, r'"canopy_height": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"canopy_height": -?\d*\.?\d+', (0.33,3), fair_range=True, clamps_outer=(3,2147483647)) # trees
Massma.Inner.normal(features_list, r'"canopy_radius": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"canopy_radius": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"leaf_placement_attempts": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"leaf_placement_attempts": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"one_branch": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"one_branch": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"two_branches": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"two_branches": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"two_branches_and_trunk": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"two_branches_and_trunk": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"height": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"height": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"radius": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"radius": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"wide_bottom_layer_hole_chance": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"wide_bottom_layer_hole_chance": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"corner_hole_chance": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"corner_hole_chance": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"hanging_leaves_chance": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"hanging_leaves_chance": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True) # trees
Massma.Inner.normal(features_list, r'"hanging_leaves_extension_chance": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"hanging_leaves_extension_chance": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"variance": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"variance": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"scale": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"scale": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True) # trees
Massma.Inner.normal(features_list, r'"density": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"density": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True) # trees
Massma.Inner.normal(features_list, r'"min_altitude_factor": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"min_altitude_factor": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True) # trees
Massma.Inner.normal(features_list, r'"width_scale": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"width_scale": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True) # trees
Massma.Inner.normal(features_list, r'"foliage_altitude_factor": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"foliage_altitude_factor": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True) # trees
Massma.Inner.normal(features_list, r'"min_width": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"min_width": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"rise": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"rise": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"run": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"run": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"decoration_chance": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"decoration_chance": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True, clamps_outer=(0,100)) # trees
Massma.Inner.normal(features_list, r'"core_width": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"core_width": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"base_radius": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"base_radius": -?\d*\.?\d+', (0.33,3), fair_range=True, zeros=False, clamps_outer=(1,2147483647)) # trees
Massma.Inner.normal(features_list, r'"base": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"base": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"radius_step_modifier": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"radius_step_modifier": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True) # trees
Massma.Inner.normal(features_list, r'"num_clusters": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"num_clusters": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"cluster_radius": -?\d*\.?\d+') # trees
Massma.Inner.scale(features_list, r'"cluster_radius": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, r'"intervals": \[ -?\d*\.?\d+ \]') # trees
Massma.Inner.scale(features_list, r'"intervals": \[ -?\d*\.?\d+ \]', (0.33,3), fair_range=True) # trees
Massma.Inner.normal(features_list, [r'"leaf_block": \{.*?\}', r'"leaf_block": ".*?"'], flags=[re.M, re.S]) # trees
Massma.Inner.normal(features_list, [r'"trunk_block": \{.*?\}', r'"trunk_block": ".*?"'], flags=[re.M, re.S]) # trees
Massma.Inner.normal(features_list, r'"min_outer_wall_distance": -?\d*\.?\d+') # amethysts
Massma.Inner.scale(features_list, r'"min_outer_wall_distance": -?\d*\.?\d+', (0.33,3), clamps_outer=(0,10), fair_range=True) # amethysts
Massma.Inner.normal(features_list, r'"max_outer_wall_distance": -?\d*\.?\d+') # amethysts
Massma.Inner.scale(features_list, r'"max_outer_wall_distance": -?\d*\.?\d+', (0.33,3), clamps_outer=(0,20), fair_range=True) # amethysts
Massma.Inner.normal(features_list, r'"min_distribution_points": -?\d*\.?\d+') # amethysts
Massma.Inner.scale(features_list, r'"min_distribution_points": -?\d*\.?\d+', (0.33,3), clamps_outer=(0,10), fair_range=True) # amethysts
Massma.Inner.normal(features_list, r'"max_distribution_points": -?\d*\.?\d+') # amethysts
Massma.Inner.scale(features_list, r'"max_distribution_points": -?\d*\.?\d+', (0.33,3), clamps_outer=(0,20), fair_range=True) # amethysts
Massma.Inner.normal(features_list, r'"min_point_offset": -?\d*\.?\d+') # amethysts
Massma.Inner.scale(features_list, r'"min_point_offset": -?\d*\.?\d+', (0.33,3), clamps_outer=(0,10), fair_range=True) # amethysts
Massma.Inner.normal(features_list, r'"max_point_offset": -?\d*\.?\d+') # amethysts
Massma.Inner.scale(features_list, r'"max_point_offset": -?\d*\.?\d+', (0.33,3), clamps_outer=(0,20), fair_range=True) # amethysts
Massma.Inner.normal(features_list, r'"max_radius": -?\d*\.?\d+') # amethysts
Massma.Inner.scale(features_list, r'"max_radius": -?\d*\.?\d+', (0.33,3), fair_range=True) # amethysts
Massma.Inner.normal(features_list, r'"crack_point_offset": -?\d*\.?\d+') # amethysts
Massma.Inner.scale(features_list, r'"crack_point_offset": -?\d*\.?\d+', (0.33,3), clamps_outer=(0,10), decimals=True, fair_range=True) # amethysts
Massma.Inner.normal(features_list, r'"generate_crack_chance": -?\d*\.?\d+') # amethysts
Massma.Inner.scale(features_list, r'"generate_crack_chance": -?\d*\.?\d+', (0.33,3), clamps_outer=(0,1), decimals=True, fair_range=True) # amethysts
Massma.Inner.normal(features_list, r'"base_crack_size": -?\d*\.?\d+') # amethysts
Massma.Inner.scale(features_list, r'"base_crack_size": -?\d*\.?\d+', (0.33,3), clamps_outer=(0,5), decimals=True, fair_range=True) # amethysts
Massma.Inner.normal(features_list, r'"noise_multiplier": -?\d*\.?\d+') # amethysts
Massma.Inner.scale(features_list, r'"noise_multiplier": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True) # amethysts
Massma.Inner.normal(features_list, r'"use_potential_placements_chance": -?\d*\.?\d+') # amethysts
Massma.Inner.scale(features_list, r'"use_potential_placements_chance": -?\d*\.?\d+', (0.33,3), clamps_outer=(0,1), decimals=True, fair_range=True) # amethysts
Massma.Inner.offset(features_list, r'\[ ".*_feature", -?\d*\.?\d+ \]', (-1, 1), decimals=False, zeros=False) # generation weight
Massma.Inner.scale(features_list, r'\[ ".*_feature", -?\d*\.?\d+ \]', (0.25,4), zeros=False, fair_range=True) # generation weight
Massma.Inner.normal(features_list, r'"vertical_search_range": -?\d*\.?\d+') # snapping
Massma.Inner.scale(features_list, r'"vertical_search_range": -?\d*\.?\d+', (0.33,3), zeros=False, fair_range=True) #snapping
Massma.Inner.normal(features_list, r'direction": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'direction": -?\d*\.?\d+', (0.33,3), fair_range=True)
Massma.Inner.normal(features_list, r'"vegetation_chance": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"vegetation_chance": -?\d*\.?\d+', (0.33,3), fair_range=True)
Massma.Inner.normal(features_list, r'"depth": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"depth": -?\d*\.?\d+', (0.33,3), fair_range=True)
Massma.Inner.normal(features_list, r'"vertical_range": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"vertical_range": -?\d*\.?\d+', (0.33,3), fair_range=True)
Massma.Inner.normal(features_list, r'"extra_deep_block_chance": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"extra_deep_block_chance": -?\d*\.?\d+', (0.33,3), fair_range=True)
Massma.Inner.normal(features_list, r'"extra_edge_column_chance": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"extra_edge_column_chance": -?\d*\.?\d+', (0.33,3), fair_range=True)
Massma.Inner.normal(features_list, r'"age": -?\d*\.?\d+') # cocoa
Massma.Inner.normal(features_list, r'"max_empty_corners": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"max_empty_corners": -?\d*\.?\d+', (0.33,3), fair_range=True)
Massma.Inner.normal(features_list, r'"discard_chance_on_air_exposure": -?\d*\.?\d+') # ores
Massma.Inner.scale(features_list, r'"discard_chance_on_air_exposure": -?\d*\.?\d+', (0.33,3), decimals=True, rounding=1, fair_range=True, clamps_outer=(0,1)) # ores
Massma.Inner.normal(features_list, r'"chance_of_spreading": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"chance_of_spreading": -?\d*\.?\d+', (0.33,3), decimals=True, rounding=1, fair_range=True, clamps_outer=(0,1))
Massma.Inner.normal(features_list, r'"search_range": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"search_range": -?\d*\.?\d+', (0.33,3), fair_range=True)
Massma.Inner.normal(features_list, r'"height_rand_a": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"height_rand_a": -?\d*\.?\d+', (0.33,3), fair_range=True, clamps_outer=(1, 214783647))
Massma.Inner.normal(features_list, r'"height_rand_b": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"height_rand_b": -?\d*\.?\d+', (0.33,3), fair_range=True)
Massma.Inner.normal(features_list, [r'"hanging": true',r'"hanging": false'])
Massma.Inner.normal(features_list, r'"branch_length": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"branch_length": -?\d*\.?\d+', (0.33,3), fair_range=True)
Massma.Inner.normal(features_list, r'"branch_slope": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"branch_slope": -?\d*\.?\d+', (0.33,3), fair_range=True)
Massma.Inner.normal(features_list, [r'"simplify_canopy": true', r'"simplify_canopy": false'])
Massma.Inner.normal(features_list, r'"fill_with": ".*"') # caves
Massma.Inner.normal(features_list, r'"width_modifier": -?\d*\.?\d+') # caves
Massma.Inner.scale(features_list, r'"width_modifier": -?\d*\.?\d+', (0.33,3), zeros=True, decimals=True, rounding=1, fair_range=True) # caves
Massma.Inner.normal(features_list, r'"skip_carve_chance": -?\d*\.?\d+') # caves
Massma.Inner.scale(features_list, r'"skip_carve_chance": -?\d*\.?\d+', (0.33,3), fair_range=True) # caves
Massma.Inner.normal(features_list, r'"y_scale": \[ .*? \]') # caves
Massma.Inner.scale(features_list, r'"y_scale": \[ .*? \]', (0.33,3), decimals=True, rounding=1, fair_range=True) # caves
Massma.Inner.normal(features_list, r'"height_limit": -?\d*\.?\d+') # caves
Massma.Inner.scale(features_list, r'"height_limit": -?\d*\.?\d+', (0.33,3), fair_range=True) # caves
Massma.Inner.normal(features_list, r'"horizontal_radius_multiplier": \[ .*? \]') # caves
Massma.Inner.scale(features_list, r'"horizontal_radius_multiplier": \[ .*? \]', (0.33,3), decimals=True, rounding=1, fair_range=True) # caves
Massma.Inner.normal(features_list, r'"vertical_radius_multiplier": \[ .*? \]') # caves
Massma.Inner.scale(features_list, r'"vertical_radius_multiplier": \[ .*? \]', (0.33,3), decimals=True, rounding=1, fair_range=True) # caves
Massma.Inner.normal(features_list, r'"floor_level": \[ .*? \]') # caves
Massma.Inner.scale(features_list, r'"floor_level": \[ .*? \]', (0.33,3), decimals=True, rounding=1, fair_range=True) # caves
Massma.Inner.normal(features_list, r'"branch_position": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"branch_position": -?\d*\.?\d+', (0.33,3), fair_range=True)
Massma.Inner.normal(features_list, r'"outer_radius": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"outer_radius": -?\d*\.?\d+', (0.33,3), fair_range=True)
Massma.Inner.normal(features_list, r'"inner_radius": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"inner_radius": -?\d*\.?\d+', (0.33,3), fair_range=True)
Massma.Inner.normal(features_list, r'"moisturized_amount": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"moisturized_amount": -?\d*\.?\d+', (0.33,3), fair_range=True)
Massma.Inner.normal(features_list, r'"minimum_distance_below_surface": -?\d*\.?\d+')
Massma.Inner.scale(features_list, r'"minimum_distance_below_surface": -?\d*\.?\d+', (0.33,3), fair_range=True)


Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED FEATURES")

# items
items_path = altered_base + "\\behavior_pack\\items"
items_list = Massma.Search.full(items_path)
items_filters = [] # used for filtering items into sections
items_filters.append(Massma.Filter.Exclude(items_list,r'"minecraft:food":', logic_strings=Massma.Logic.NAND)) # only shuffles foods
items_filters.append(Massma.Filter.Exclude(items_list,r'"identifier": ".*?bundle"', logic_strings=Massma.Logic.NAND)) # only shuffles bundles
items_filters.append(Massma.Filter.Exclude(items_list,r'"minecraft:seed":', logic_strings=Massma.Logic.NAND)) # only shuffles seeds


Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED ITEMS")

# item catalogs
item_catalogs_path = altered_base + "\\behavior_pack\\item_catalog"
item_catalogs_list = []

Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED SPAWN ITEM CATALOGS")

# aim assists
aim_assists_path = altered_base + "\\behavior_pack\\aim_assist"
aim_assists_list = []

Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED AIM ASSISTS")

# behavior trees
behavior_trees_path = altered_base + "\\behavior_pack\\behavior_trees"
behavior_trees_list = []

Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED BEHAVIOR TREES")

# structures
structures_path = altered_base + "\\behavior_pack\\structures"
structures_list = []

Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED STRUCTURES")

# worldgens
worldgens_path = altered_base + "\\behavior_pack\\worldgens"
worldgens_list = []

Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED WORLDGEN")

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
Not all source things in outputs align correct to text, some are smaller than the gap is giving
ERROR WITH LOGGING DATA, LOOK AT LATER (LOGGINE UNIQUE CHARACTERS)
add inner shuffling more similar to otter group, allowing users to shuffling everything of the same data together, in groups
allow for full path searches, instead of only name searches
simple way to directly edit data inside files
in filters make it so when comparing file with files, it is the absolute paths of both files
stop access filters inside method you should not, like accessing swap inside Inner
get sets for filters
HARD: a way to inject shuffled data, allowing you to shuffle data info files that didnt even have that data in the first place
allowing some kind of filter made for altering and controlling numbers
INNER GROUP NOT WORKING, SIMPLY DUMPING DATA
add set method to display the normal results form display
"""