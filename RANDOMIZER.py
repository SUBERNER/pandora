import Massma
from Massma import random # used for allowing randoms that are outside Massma's methods to still use the same seed
import os
import math
import re

from Massma.Filter import Ignore
from Massma.Inner import scale

#EDIT THIS TO CHANGE WHAT AND HOW DATA IS SHUFFLED
Massma.Methods.seed(5348945732)
shuffle_entities = False
shuffle_spawn_rules = True
shuffle_spawn_groups = False  # WORK ON
shuffle_trading = True
shuffle_loot = True
shuffle_biomes = True
shuffle_recipies = False
shuffle_feature_rules = True
shuffle_features = True
shuffle_items = True
shuffle_item_catalogs = False  # WORK ON
shuffle_aim_assists = False  # WORK ON
shuffle_behavior_trees = False  # WORK ON
shuffle_structures = False  # WORK ON
shuffle_worldgens = False  # WORK ON
shuffle_gamerules = False
shuffle_animation_controllers = False  # WORK ON
shuffle_animations = False  # WORK ON
shuffle_atmospherics = False  # WORK ON
shuffle_attachables = False  # WORK ON
shuffle_biomes_resource = False  # WORK ON
shuffle_cameras = False  # WORK ON
shuffle_color_gradings = False  # WORK ON
shuffle_entities_resource = False  # WORK ON
shuffle_fogs = False  # WORK ON
shuffle_fonts = False  # WORK ON
shuffle_lightings = False  # WORK ON
shuffle_materials = False  # WORK ON
shuffle_models = False  # WORK ON
shuffle_particles = False  # WORK ON
shuffle_pdrs = False  # WORK ON
shuffle_render_controllers = False  # WORK ON
shuffle_shadows = False
shuffle_sounds = False  # WORK ON
shuffle_texts = False  # WORK ON
shuffle_textures = False  # WORK ON
shuffle_uis = False  # WORK ON
shuffle_waters = False  # WORK ON



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
if shuffle_entities:
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
if shuffle_spawn_rules:
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
if shuffle_spawn_groups:
    spawn_groups_path = altered_base + "\\behavior_pack\\spawn_groups"
    spawn_groups_list = Massma.Search.full(spawn_groups_path)
    # no section exclusive shuffling and altering
    Massma.Inner.normal(spawn_groups_list, r'"identifier": ".*"')
    Massma.Inner.normal(spawn_groups_list, r'"entity_type": ".*"')
    Massma.Inner.normal(spawn_groups_list, r'"minecraft:herd": {.*?},')
    Massma.Inner.scale(spawn_groups_list, [r'"minecraft:herd": {.*?},'], (0.33,3), zeros=False, decimals=False, minmaxing=True, fair_range=True) # multiplies or divides the min and max values of data

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED SPAWN GROUPS")

# trading
if shuffle_trading:
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
        Massma.Inner.scale(list, r'"base_cost": -?\d*\.?\d+', (0.33, 3), decimals=False, minmaxing=True, zeros=False, fair_range=True)  # multiplies or divides librarian villager's base cost for books
        Massma.Inner.scale(list, r'"base_random_cost": -?\d*\.?\d+', (0.33, 3), decimals=False, zeros=False, fair_range=True)  # multiplies or divides librarian villager's base cost for books randomly added or subtracted
        Massma.Inner.scale(list, r'"per_level_random_cost": -?\d*\.?\d+', (0.33, 3), decimals=False, zeros=False, fair_range=True)  # multiplies or divides librarian villager's cost based on per level added, randomly adding or subtracting
        Massma.Inner.scale(list, r'"per_level_cost": -?\d*\.?\d+', (0.33, 3), decimals=False, zeros=False, fair_range=True)  # multiplies or divides librarian villager's cost based on per level added
        Massma.Inner.scale(list, r'"trader_exp":  -?\d*\.?\d+',(0.33, 3), decimals=False, zeros=False, fair_range=True) # shuffles how much xp a user gets for trading
        #Massma.Inner.normal(list, r'"gives": \[.*?\],.*?"', flags=[re.M, re.S]) # shuffles what a village gives for each trade
        Massma.Inner.normal(list, r'"wants": \[.*?\],.*?"', flags=[re.M, re.S])  # shuffles what a village wants for each trade

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED TRADING")

# loot
if shuffle_loot:
    loot_list = [] # the list of each section of loot_tables
    loot_path = altered_base + "\\behavior_pack\\loot_tables"
    # sets up the groups for each section of loot tables to be shuffled
    loot_list.append(Massma.Search.full(loot_path + "\\chests", deep_search=True, ignores=Massma.Filter.Ignore(Massma.Search.name(loot_path + "\\chests",["reward.json","dispenser", "village_blacksmith", "village_two_room_house"], deep_search=True, logic=Massma.Logic.OR)))) # chests, except dispenser, old village houses, and rewards
    loot_list[-1] + Massma.Search.full(loot_path + "\\pots", deep_search=True)  # gets pots for chests
    loot_list.append(Massma.Search.full(loot_path + "\\dispensers", deep_search=True))  # dispensers
    loot_list[-1] + Massma.Search.name(loot_path + "\\chests", contains="dispenser", deep_search=True)  # gets dispensers from chests
    loot_list[-1] + Massma.Search.name(loot_path + "\\spawners", contains="items_to_drop", deep_search=True)  # gets item_drops from spawners

    loot_list.append(Massma.Search.full(loot_path + "\\equipment", ignores=Massma.Filter.Ignore(Massma.Search.name(loot_path + "\\equipment","low_tier_items.json"))))  # equipment equipment
    loot_list[-1] + Massma.Search.name(loot_path + "\\entities", "set")  # gets armor sets from entites
    loot_list.append(Massma.Search.name(loot_path + "\\entities", ["equipment", "gear"], logic=Massma.Logic.OR))  # entity equipment
    loot_list.append(Massma.Search.name(loot_path + "\\entities", "brush"))  # brushing
    loot_list.append(Massma.Search.name(loot_path, ["cat_gift.json","piglin_barter.json","sniffer_seeds.json","panda_sneeze.json"], deep_search=True, logic=Massma.Logic.OR))  # interactions
    loot_list.append(Massma.Search.full(loot_path + "\\entities", ignores=Massma.Filter.Ignore(loot_list[-1] + loot_list[-2] + loot_list[-3] + loot_list[-4]))) # everything not used yet in entities' loot list
    loot_list.append(Massma.Search.full(loot_path + "\\gameplay")) # fish
    loot_list[-1] + Massma.Search.full(loot_path + "\\gameplay\\fishing") # fishing
    loot_list.append(Massma.Search.name(loot_path + "\\gameplay\\entities", "mooshroom_milking")) # mushroom
    loot_list.append(Massma.Search.full(loot_path + "\\spawners", deep_search=True, ignores=Massma.Filter.Ignore(Massma.Search.name(loot_path + "\\spawners", contains="items_to_drop", deep_search=True)))) # spawners
    # goes through each list and shuffles within
    print(loot_list)
    for list in loot_list:
        Massma.Inner.normal(list, r'.+', flags=[re.S]) # shuffles ALL the data inside a loot_table between groups of loot_tables
        Massma.Inner.offset(list, [r'"rolls": -?\d*\.?\d+', r'"rolls": \{.*?\}'], (-1, 1), zeros=False, flags=[re.M, re.S])  # adds and subtract the attempts to select items
        Massma.Inner.scale(list, [r'"rolls": -?\d*\.?\d+', r'"rolls": \{.*?\}'], (0.33, 3), fair_range=True, zeros=False, flags=[re.M, re.S])  # multiples and divides the attempts to select items
        Massma.Inner.normal(list, [r'"rolls": -?\d*\.?\d+', r'"rolls": \{.*?\}'], duplicate=True, flatten=True, flags=[re.M, re.S])  # shuffles the attempts to select items
        Massma.Inner.offset(list, r'"weight": -?\d*\.?\d+', (-1, 1), zeros=False)  # adds and subtracts the chance of an item spawning
        Massma.Inner.scale(list, r'"weight": -?\d*\.?\d+', (0.33, 3), fair_range=True, zeros=False)  # multiples and divides the chance of an item spawning
        Massma.Inner.normal(list, r'"weight": -?\d*\.?\d+', duplicate=True, flatten=True)  # shuffles the chance of an item spawning
        Massma.Inner.offset(list, r'"count": \{.*?\}', (-1, 1), zeros=False, flags=[re.M, re.S])  # adds and subtract the number of items spawn
        Massma.Inner.scale(list, r'""count": \{.*?\}', (0.33, 3), fair_range=True, zeros=False, flags=[re.M, re.S])  # multiples and divides the number of items spawn
        Massma.Inner.normal(list, r'"count": \{.*?\}', duplicate=True, flatten=True, flags=[re.M, re.S])  # shuffles the number of items spawn
        Massma.Inner.scale(list, r'chance": -?\d*\.?\d+', (0.33, 3), fair_range=True, zeros=False, clamps_outer=(0,1))  # multiples and divides the chance of item spawning
        Massma.Inner.normal(list, r'chance": -?\d*\.?\d+', duplicate=True, flatten=True)  # shuffles the chance of item spawning
        Massma.Inner.normal(list, r'"type": "loot_table",.*?"name": ".*"', flags=[re.M, re.S])  # shuffles loot tables tied to other loot tables
        Massma.Inner.normal(list, r'"tiers": \{.*?\}', flags=[re.M, re.S])  # shuffles
        Massma.Inner.offset(list, r'"initial_range": -?\d*\.?\d+', (-1, 1), zeros=False)  # adds and subtracts
        Massma.Inner.scale(list, r'"initial_range": -?\d*\.?\d+', (0.33, 3), fair_range=True, zeros=False)  # multiples and divides
        Massma.Inner.normal(list, r'"initial_range": -?\d*\.?\d+', duplicate=True, flatten=True)  # shuffles
        Massma.Inner.offset(list, r'"bonus_rolls": -?\d*\.?\d+', (-1, 1), zeros=False)  # adds and subtracts
        Massma.Inner.scale(list, r'"bonus_rolls": -?\d*\.?\d+', (0.33, 3), fair_range=True, zeros=False)  # multiples and divides
        Massma.Inner.normal(list, r'"bonus_rolls": -?\d*\.?\d+', duplicate=True, flatten=True)  # shuffles
        Massma.Inner.scale(list, r'"bonus_chance": -?\d*\.?\d+', (0.33, 3), fair_range=True, zeros=False, clamps_outer=(0,1))  # multiples and divides
        Massma.Inner.normal(list, r'"bonus_chance": -?\d*\.?\d+', duplicate=True, flatten=True)  # shuffles

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED LOOT")

# biomes
if shuffle_biomes:
    biomes_path = altered_base + "\\behavior_pack\\biomes"
    deprecated_ignores = Massma.Filter.Ignore(Massma.Search.content(biomes_path, "deprecated"))  # ignores deprecated and not used biomes
    biomes_list = Massma.Search.full(biomes_path, ignores=deprecated_ignores)
    biome_filters = [] # stores all biome filters
    # filters (its excluded if it does not contain the text in "")
    biome_filters.append([Massma.Filter.Exclude(biomes_list,r'"nether"', logic_strings=Massma.Logic.NAND)])
    biome_filters.append([Massma.Filter.Exclude(biomes_list, r'"caves"', logic_strings=Massma.Logic.NAND)])
    biome_filters.append([Massma.Filter.Exclude(biomes_list, r'"the_end"', logic_strings=Massma.Logic.NAND)])
    biome_filters.append([Massma.Filter.Exclude(biomes_list, [r'"overworld"',r'"caves'], logic_strings=Massma.Logic.NOR)])
    # shuffling based on filters
    for filter in biome_filters:
        #Massma.Inner.normal(biomes_list, r'"identifier": ".*"', excludes=filter) # shuffles how biomes are identified in the system
        Massma.Inner.normal(biomes_list, r'"sea_floor_material": ".*"', excludes=filter, duplicate=True, flatten=True) # shuffles the block used for the sea floor of a biome
        Massma.Inner.normal(biomes_list, r'"minecraft:multinoise_generation_rules": \{.*?\}', flags=[re.M, re.S], excludes=filter, duplicate=True, flatten=True) # shuffles how and where nether biomes are created
        #Massma.Inner.normal(biomes_list, r'"weight": -?\d*\.?\d+', excludes=filter) # shuffles the likelihood a biome is created
    # no section exclusive shuffling and altering
    Massma.Inner.normal(biomes_list, r'"sea_material": ".*"', duplicate=True, preset=['"sea_material": "minecraft:water"','"sea_material": "minecraft:water"','"sea_material": "minecraft:water"','"sea_material": "minecraft:water"','"sea_material": "minecraft:water"','"sea_material": "minecraft:water"','"sea_material": "minecraft:water"','"sea_material": "minecraft:water"','"sea_material": "minecraft:water"','"sea_material": "minecraft:lava"']) # changes the liquids to either water or lava
    Massma.Inner.normal(biomes_list, [r'"blue_spores": .*', r'"ash": .*', r'"red_spores": .*', r'"white_ash": .*'], duplicate=True, flatten=True) # shuffles the particles from nether biomes
    Massma.Inner.scale(biomes_list, [r'"blue_spores": .*', r'"ash": .*', r'"red_spores": .*', r'"white_ash": .*'], (0.5,2.0), zeros=False, rounding=2, decimals=True, fair_range=True) # multiplies and divides the particles from nether biomes
    Massma.Inner.group(biomes_list, [r'"downfall": -?\d*\.?\d+',r'',r'"snow_accumulation": \[.*?\]','"temperature": -?\d*\.?\d+'], flags=[re.M, re.S], duplicate=True, flatten=True) # shuffles the climate of all biomes
    Massma.Inner.normal(biomes_list, r'"minecraft:overworld_height": \{.*?\}', flags=[re.M, re.S], duplicate=True, flatten=True) # shuffles the terrain type of each biome
    Massma.Inner.normal(biomes_list, r'"minecraft:overworld_generation_rules": \{.*?\}', flags=[re.M, re.S], duplicate=True, flatten=True) # shuffles the terrain type of each biome
    Massma.Inner.scale(biomes_list, r'"sea_floor_depth": -?\d*\.?\d+', (0.33,3), fair_range=True) # multiplies and devices how far biome seas reach in oceans and rivers
    Massma.Inner.normal(biomes_list, r'"sea_floor_depth": -?\d*\.?\d+', duplicate=True, flatten=True) # shuffles how far biome seas reach in oceans and rivers
    Massma.Inner.normal(biomes_list, r'"minecraft:mesa_surface": \{.*?\}', flags=[re.M, re.S], duplicate=True, flatten=True) # shuffles how each mesa biome generates
    Massma.Inner.normal(biomes_list, [r'"bryce_pillars": true',r'"bryce_pillars": false'], duplicate=True, flatten=True) # shuffles if mesa biomes generate with giant pillars
    Massma.Inner.normal(biomes_list, [r'"has_forest": true',r'"has_forest": false'], duplicate=True, flatten=True) # shuffles if mesa biomes generate with forests
    Massma.Inner.scale(biomes_list, r'"noise_frequency_scale": -?\d*\.?\d+', (0.33, 3), zeros=False, decimals=True, rounding=1)
    Massma.Inner.scale(biomes_list, r'"noise_range": \[ -?\d*\.?\d+, -?\d*\.?\d+ \]', (0.33, 3), zeros=False, decimals=True, minmaxing=True, rounding=1, minmax_matching=False)
    Massma.Inner.group(biomes_list, [r'"noise_frequency_scale": -?\d*\.?\d+', r'"noise_range": \[ -?\d*\.?\d+, -?\d*\.?\d+ \]'], duplicate=True, flatten=True)
    Massma.Inner.scale(biomes_list, r'"noise_params": \[ .*? \]', (0.33,3), decimals=True, zeros=True, rounding=3, fair_range=True) # multiplies or divides how biomes scale the terrain
    Massma.Inner.normal(biomes_list, r'"noise_params": \[ .*? \]', duplicate=True, flatten=True) # shuffles how biomes scale the terrain
    Massma.Inner.normal(biomes_list, [r'"north_slopes": true', r'"north_slopes": false', r'"east_slopes": true', r'"east_slopes": false', r'"south_slopes": true', r'"south_slopes": false', r'"west_slopes": true', r'"west_slopes": false'], duplicate=True, preset=[r'"north_slopes": true', r'"north_slopes": false', r'"east_slopes": true', r'"east_slopes": false', r'"south_slopes": true', r'"south_slopes": false', r'"west_slopes": true', r'"west_slopes": false']) # shuffles which way slopes face
    Massma.Inner.normal(biomes_list, [r'"top_slide": \{.*?\}'], flags=[re.M, re.S], duplicate=True, preset=[r'"top_slide": {"enabled": false}',r'"top_slide": {"enabled": true}']) # shuffles if mountains have peaks

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED BIOMES")

# recipes
if shuffle_recipies:
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
if shuffle_feature_rules:
    feature_rules_path = altered_base + "\\behavior_pack\\feature_rules"
    deprecated_ignores = Massma.Filter.Ignore(Massma.Search.content(feature_rules_path, "deprecated"))  # ignores deprecated and not used feature_rules
    feature_rules_list = Massma.Search.full(feature_rules_path, ignores=deprecated_ignores)
    distribution_filter = Massma.Filter.Ignore(Massma.Search.name(feature_rules_path, ["seagrass", "vines"], logic=Massma.Logic.OR)) # filters out files that break during distribution shuffle
    place_filter = [] # filters and categorizes groups of place features
    # no section exclusive shuffling and altering
    Massma.Inner.normal(feature_rules_list, r'[x-z][x-z][x-z]', duplicate=True) #coordinate_eval_order, or the order in which operation will happen
    Massma.Inner.normal(feature_rules_list, r'"distribution": ".*"', duplicate=True, ignores=distribution_filter)
    Massma.Inner.offset(feature_rules_list, r'"iterations": -?\d*\.?\d+',(-1, 1), zeros=False, decimals=False)  # allowing values of 1 to be effect by scale (NO ZEROS COULD CAUSE PROBLEMS AS SOME DO HAVE ZEROS)
    Massma.Inner.scale(feature_rules_list, r'"iterations": -?\d*\.?\d+', (0.33,3), zeros=False, decimals=False, fair_range=True)
    Massma.Inner.normal(feature_rules_list, r'"iterations": -?\d*\.?\d+')
    # extents used underground
    underground_ignore = Massma.Filter.Ignore(Massma.Search.name(feature_rules_path,r'underground', ignores=deprecated_ignores, logic=Massma.Logic.NAND)) # filters out underground do to all spawning to close together or not at all, first only allows underground, then does not allow
    Massma.Inner.offset(feature_rules_list, r'"extent": \[ -?\d*\.?\d+, -?\d*\.?\d+ \]',(-1, 1), zeros=True, decimals=False, minmaxing=True, ignores=underground_ignore)  # allowing values of 1 to be effect by scale
    Massma.Inner.scale(feature_rules_list, r'"extent": \[ -?\d*\.?\d+, -?\d*\.?\d+ \]', (0.33,3), zeros=True, decimals=False, minmaxing=True, fair_range=True, ignores=underground_ignore)
    Massma.Inner.normal(feature_rules_list, r'"extent": \[ -?\d*\.?\d+, -?\d*\.?\d+ \]', ignores=underground_ignore)
    underground_ignore = Massma.Filter.Ignore(Massma.Search.name(feature_rules_path,r'underground', ignores=deprecated_ignores, logic=Massma.Logic.AND)) # now will filter out all underground features
    # extents without negatives
    Massma.Inner.offset(feature_rules_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]',(-1, 1), zeros=True, decimals=False, minmaxing=True, clamps_outer=(-1,2147483647), ignores=underground_ignore)  # allowing values of 1 to be effect by scale
    Massma.Inner.scale(feature_rules_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]', (0.33,3), zeros=True, decimals=False, minmaxing=True, fair_range=True, clamps_outer=(-1,2147483647), ignores=underground_ignore)
    Massma.Inner.normal(feature_rules_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]', ignores=underground_ignore)
    # extents with negatives
    Massma.Inner.offset(feature_rules_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]',(-1, 1), zeros=True, decimals=False, minmaxing=True, ignores=underground_ignore)  # allowing values of 1 to be effect by scale
    Massma.Inner.scale(feature_rules_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]', (0.33,3), zeros=True, decimals=False, minmaxing=True, fair_range=True, ignores=underground_ignore)
    Massma.Inner.normal(feature_rules_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]', ignores=underground_ignore)
    # FEATURE PASS

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED FEATURE RULES")

# features
if shuffle_features:
    features_path = altered_base + "\\behavior_pack\\features"
    deprecated_ignores = Massma.Filter.Ignore(Massma.Search.content(features_path, "deprecated"))  # ignores deprecated and not used features
    features_list = Massma.Search.full(features_path, ignores=deprecated_ignores)
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
    Massma.Inner.offset(features_list, r'"iterations": -?\d*\.?\d+',(-1, 1), decimals=False, zeros=False)  # allowing values of 1 to be effect by scale
    Massma.Inner.scale(features_list, r'"iterations": -?\d*\.?\d+', (0.33,3), zeros=False, decimals=False, fair_range=True, clamps_outer=(0,2147483647))
    Massma.Inner.normal(features_list, r'"iterations": -?\d*\.?\d+')
    Massma.Inner.scale(features_list, r'"count": -?\d*\.?\d+', (0.33,3), zeros=False, decimals=False)
    Massma.Inner.normal(features_list, r'"count": -?\d*\.?\d+')
    Massma.Inner.offset(features_list, [r'"numerator": -?\d*\.?\d+,.*? "denominator": -?\d*\.?\d+'], (-1, 1), flags=[re.M, re.S], zeros=False, decimals=False, minmaxing=True, minmax_matching=False)
    Massma.Inner.scale(features_list, [r'"numerator": -?\d*\.?\d+,.*? "denominator": -?\d*\.?\d+'], (0.33,3), flags=[re.M, re.S], zeros=False, decimals=False, minmaxing=True, fair_range=True, minmax_matching=False)
    Massma.Inner.normal(features_list, [r'"numerator": -?\d*\.?\d+,.*? "denominator": -?\d*\.?\d+'], flags=[re.M, re.S]) # FIX THIS FOR SOME REASON
    Massma.Inner.offset(features_list, r'"range_min": -?\d*\.?\d+, "range_max": -?\d*\.?\d+', (-1, 1), flags=[re.M, re.S], decimals=False, minmaxing=True)
    Massma.Inner.scale(features_list, r'"range_min": -?\d*\.?\d+, "range_max": -?\d*\.?\d+', (0.33,3), flags=[re.M, re.S], decimals=False, minmaxing=True, fair_range=True, clamps_outer=(3, 2147483647))
    Massma.Inner.normal(features_list, r'"range_min": -?\d*\.?\d+, "range_max": -?\d*\.?\d+', flags=[re.M, re.S])
    Massma.Inner.normal(features_list, r'"min": \[ -?\d*\.?\d+, -?\d*\.?\d+, -?\d*\.?\d+\], "max": \[ -?\d*\.?\d+, -?\d*\.?\d+, -?\d*\.?\d+\]', flags=[re.M, re.S])
    Massma.Inner.scale(features_list, r'"min": \[ -?\d*\.?\d+, -?\d*\.?\d+, -?\d*\.?\d+\], "max": \[ -?\d*\.?\d+, -?\d*\.?\d+, -?\d*\.?\d+\]', (0.33,3), flags=[re.M, re.S], zeros=True, decimals=False, minmaxing=True, fair_range=True)
    Massma.Inner.scale(features_list, r'"min": -?\d*\.?\d+, "max": -?\d*\.?\d+', (0.33,3), zeros=False, decimals=False, minmaxing=True, fair_range=True,flags=[re.M, re.S])
    Massma.Inner.normal(features_list, r'"min": -?\d*\.?\d+, "max": -?\d*\.?\d+',  flags=[re.M, re.S])
    Massma.Inner.normal(features_list, r'"search_range": -?\d*\.?\d+')
    Massma.Inner.scale(features_list, r'"search_range": -?\d*\.?\d+', (0.33,3), zeros=True, decimals=False, fair_range=True, clamps_outer=(1,64))
    Massma.Inner.normal(features_list, r'[x-z][x-z][x-z]', duplicate=True) #coordinate_eval_order, or the order in which operation will happen
    Massma.Inner.normal(features_list, r'"distribution": ".*"', duplicate=True, excludes=cocoa_filters[1]) # does not affect coco
    Massma.Inner.normal(features_list, r'"distribution": ".*"', duplicate=True, excludes=cocoa_filters[0], preset=['"distribution": "fixed_grid"', '"distribution": "jittered_grid"']) # does effect coco
    # extents used underground #SOMETHING WRONG
    underground_ignore = Massma.Filter.Ignore(Massma.Search.name(features_path,r'underground', ignores=deprecated_ignores, logic=Massma.Logic.NAND)) # filters out underground do to all spawning to close together or not at all, first only allows underground, then does not allow
    Massma.Inner.offset(features_list, r'"extent": \[ -?\d*\.?\d+, -?\d*\.?\d+ \]',(-1, 1), zeros=True, decimals=False, minmaxing=True, ignores=underground_ignore)  # allowing values of 1 to be effect by scale
    Massma.Inner.scale(features_list, r'"extent": \[ -?\d*\.?\d+, -?\d*\.?\d+ \]', (0.33,3), zeros=True, decimals=False, minmaxing=True, fair_range=True, ignores=underground_ignore)
    Massma.Inner.normal(features_list, r'"extent": \[ -?\d*\.?\d+, -?\d*\.?\d+ \]', ignores=underground_ignore)
    underground_ignore = Massma.Filter.Ignore(Massma.Search.name(features_path,r'underground', ignores=deprecated_ignores, logic=Massma.Logic.AND)) # now will filter out all underground features
    # extents without negatives #SOMETHING WRONG
    Massma.Inner.offset(features_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]',(-1, 1), zeros=True, decimals=False, minmaxing=True, clamps_outer=(-1,2147483647), ignores=underground_ignore)  # allowing values of 1 to be effect by scale
    Massma.Inner.scale(features_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]', (0.33,3), zeros=True, decimals=False, minmaxing=True, fair_range=True, clamps_outer=(-1,2147483647), ignores=underground_ignore)
    Massma.Inner.normal(features_list, r'"extent": \[ \d*\.?\d+, -?\d*\.?\d+ \]', ignores=underground_ignore)
    # extents with negatives #SOMETHING WRONG
    Massma.Inner.offset(features_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]',(-1, 1), zeros=True, decimals=False, minmaxing=True, ignores=underground_ignore)  # allowing values of 1 to be effect by scale
    Massma.Inner.scale(features_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]', (0.33,3), zeros=True, decimals=False, minmaxing=True, fair_range=True, ignores=underground_ignore)
    Massma.Inner.normal(features_list, r'"extent": \[ -\d*\.?\d+, -?\d*\.?\d+ \]', ignores=underground_ignore)
    Massma.Inner.normal(features_list, r'"trunk_width": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"trunk_width" -?\d*\.?\d+', (-1, 1), zeros=False) # trees
    Massma.Inner.scale(features_list, r'"trunk_width" -?\d*\.?\d+', (0.33,3), fair_range=True, zeros=False) # trees
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
    Massma.Inner.scale(features_list, r'"height": -?\d*\.?\d+', (0.33,3), fair_range=True, clamps_outer=(4, 2147483647)) # trees
    Massma.Inner.normal(features_list, r'"radius": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"radius": -?\d*\.?\d+', (0.33,3), fair_range=True, clamps_outer=(3, 2147483647)) # trees
    Massma.Inner.normal(features_list, r'"wide_bottom_layer_hole_chance": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"wide_bottom_layer_hole_chance": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
    Massma.Inner.normal(features_list, r'"corner_hole_chance": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"corner_hole_chance": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
    Massma.Inner.normal(features_list, r'"hanging_leaves_chance": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"hanging_leaves_chance": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True, rounding=4) # trees
    Massma.Inner.normal(features_list, r'"hanging_leaves_extension_chance": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"hanging_leaves_extension_chance": -?\d*\.?\d+', (0.33,3), fair_range=True, decimals=True) # trees
    Massma.Inner.normal(features_list, r'"variance": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"variance": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
    Massma.Inner.normal(features_list, r'"scale": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"scale": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True,rounding=3) # trees
    Massma.Inner.normal(features_list, r'"density": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"density": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True) # trees
    Massma.Inner.normal(features_list, r'"min_altitude_factor": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"min_altitude_factor": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True, rounding=1) # trees
    Massma.Inner.normal(features_list, r'"width_scale": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"width_scale": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True,rounding=1) # trees
    Massma.Inner.normal(features_list, r'"foliage_altitude_factor": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"foliage_altitude_factor": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True,rounding=1) # trees
    Massma.Inner.normal(features_list, r'"min_width": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"min_width": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
    Massma.Inner.normal(features_list, r'"rise": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"rise": -?\d*\.?\d+', (0.33,3), fair_range=True, zeros=False) # trees
    Massma.Inner.normal(features_list, r'"run": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"run": -?\d*\.?\d+', (0.33,3), fair_range=True, zeros=False) # trees
    Massma.Inner.normal(features_list, r'"decoration_chance": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"decoration_chance": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True, clamps_outer=(0,100)) # trees
    Massma.Inner.normal(features_list, r'"core_width": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"core_width": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
    Massma.Inner.normal(features_list, r'"base_radius": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"base_radius": -?\d*\.?\d+', (0.33,3), fair_range=True, zeros=False, clamps_outer=(1,2147483647)) # trees
    Massma.Inner.normal(features_list, r'"base": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"base": -?\d*\.?\d+', (0.33,3), fair_range=True) # trees
    Massma.Inner.normal(features_list, r'"radius_step_modifier": -?\d*\.?\d+') # trees
    Massma.Inner.scale(features_list, r'"radius_step_modifier": -?\d*\.?\d+', (0.33,3), decimals=True, fair_range=True, rounding=1) # trees
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
    Massma.Inner.normal(features_list, r'"vegetation_chance": -?\d*\.?\d+')
    Massma.Inner.scale(features_list, r'"vegetation_chance": -?\d*\.?\d+', (0.33,3), fair_range=True, decimals=True, rounding=2)
    Massma.Inner.normal(features_list, r'"depth": -?\d*\.?\d+')
    Massma.Inner.scale(features_list, r'"depth": -?\d*\.?\d+', (0.33,3), fair_range=True)
    Massma.Inner.normal(features_list, r'"vertical_range": -?\d*\.?\d+')
    Massma.Inner.scale(features_list, r'"vertical_range": -?\d*\.?\d+', (0.33,3), fair_range=True)
    Massma.Inner.normal(features_list, r'"extra_deep_block_chance": -?\d*\.?\d+')
    Massma.Inner.scale(features_list, r'"extra_deep_block_chance": -?\d*\.?\d+', (0.33,3), fair_range=True, rounding=2, decimals=True)
    Massma.Inner.normal(features_list, r'"extra_edge_column_chance": -?\d*\.?\d+')
    Massma.Inner.scale(features_list, r'"extra_edge_column_chance": -?\d*\.?\d+', (0.33,3), fair_range=True, rounding=2, decimals=True)
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
if shuffle_items:
    items_path = altered_base + "\\behavior_pack\\items"
    items_list = Massma.Search.full(items_path)
    items_filters = [] # used for filtering items into sections
    items_filters.append(Massma.Filter.Exclude(items_list,r'"minecraft:food":', logic_strings=Massma.Logic.NAND))  # only shuffles foods
    items_filters.append(Massma.Filter.Exclude(items_list,r'"identifier": ".*?bundle"', logic_strings=Massma.Logic.NAND))  # only shuffles bundles
    # shuffles based on filters
    for filter in items_filters:
        Massma.Inner.normal(items_list, r'"identifier": ".*"', excludes=filter)  # shuffles what traits each item has
    # selects universal number to multiply and divide for some variables
    duration_scale = math.exp(random.uniform(math.log(0.33), math.log(3)))
    cooldown_scale = math.exp(random.uniform(math.log(0.33), math.log(3)))
    range_scale = math.exp(random.uniform(math.log(0.33), math.log(3)))
    # only effects food
    Massma.Inner.normal(items_list, r'"crop_result": ".*"', ignores=Massma.Filter.Ignore(items_path + "\\glow_berries.json"))  # shuffles what seed's plant and where
    Massma.Inner.normal(items_list, r'"minecraft:use_duration": -?\d*\.?\d+', excludes=items_filters[0])  # shuffles how long it takes to use the item
    Massma.Inner.scale(items_list, r'"minecraft:use_duration": -?\d*\.?\d+', (duration_scale, duration_scale), excludes=items_filters[0])  # multiplies and divides how long it takes to use the item
    Massma.Inner.normal(items_list, r'"cooldown_time": -?\d*\.?\d+', excludes=items_filters[0])  # shuffles how long till an item can be used again
    Massma.Inner.scale(items_list, r'"cooldown_time": -?\d*\.?\d+', (cooldown_scale, cooldown_scale), excludes=items_filters[0])  # multiplies and divides how long till an item can be used again
    Massma.Inner.normal(items_list, r'"on_use_range": \[ .*? \]', excludes=items_filters[0])  # shuffles the range of an item's effect
    Massma.Inner.scale(items_list, r'"on_use_range": \[ .*? \]', (cooldown_scale, cooldown_scale), excludes=items_filters[0])  # multiplies and divides the range of an item's effect
    Massma.Inner.normal(items_list, r'"saturation_modifier": ".*"', excludes=items_filters[0])  # shuffles much saturation a player gets from food
    Massma.Inner.normal(items_list, r'"nutrition": -?\d*\.?\d+', excludes=items_filters[0])  # shuffles how much hunger food gives back
    Massma.Inner.normal(items_list, r'"minecraft:max_stack_size": -?\d*\.?\d+', excludes=items_filters[0])  # shuffles how many items can be in a stack
    Massma.Inner.normal(items_list, r'"using_converts_to": ".*"', excludes=items_filters[0])  # shuffles what items convert to after being used

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED ITEMS")

# item catalogs
if shuffle_item_catalogs:
    item_catalogs_path = altered_base + "\\behavior_pack\\item_catalog"
    item_catalogs_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED SPAWN ITEM CATALOGS")

# aim assists
if shuffle_aim_assists:
    aim_assists_path = altered_base + "\\behavior_pack\\aim_assist"
    aim_assists_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED AIM ASSISTS")

# behavior trees
if shuffle_behavior_trees:
    behavior_trees_path = altered_base + "\\behavior_pack\\behavior_trees"
    behavior_trees_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED BEHAVIOR TREES")

# structures
if shuffle_structures:
    structures_path = altered_base + "\\behavior_pack\\structures"
    structures_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED STRUCTURES")

# worldgens
if shuffle_worldgens:
    worldgens_path = altered_base + "\\behavior_pack\\worldgens"
    worldgens_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED WORLDGEN")

# gamerules
if shuffle_gamerules:
    gamerules_path = altered_base + "\\behavior_pack\\functions"
    gamerules_data = "time set 0\nweather -WOS-\ngamerule playersSleepingPercentage 0\ngamerule randomtickspeed -RTS-\ngamerule spawnradius 0\ngamerule falldamage -TF-\ngamerule freezedamage -TF-\ngamerule firedamage -TF-\ngamerule drowningdamage -TF-\ngamerule pvp -TF-\ngamerule dodaylightcycle -TF-\ngamerule doweathercycle -TF-\ngamerule mobgriefing -TF-\ngamerule respawnblocksexplode -TF-\ngamerule tntexplodes -TF-\ngamerule dofiretick -TF-\ngamerule recipesUnlock -TF-\ngamerule naturalRegeneration -TF-\ngamerule showdeathmessages -TF-\ngamerule projectilesCanBreakBlocks -TF-\ngamerule doimmediaterespawn -FT-\ngamerule keepinventory -FT-\ngamerule doLimitedCrafting -FT-\ngamerule tntExplosionDropDecay -FT-\n"
    tick_data = '{"values": ["random_functions"]}'  # file data to rune the gamerule data command and file
    # creates folder and files to add data to
    Massma.Methods.create_folder(gamerules_path)
    gamerule_file = Massma.Methods.create_file(gamerules_path + "\\random_functions.mcfunction")  # name of the file to store the gamerule commands
    tick_file = Massma.Methods.create_file(gamerules_path + "\\ticks.json")  # name of the file to run the gamerule commands
    # adds the data inside the files
    with open(gamerule_file, 'w') as file:
        file.write(gamerules_data)
    with open(tick_file, 'w') as file:
        file.write(tick_data)
    # replace the template values with new random values
    Massma.Inner.normal(gamerule_file, "-TF-", preset=["False", "True", "True", "True"], duplicate=True)  # shuffles values that default to true
    Massma.Inner.normal(gamerule_file, "-FT-", preset=["False", "False", "False", "True"], duplicate=True)  # shuffles values that default to false
    Massma.Inner.normal(gamerule_file, "-WOS-", preset=["clear", "clear", "rain", "thunder"], duplicate=True)  # shuffles values that change starting weather
    Massma.Inner.offset(gamerule_file, "time set -?\d*\.?\d+", (0,24000), decimals=False, zeros=True)  # shuffles values that change starting time
    Massma.Inner.normal(gamerule_file, "-RTS-", preset=["1", "1", "1", "1", "2", "2", "2", "2", "3", "3", "3", "3" "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "7", "7", "7", "8", "8", "8", "9", "9", "9", "10", "10", "10", "11", "11", "12", "12", "13", "13", "14", "14", "15", "15", "16", "17", "18", "19", "20"], duplicate=True)  # shuffles values that
    Massma.Inner.offset(gamerule_file, "gamerule playersSleepingPercentage -?\d*\.?\d+", (0,100))  # shuffles values that change how many players need to sleep
    Massma.Inner.offset(gamerule_file, "gamerule spawnradius -?\d*\.?\d+", (0, 128), decimals=False, zeros=True)  # shuffles values that change spawn radius of players

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED GAMERULES")

# RESOURCE PACKS RESOURCE PACKS RESOURCE PACKS
# RESOURCE PACKS RESOURCE PACKS RESOURCE PACKS
# RESOURCE PACKS RESOURCE PACKS RESOURCE PACKS

# animation controllers
if shuffle_animation_controllers:
    animation_controllers_list = []
    animation_controllers_path = altered_base + "\\resource_pack\\animation_controllers"

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED ANIMATION CONTROLLERS")

# animations
if shuffle_animations:
    animations_path = altered_base + "\\resource_pack\\animations"
    animations_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED ANIMATIONS")

# atmospherics
if shuffle_atmospherics:
    atmospherics_path = altered_base + "\\resource_pack\\atmospherics"
    atmospherics_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED ATOMESPHERICS")

# attachables
if shuffle_attachables:
    attachables_path = altered_base + "\\resource_pack\\attachables"
    attachables_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED ATTACHABLES")

# biomes (ATTACH/SYNC TO FOG SHUFFLES)
if shuffle_biomes_resource:
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

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED BIOMES")

# cameras
if shuffle_cameras:
    cameras_path = altered_base + "\\resource_pack\\cameras"
    cameras_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED CAMERA")

# color_gradings
if shuffle_color_gradings:
    color_gradings_path = altered_base + "\\resource_pack\\color_grading"
    color_gradings_list = Massma.Search.full(color_gradings_path)
    Massma.Inner.normal(color_gradings_list, r'"identifier": ".*"') # shuffles what biome the color grading is assigned to
    Massma.Inner.normal(color_gradings_list, r'"temperature": \{.*\}', flags=[re.M, re.S])  # shuffles the temperature based color grading
    Massma.Inner.group(color_gradings_list, [r'"contrast": \[.*\]',r'"": \[.*\]',r'"gain": \[.*\]',r'"gamma": \[.*\]',r'"offset": \[.*\]', r'"saturation": \[.*\]'], flags=[re.M, re.S]) # shuffles groups of color grading, based on how colors, light, and shadows reach to each other

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED COLOR_GRADING")

# entities
if shuffle_entities_resource:
    entities_path = altered_base + "\\resource_pack\\entities"
    entities_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED ENTITIES")

# fogs
if shuffle_fogs:
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

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED FOGS")

# fonts
if shuffle_fonts:
    fonts_path = altered_base + "\\resource_pack\\font"
    fonts_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED FONTS")

# lightings
if shuffle_lightings:
    lightings_path = altered_base + "\\resource_pack\\lighting"
    lightings_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED LIGHTINGS")

# materials
if shuffle_materials:
    materials_path = altered_base + "\\resource_pack\\materials"
    materials_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED MATERIALS")

# models
if shuffle_models:
    models_path = altered_base + "\\resource_pack\\models"
    models_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED MODELS")

# particles
if shuffle_particles:
    particles_path = altered_base + "\\resource_pack\\particles"
    particles_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED PARTICLES")

# pdrs
if shuffle_pdrs:
    pdrs_path = altered_base + "\\resource_pack\\pdr"
    pdrs_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED PDRS")


# render_controllers
if shuffle_render_controllers:
    render_controllers_path = altered_base + "\\resource_pack\\render_controllers"
    render_controllers_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED RENDER CONTROLLERS")

# shadows
if shuffle_shadows:
    shadows_path = altered_base + "\\resource_pack\\shadows"
    shadows_list = Massma.Search.full(shadows_path)
    # change file data
    Massma.Inner.normal(shadows_list, r'"shadow_style": ".*"', preset=[r'"shadow_style": "blocky_shadows"',r'"shadow_style": "soft_shadows"']) # shuffles how shadows are rendered
    Massma.Inner.normal(shadows_list, r'"texel_size": -?\d*\.?\d+', preset=[r'"texel_size": 16',r'""texel_size": 32']) # shuffles the resolution of blocky shadows

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED SHADOWS")

# sounds
if shuffle_sounds:
    sounds_path = altered_base + "\\resource_pack\\sounds"
    sounds_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED SOUNDS")

# text
if shuffle_texts:
    texts_path = altered_base + "\\resource_pack\\texts"
    texts_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED TEXT")

# textures
if shuffle_textures:
    textures_path = altered_base + "\\resource_pack\\textures"
    textures_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED TEXTURES")

# uis
if shuffle_uis:
    uis_path = altered_base + "\\resource_pack\\uis"
    uis_list = []

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED UIS")

# waters
if shuffle_waters:
    waters_list = []
    waters_path = altered_base + "\\resource_pack\\water"

    Massma.Display.methods.result_notify(os.getcwd(), "randomizer", "COMPLETED WATERS")

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
Get weight to work properly (FUNCTIONS NEED THIS)
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
HARD::: a way to inject shuffled data, allowing you to shuffle data info files that didn't even have that data in the first place
HARD::: If code injections are allowed, be able to specifiy where in the file, such as under or above a existing line of code
allowing some kind of filter made for altering and controlling numbers
INNER GROUP NOT WORKING, SIMPLY DUMPING DATA
add set method to display the normal results form display
add a way to dump or add data into a text or script file (add_data, remove_data)
inside inner scale and offset, allow for normal randomization, mode randomization, and fair randomization. and even more if found useful
OVERALL THE GOAL SHOULD BE TO HAVE ALMOST 0 OF THE LINES NOT BE FROM THE LIBRARY, other than a few exceptions such as creating variables and so on
filters in filters, such as ignores inside a exclude
rounding causing 1 in scale inner method to be able to go to 2 (MAYBE)
an ignore filter that will ignore text found within the data being shuffled
not flattin, but to swap the amount of each type, so if there is 2 lavas and 4 waters, it could make it 4 lavas and 2 waters
"""