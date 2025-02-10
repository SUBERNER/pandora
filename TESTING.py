from Buffle import random  # used for seeds
import Buffle
import os
import re

# base methods
base = os.getcwd()
unchanged_base = base + "\\UNCHANGED\\bedrock-samples-1.21.50.7"
changed_base = base + "\\CHANGED\\bedrock-samples-1.21.50.7"

# formatting results
Buffle.Display.audio.set_format(2)
Buffle.Display.search.set_format(2)
Buffle.Display.image.set_format(2)
Buffle.Display.outer.set_format(2)
Buffle.Display.inner.set_format(2)
Buffle.Display.methods.set_format(2)
Buffle.Display.filter.set_format(2)
Buffle.seed(3347899999999)

# small setup
Buffle.copy(unchanged_base, changed_base)
changed_base = Buffle.redo_name(changed_base, "RANDOMIZER")
boss_ignore = Buffle.Filter.Ignore([changed_base + "\\behavior_pack\\entities\\OTHERS\\ender_dragon.json", changed_base + "\\behavior_pack\\entities\\OTHERS\\elder_guardian.json", changed_base + "\\behavior_pack\\entities\\OTHERS\\wither.json"])


# entities
entities_list = []
entities_path = changed_base + "\\behavior_pack\\entities"
entities_list.append(Buffle.Search.full(entities_path + "\\BOATS"))
entities_list.append(Buffle.Search.full(entities_path + "\\CUBES"))
entities_list.append(Buffle.Search.full(entities_path + "\\OTHERS"))
entities_list.append(Buffle.Search.full(entities_path + "\\FISH"))
entities_list.append(Buffle.Search.full(entities_path + "\\MINECARTS"))
entities_list.append(Buffle.Search.full(entities_path + "\\PROJECTILES"))
entities_list.append(Buffle.Search.full(entities_path + "\\SQUIDS"))
for folder in entities_list:
    Buffle.Inner.group(folder, [r'"identifier": ".*",', r'"width": .*', r'"height": .*'], ignores=boss_ignore)
    Buffle.Inner.normal(folder, r'"jump_delay": \[\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*\]')
    Buffle.Inner.normal(folder, r'"minecraft:health": {.*?}', flags=[re.M, re.S])
    Buffle.Inner.normal(folder, r'"damage": -?\d*\.?\d+')
    for file in folder:
        Buffle.move(file, os.path.dirname(os.path.dirname(file)))
Buffle.Inner.normal(Buffle.Search.full(changed_base + "\\behavior_pack\\entities"), r'"power": \d*\.?\d+')
Buffle.Inner.multiply(Buffle.Search.full(changed_base + "\\behavior_pack\\entities"), r'"power": \d*\.?\d+', (0.5, 2))


# spawn_rules
spawn_rules_list = []
spawn_rules_path = changed_base + "\\behavior_pack\\spawn_rules"
spawn_rules_list.append(Buffle.Search.full(spawn_rules_path + "\\FISH"))
spawn_rules_list.append(Buffle.Search.full(spawn_rules_path + "\\OTHER"))
for folder in spawn_rules_list:
    Buffle.Inner.normal(folder, r'"identifier": ".*"')
    Buffle.Inner.normal(folder, r'"adjust_for_weather": .*')
    Buffle.Inner.normal(folder, r'"default": -?\d*\.?\d+')
    Buffle.Inner.normal(folder, r'"rarity": -?\d*\.?\d+')
    Buffle.Inner.normal(folder, r'"underground": -?\d*\.?\d+')
    Buffle.Inner.normal(folder, r'"surface": -?\d*\.?\d+')
    Buffle.Inner.normal(folder, r'"minecraft:herd": {.*?}', flags=[re.M, re.S])
    Buffle.Inner.normal(folder, r'"minecraft:brightness_filter": {.*?}', flags=[re.M, re.S])
    Buffle.Inner.multiply(folder, r'"default": -?\d*\.?\d+', (0.5, 2), allow_zeros=False)
    Buffle.Inner.multiply(folder, r'"rarity": -?\d*\.?\d+', (0.5, 2), allow_zeros=False)
    Buffle.Inner.multiply(folder, r'"underground": -?\d*\.?\d+', (0.5, 2), allow_zeros=False)
    Buffle.Inner.multiply(folder, r'"surface": -?\d*\.?\d+', (0.5, 2), allow_zeros=False)
    Buffle.Inner.multiply(folder, r'"minecraft:herd": {.*?}', (0.5, 2), flags=[re.M, re.S], allow_zeros=False)
    for file in folder:
        Buffle.move(file, os.path.dirname(os.path.dirname(file)))

# trading
trading_list = []
trading_path = changed_base + "\\behavior_pack\\trading"
trading_list.append(Buffle.Search.full(trading_path))
trading_list.append(Buffle.Search.full(trading_path + "\\economy_trades"))
for folder in trading_list:
    Buffle.Inner.group(folder, [r'"min": \d', r'"max": \d'])
    Buffle.Inner.normal(folder, r'"num_to_select": -?\d*\.?\d+')
    Buffle.Inner.normal(folder, r'"quantity": -?\d*\.?\d+')
    Buffle.Inner.normal(folder, r'"trader_exp": -?\d*\.?\d+')
    Buffle.Inner.normal(folder, r'"max_uses": -?\d*\.?\d+')
    Buffle.Inner.normal(folder, r'"reward_exp": [a-zA-Z]+')
    Buffle.Inner.normal(folder, r'"price_multiplier": -?\d*\.?\d+')
    Buffle.Inner.normal(folder, r'"total_exp_required": \d')


# loot
loot_list = []
loot_path = changed_base + "\\behavior_pack\\loot_tables"
loot_list.append((Buffle.Search.full(loot_path + "\\chests", deep_search=True)))
for file in loot_list[0]:  # removes all files from trial chambers REWARDS (ALLOW ANYTHING BUT IN FUTURE UPDATES)
    if "REWARDS" in file:
        loot_list[0].remove(file)
loot_list.append((Buffle.Search.full(loot_path + "\\chests\\trial_chambers\\REWARDS")))
loot_list.append(Buffle.Search.full(loot_path + "\\dispensers", deep_search=True))
loot_list.append(Buffle.Search.full(loot_path + "\\equipment", deep_search=True))
loot_list.append(Buffle.Search.full(loot_path + "\\gameplay"))
loot_list.append(Buffle.Search.full(loot_path + "\\gameplay\\entities"))
loot_list.append(Buffle.Search.full(loot_path + "\\gameplay\\fishing"))
loot_list.append(Buffle.Search.full(loot_path + "\\pots", deep_search=True))
loot_list.append(Buffle.Search.full(loot_path + "\\entities\\ARMOR"))
loot_list.append(Buffle.Search.full(loot_path + "\\entities\\BRUSH"))
loot_list.append(Buffle.Search.full(loot_path + "\\entities\\EQUIPMENT"))
loot_list.append(Buffle.Search.full(loot_path + "\\entities\\GIVE"))
loot_list.append(Buffle.Search.full(loot_path + "\\entities\\OTHER"))
loot_list.append(Buffle.Search.full(loot_path + "\\entities\\RAID"))
loot_list.append(Buffle.Search.full(loot_path + "\\spawners", deep_search=True))
for folder in loot_list:
    Buffle.Inner.normal(folder, r'"weight": \d')
    Buffle.Inner.normal(folder, r'"rolls": -?\d*\.?\d+')
    Buffle.Inner.normal(folder, r'"chance": -?\d*\.?\d+')
    Buffle.Inner.normal(folder, r'"max_chance": -?\d*\.?\d+')
    Buffle.Inner.normal(folder, r'""initial_range": -?\d*\.?\d+')
    Buffle.Inner.normal(folder, r'"bonus_rolls": -?\d*\.?\d+')
    Buffle.Inner.normal(folder, r'"bonus_chance": -?\d*\.?\d+')
    Buffle.Inner.multiply(folder, r'"weight": \d', (0.5, 2), allow_zeros=False)
    Buffle.Inner.multiply(folder, r'"rolls": -?\d*\.?\d+', (0.5, 2), allow_zeros=False)
    Buffle.Inner.multiply(folder, r'"chance": -?\d*\.?\d+', (0.5, 2), allow_zeros=False)
    Buffle.Inner.multiply(folder, r'"max_chance": -?\d*\.?\d+', (0.5, 2), allow_zeros=False)
    Buffle.Inner.multiply(folder, r'""initial_range": -?\d*\.?\d+', (0.5, 2), allow_zeros=False)
    Buffle.Inner.multiply(folder, r'"bonus_rolls": -?\d*\.?\d+', (0.5, 2), allow_zeros=False)
    Buffle.Inner.multiply(folder, r'"bonus_chance": -?\d*\.?\d+', (0.5, 2), allow_zeros=False)
    Buffle.Inner.group(folder, [r'"type": "loot_table"', r'"name: .*"'])
    Buffle.Inner.group(folder, [r'"type": "item"', r'"name: .*"'])
    for file in folder:
        if "trial_chamber.json" in file:  # removes trial_chamber.json from equipment
            folder.remove(file)
        if "spawners" in file:  # removes all spawners from name shuffling
            folder.remove(file)
    Buffle.Outer.normal(folder)
    for file in folder:
        if "entities" in file:  # puts entities pack in their correct directory
            Buffle.move(file, os.path.dirname(os.path.dirname(file)))
for file in loot_list[1]:  # corrects the location of REWARDS
    Buffle.move(file, os.path.dirname(os.path.dirname(file)))


# biomes
biomes_list = []
biomes_path = changed_base + "\\behavior_pack\\biomes"
biomes_list.append(Buffle.Search.full(biomes_path + "\\UNDERWORLD"))
biomes_list.append(Buffle.Search.full(biomes_path + "\\END"))
biomes_list.append(Buffle.Search.full(biomes_path + "\\NETHER"))
biomes_list.append(Buffle.Search.full(biomes_path + "\\OVERWORLD"))
for folder in biomes_list:
    Buffle.Inner.normal(folder, r'"identifier": ".*"')
    # Buffle.Inner.group(folder, [r'"sea_floor_material":\s*.*?(?=,)', r'"foundation_material":\s*.*?(?=,)', r'"mid_material":\s*.*?(?=,)', r'"top_material":\s*.*?(?=,)'])
    for file in folder:
        Buffle.move(file, os.path.dirname(os.path.dirname(file)))
biomes_list = Buffle.Search.full(biomes_path)
Buffle.Inner.normal(biomes_list, r'"sea_material": ".*"', replace_auto=True, duplicates=True)
Buffle.Inner.normal(biomes_list, r'"sea_floor_depth": -?\d*\.?\d+', replace_auto=True, duplicates=True)
#Buffle.Inner.normal(biomes_list, r'"downfall": .*')
#Buffle.Inner.normal(biomes_list, r'"snow_accumulation": \[\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*\]')
#Buffle.Inner.normal(biomes_list, r'"temperature": .*')
Buffle.Inner.normal(biomes_list, r'"noise_params": \[\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*\"', replace_auto=True, duplicates=True)
Buffle.Inner.normal(biomes_list, r'"noise_type": ".*"', replace_auto=True, duplicates=True)
Buffle.Inner.normal(biomes_list, r'"has_forest": .*', replace_auto=True, duplicates=True)
Buffle.Inner.normal(biomes_list, r'"bryce_pillars": .*', replace_auto=True, duplicates=True)
Buffle.Inner.normal(biomes_list, r'"enabled": .*', replace_auto=True, duplicates=True)
Buffle.Inner.group(biomes_list, [r'"target_temperature": .*', r'"target_humidity": .*', r'"target_altitude": .*', r'"target_weirdness": .*', r'"weight": .*'])
Buffle.Inner.normal(biomes_list, r'"east_slopes": .*', replace_auto=True, duplicates=True)
Buffle.Inner.normal(biomes_list, r'"north_slopes": .*', replace_auto=True, duplicates=True)
Buffle.Inner.normal(biomes_list, r'"peaks_factor": .*', replace_auto=True, duplicates=True)
Buffle.Inner.normal(biomes_list, r'"height_range": [ ".*", ".*" ]', replace_auto=True, duplicates=True)
Buffle.Inner.normal(biomes_list, [r'"blue_spores": .*', r'"ash": .*', r'"red_spores": .*', r'"white_ash": .*'], replace_auto=True, duplicates=True)


# recipes
recipes_list = []
recipes_path = changed_base + "\\behavior_pack\\recipes"
recipes_list.append(Buffle.Search.full(recipes_path + "\\BREW"))
recipes_list.append(Buffle.Search.full(recipes_path + "\\CRAFTING"))
recipes_list.append(Buffle.Search.full(recipes_path + "\\FURNACE"))
recipes_list.append(Buffle.Search.full(recipes_path + "\\SMITHING"))
recipes_list.append(Buffle.Search.full(recipes_path + "\\STONECUTTER"))
for folder in recipes_list:
    Buffle.Inner.normal(folder, r'"identifier": ".*"')
    Buffle.Inner.normal(folder, r'"count": -?\d*\.?\d+')
    Buffle.Inner.multiply(folder, r'"count": -?\d*\.?\d+', (0.5, 2), allow_zeros=False)
    Buffle.Inner.normal(folder, r'"output": ".*"')  # furnace & brewing
    Buffle.Inner.normal(folder, r'"result": ".*"')  # smithing table
    Buffle.Inner.normal(folder, r'"result": {.*?}', flags=[re.M, re.S])
    Buffle.Inner.normal(folder, r'"result": {.*?}', flags=[re.M, re.S])
    for file in folder:
        Buffle.Inner.normal(file, r'".": {')
        Buffle.move(file, os.path.dirname(os.path.dirname(file)))


# feature_rules
feature_rules_list = []
feature_rules_path = changed_base + "\\behavior_pack\\feature_rules"
feature_rules_list.append(Buffle.Search.full(feature_rules_path + "\\WARPED"))
feature_rules_list.append(Buffle.Search.full(feature_rules_path + "\\UNDERGROUND"))
feature_rules_list.append(Buffle.Search.full(feature_rules_path + "\\SOUL"))
feature_rules_list.append(Buffle.Search.full(feature_rules_path + "\\CRIMSON"))
feature_rules_list.append(Buffle.Search.full(feature_rules_path + "\\CAVES"))
for folder in feature_rules_list:
    Buffle.Inner.normal(folder, r'"places_feature": ".*"')
    for file in folder:
        Buffle.move(file, os.path.dirname(os.path.dirname(file)))
feature_rules_list = Buffle.Search.full(feature_rules_path)
Buffle.Inner.normal(feature_rules_list, r'"extent": \[\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*\]', replace_auto=True, duplicates=True)
Buffle.Inner.normal(feature_rules_list, r'"iterations": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(feature_rules_list, r'"distribution": ".*"', replace_auto=True, duplicates=True)
Buffle.Inner.group(feature_rules_list, [r'"numerator": -?\d*\.?\d+', r'"denominator": -?\d*\.?\d+'])
Buffle.Inner.normal(feature_rules_list, r'"coordinate_eval_order": ".*"', replace_auto=True, duplicates=True)

# features
features_path = changed_base + "\\behavior_pack\\features"
caves_list = (Buffle.Search.full(features_path + "\\CAVES"))
Buffle.Inner.normal(caves_list, r'"skip_carve_chance": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(caves_list, r'"width_modifier": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(caves_list, r'"y_scale": \[\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*\]', replace_auto=True, duplicates=True)
Buffle.Inner.normal(caves_list, r'"height_limit": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(caves_list, r'"horizontal_radius_multiplier": \[\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*\]', replace_auto=True, duplicates=True)
Buffle.Inner.normal(caves_list, r'"vertical_radius_multiplier": \[\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*\]', replace_auto=True, duplicates=True)
Buffle.Inner.normal(caves_list, r'"floor_level": \[\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*\]', replace_auto=True, duplicates=True)
Buffle.Inner.normal(caves_list, r'"fill_with": ".*"', replace_auto=True, duplicates=True)
Buffle.Inner.multiply(caves_list, r'"width_modifier": -?\d*\.?\d+', (0.20, 5), allow_zeros=False)
Buffle.Inner.multiply(caves_list, r'"skip_carve_chance": -?\d*\.?\d+', (0.20, 5), allow_zeros=False)
Buffle.Inner.multiply(caves_list, r'"y_scale": \[\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*\]', (0.20, 5), allow_zeros=False)
Buffle.Inner.multiply(caves_list, r'"height_limit": -?\d*\.?\d+', (0.20, 5), allow_zeros=False)
Buffle.Inner.multiply(caves_list, r'"horizontal_radius_multiplier": \[\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*\]', (0.20, 5), allow_zeros=False)
Buffle.Inner.multiply(caves_list, r'"vertical_radius_multiplier": \[\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*\]', (0.20, 5), allow_zeros=False)
Buffle.Inner.multiply(caves_list, r'"floor_level": \[\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*\]', (0.20, 5), allow_zeros=False)

features_list = (Buffle.Search.full(features_path))  # gets files after after dump
Buffle.Inner.normal(features_list, r'"count": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"iterations": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"scatter_chance": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"vegetation_chance": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.group(features_list, [r'"denominator": \b(?:\d+\.?\d*|\.\d+)\b', r'"numerator": \b(?:\d+\.?\d*|\.\d+)\b'])  # IGNORES NEGATIVE NUMBERS FOR NOW
Buffle.Inner.normal(features_list, r'"vertical_search_range": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.group(features_list, [r'"range_min": \b(?:\d+\.?\d*|\.\d+)\b', r'"range_max": \b(?:\d+\.?\d*|\.\d+)\b'])  # IGNORES NEGATIVE NUMBERS FOR NOW
Buffle.Inner.group(features_list, [r'"min": -?\d*\.?\d+', r'"max": -?\d*\.?\d+'])
Buffle.Inner.normal(features_list, r'"moisturized_amount": -?\d*\.?\d+')
Buffle.Inner.normal(features_list, r'"depth": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"max_depth": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"vertical_range": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'extent": \[\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*\]', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"max_empty_corners": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"discard_chance_on_air_exposure": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"decoration_chance": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"distribution": ".*"', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"search_range": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"chance_of_spreading": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"extra_edge_column_chance": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"extra_deep_block_chance": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'minimum_distance_below_surface": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'placement_radius_around_floor": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"fill_with": ".*"', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"canopy_height": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"canopy_radius": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"canopy_size": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"leaf_placement_attempts": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"height": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"radius": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"num_steps": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"base": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"trunk_width": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"branches_chance": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"foliage_altitude_factor": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"width_scale": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"density": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"min_altitude_factor": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"scale": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"variance": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"intervals": \[\s*(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\s*\]', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"branch_chance": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"core_width": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.group(features_list, [r'"outer_radius": -?\d*\.?\d+', r'"inner_radius": 3'])
Buffle.Inner.normal(features_list, r'"simplify_canopy": .*', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"branch_position": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"base_radius": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"radius_step_modifier": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"num_clusters": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"cluster_radius": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"branch_length": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"branch_slope": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"min_width": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"min_height_for_canopy": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"wide_bottom_layer_hole_chance": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"corner_hole_chance": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"hanging_leaves_chance": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"hanging_leaves_extension_chance": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"one_branch": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"two_branches": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"two_branches_and_trunk": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"height_rand_a": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"height_rand_b": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"hanging": .*', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"trunk_height": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"rise": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"run": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"min_sides_must_attach" -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.group(features_list, [r'"min": [.*, .*,.*]', r'"max": [.*, .*,.*]'])
#Buffle.Inner.normal(features_list, r'"enforce_survivability_rules": .*')  # COULD BREAK
#Buffle.Inner.normal(features_list, r'"enforce_placement_rules": .*')  # COULD BREAK
#Buffle.Inner.normal(features_list, r'"can_place_on_floor": .*')  # COULD BREAK
#Buffle.Inner.normal(features_list, r'"can_place_on_ceiling": .*')  # COULD BREAK
#Buffle.Inner.normal(features_list, r'"can_place_on_wall": .*')  # COULD BREAK
Buffle.Inner.normal(features_list, r'"project_input_to_floor": .*', replace_auto=True, duplicates=True)  # COULD BREAK
Buffle.Inner.normal(features_list, r'"cursor_count": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"charge_amount": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"spread_attempts": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"growth_rounds": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"spread_rounds": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"central_block_placement_chance": -?\d*\.?\d+', replace_auto=True, duplicates=True)
Buffle.Inner.normal(features_list, r'"coordinate_eval_order": ".*"', replace_auto=True, duplicates=True)
for file in caves_list:
    Buffle.move(file, os.path.dirname(os.path.dirname(file)))


# spawn_groups
spawn_groups_path = changed_base + "\\behavior_pack\\spawn_groups"
spawn_groups_list = (Buffle.Search.full(spawn_groups_path))
Buffle.Inner.normal(spawn_groups_list, r'"identifier": ".*"')
Buffle.Inner.normal(spawn_groups_list, r'"entity_type": ".*"')
Buffle.Inner.group(spawn_groups_list, [r'"min_size": -?\d*\.?\d+', r'"max_size": -?\d*\.?\d+'])
Buffle.Inner.multiply(spawn_groups_list, [r'"min_size": -?\d*\.?\d+', r'"max_size": -?\d*\.?\d+'], (0.5, 2), allow_zeros=False)


# items
items_list = []
items_path = changed_base + "\\behavior_pack\\items"
items_list.append(Buffle.Search.full(items_path + "\\FOOD"))
#items_list.append(Buffle.Search.full(items_path + "\\BUNDLE"))
items_list.append(Buffle.Search.full(items_path + "\\SEEDS"))
for folder in items_list:
    Buffle.Inner.normal(folder, r'"minecraft:use_duration": -?\d*\.?\d+')
    Buffle.Inner.normal(folder, r'"nutrition": -?\d*\.?\d+')
    Buffle.Inner.normal(folder, r'"saturation_modifier": ".*"')
    Buffle.Inner.normal(folder, r'"identifier": ".*"')
    Buffle.Inner.normal(folder, r'"crop_result": ".*"')
    Buffle.Inner.group(folder, [r'"name": ".*"', r'"chance": -?\d*\.?\d+', r'"duration": -?\d*\.?\d+', r'"amplifier": -?\d*\.?\d+'])
    for file in folder:
        Buffle.move(file, os.path.dirname(os.path.dirname(file)))


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# biomes
biomes_path = changed_base + "\\resource_pack\\biomes"
biomes_list = (Buffle.Search.full(biomes_path))
#Buffle.Inner.normal(biomes_list, r'"identifier": ".*"')
Buffle.Inner.normal(biomes_list, r'"fog_identifier": ".*"')
Buffle.Inner.normal(biomes_list, r'"surface_color": ".*"')
Buffle.Inner.normal(biomes_list, r'"sky_color": ".*"')
Buffle.Inner.group(biomes_list, [r'"addition": ".*"', r'"loop": ".*"', r'"mood": ".*"'])


# fogs
fogs_path = changed_base + "\\resource_pack\\fogs"
fogs_list = (Buffle.Search.full(fogs_path))
Buffle.Inner.normal(fogs_list, r'render_distance_type": ".*"')
Buffle.Inner.normal(fogs_list, r'"fog_color": ".*"')
Buffle.Inner.normal(fogs_list, r'"identifier": ".*"')
Buffle.Inner.group(fogs_list, [r'"fog_start": -?\d*\.?\d+', r'"fog_start": -?\d*\.?\d+'])
Buffle.Inner.group(fogs_list, [r'"min_percent": -?\d*\.?\d+', r'"mid_seconds": -?\d*\.?\d+', r'"mid_percent": -?\d*\.?\d+', r'"max_seconds": -?\d*\.?\d+'])


# colormap
colormaps_list = []
colormaps_path = changed_base + "\\resource_pack\\textures\\colormap"
colormaps_list.append(Buffle.Search.full(colormaps_path + "\\BIG"))
colormaps_list.append(Buffle.Search.full(colormaps_path + "\\SMALL"))
for folder in colormaps_list:
    Buffle.Image.brightness(folder, random.uniform(0.5, 2))
    Buffle.Image.contrast(folder, random.uniform(0.5, 2))
    Buffle.Image.saturation(folder, random.uniform(0.5, 2))
    for file in folder:
        Buffle.move(file, os.path.dirname(os.path.dirname(file)))


# blocks
blocks_list = []
blocks_path = changed_base + "\\resource_pack\\textures\\blocks"
blocks_list.append(Buffle.Search.full(blocks_path + "\\BAMBO"))
blocks_list.append(Buffle.Search.full(blocks_path + "\\GLOW"))
blocks_list.append(Buffle.Search.full(blocks_path + "\\FLOWER"))
blocks_list.append(Buffle.Search.full(blocks_path + "\\POTTERY"))
blocks_list.append(Buffle.Search.full(blocks_path + "\\ICE"))
for folder in blocks_list:
    Buffle.Outer.normal(folder)
    for file in folder:
        Buffle.move(file, os.path.dirname(os.path.dirname(file)))
blocks_list = []
blocks_list.append(Buffle.Search.full(blocks_path + "\\ANVIL"))
blocks_list.append(Buffle.Search.full(blocks_path + "\\FROSTED"))
blocks_list.append(Buffle.Search.full(blocks_path + "\\EGG"))
for folder in blocks_list:
    if random.random() > 0.5:  # makes sure there not always reversed
        Buffle.Outer.reverse(folder)
    for file in folder:
        Buffle.move(file, os.path.dirname(os.path.dirname(file)))
blocks_list = Buffle.Search.full(blocks_path + "\\SAND")
Buffle.Outer.group(blocks_list, ["red_sand", "sand"])
blocks_list = Buffle.Search.full(blocks_path + "\\SAND")
for file in blocks_list:
    Buffle.move(file, os.path.dirname(os.path.dirname(file)))
blocks_list = Buffle.Search.full(blocks_path + "\\MUSHROOM")
Buffle.Outer.group(blocks_list, ["brown", "red"])
blocks_list = Buffle.Search.full(blocks_path + "\\MUSHROOM")
for file in blocks_list:
    Buffle.move(file, os.path.dirname(os.path.dirname(file)))
blocks_list = Buffle.Search.full(blocks_path + "\\CORAL")
Buffle.Outer.group(blocks_list, ["blue", "pink", "red", "yellow"])
blocks_list = Buffle.Search.full(blocks_path + "\\CORAL")
for file in blocks_list:
    Buffle.move(file, os.path.dirname(os.path.dirname(file)))
blocks_list = Buffle.Search.full(blocks_path + "\\DROPDISP")
Buffle.Outer.group(blocks_list, ["dispenser", "dropper"])
blocks_list = Buffle.Search.full(blocks_path + "\\DROPDISP")
for file in blocks_list:
    Buffle.move(file, os.path.dirname(os.path.dirname(file)))


# items
items_path = changed_base + "\\resource_pack\\textures\\items"
items_list = Buffle.Search.full(items_path + "\\SLOTS")
if random.random() > 0.5:  # makes sure there not always reversed
    Buffle.Outer.reverse(items_list)
items_list = Buffle.Search.full(items_path + "\\SLOTS")
for file in items_list:
    Buffle.move(file, os.path.dirname(os.path.dirname(file)))
items_list = Buffle.Search.full(items_path + "\\MAP")
Buffle.Outer.normal(items_list)
items_list = Buffle.Search.full(items_path + "\\MAP")
for file in items_list:
    Buffle.move(file, os.path.dirname(os.path.dirname(file)))
items_list = Buffle.Search.full(items_path + "\\TOOLS")
Buffle.Outer.group(items_list, ["diamond", "gold", "iron", "stone", "wood","netherite"])
items_list = Buffle.Search.full(items_path + "\\TOOLS")
Buffle.Outer.group(items_list, ["pickaxe", "axe", "hoe", "shovel", "sword"])
items_list = Buffle.Search.full(items_path + "\\TOOLS")
for file in items_list:
    Buffle.move(file, os.path.dirname(os.path.dirname(file)))
items_list = Buffle.Search.full(items_path + "\\POTION")
Buffle.Outer.group(items_list, ["potion_bottle_lingering", "potion_bottle_splash", "potion_bottle"])
items_list = Buffle.Search.full(items_path + "\\POTION")
for file in items_list:
    Buffle.move(file, os.path.dirname(os.path.dirname(file)))


# colors
colors_path = changed_base + "\\resource_pack\\textures"
colors_list = []
color_swap = Buffle.Filter.Swap([(colors_path + "\\items\\COLOR\\bundle_light_gray_open.png",colors_path + "\\items\\COLOR\\bundle_silver_open.png")
                                    ,(colors_path + "\\items\\COLOR\\bundle_light_gray.png",colors_path + "\\items\\COLOR\\bundle_silver.png")
                                    ,(colors_path + "\\items\\COLOR\\bundle_light_gray_open_back.png",colors_path + "\\items\\COLOR\\bundle_silver_open_back.png")
                                    ,(colors_path + "\\items\\COLOR\\bundle_light_gray_open_front.png",colors_path + "\\items\\COLOR\\bundle_silver_open_front.png")
                                    ,(colors_path + "\\items\\candles\\light_gray_candle.png",colors_path + "\\items\\candles\\silver_candle.png")
                                    ,(colors_path + "\\blocks\\candles\\light_gray_candle.png",colors_path + "\\blocks\\candles\\silver_candle.png")
                                    ,(colors_path + "\\blocks\\candles\\light_gray_candle_lit.png",colors_path + "\\blocks\\candles\\silver_candle_lit.png")
                                    ,(colors_path + "\\blocks\\COLOR\\wool_colored_black.png",colors_path + "\\blocks\\COLOR\\wool_color_black.png")
                                    ,(colors_path + "\\blocks\\COLOR\\wool_colored_blue.png",colors_path + "\\blocks\\COLOR\\wool_color_blue.png")
                                    ,(colors_path + "\\blocks\\COLOR\\wool_colored_brown.png",colors_path + "\\blocks\\COLOR\\wool_color_brown.png")
                                    ,(colors_path + "\\blocks\\COLOR\\wool_colored_cyan.png",colors_path + "\\blocks\\COLOR\\wool_color_cyan.png")
                                    ,(colors_path + "\\blocks\\COLOR\\wool_colored_gray.png",colors_path + "\\blocks\\COLOR\\wool_color_gray.png")
                                    ,(colors_path + "\\blocks\\COLOR\\wool_colored_green.png",colors_path + "\\blocks\\COLOR\\wool_color_green.png")
                                    ,(colors_path + "\\blocks\\COLOR\\wool_colored_light_blue.png",colors_path + "\\blocks\\COLOR\\wool_color_light_blue.png")
                                    ,(colors_path + "\\blocks\\COLOR\\wool_colored_lime.png",colors_path + "\\blocks\\COLOR\\wool_color_lime.png")
                                    ,(colors_path + "\\blocks\\COLOR\\wool_colored_magenta.png",colors_path + "\\blocks\\COLOR\\wool_color_magenta.png")
                                    ,(colors_path + "\\blocks\\COLOR\\wool_colored_orange.png",colors_path + "\\blocks\\COLOR\\wool_color_orange.png")
                                    ,(colors_path + "\\blocks\\COLOR\\wool_colored_pink.png",colors_path + "\\blocks\\COLOR\\wool_color_pink.png")
                                    ,(colors_path + "\\blocks\\COLOR\\wool_colored_purple.png",colors_path + "\\blocks\\COLOR\\wool_color_purple.png")
                                    ,(colors_path + "\\blocks\\COLOR\\wool_colored_red.png",colors_path + "\\blocks\\COLOR\\wool_color_red.png")
                                    ,(colors_path + "\\blocks\\COLOR\\wool_colored_silver.png",colors_path + "\\blocks\\COLOR\\wool_color_silver.png")
                                    ,(colors_path + "\\blocks\\COLOR\\wool_colored_white.png",colors_path + "\\blocks\\COLOR\\wool_color_white.png")
                                    ,(colors_path + "\\blocks\\COLOR\\wool_colored_yellow.png",colors_path + "\\blocks\\COLOR\\wool_color_yellow.png")
                                    ,(colors_path + "\\items\\COLOR\\dye_powder_blue_new.png",colors_path + "\\items\\COLOR\\dye_powder_blue.png")
                                    ,(colors_path + "\\items\\COLOR\\dye_powder_brown_new.png",colors_path + "\\items\\COLOR\\dye_powder_brown.png")
                                    ,(colors_path + "\\items\\COLOR\\dye_powder_white_new.png",colors_path + "\\items\\COLOR\\dye_powder_white.png")
                                    ,(colors_path + "\\items\\COLOR\\dye_powder_black_new.png", colors_path + "\\items\\COLOR\\dye_powder_black.png")])
color_swap()  # swaps to format for easier shuffling
colors_list.extend(Buffle.Search.full(colors_path + "\\blocks\\candles"))
colors_list.extend(Buffle.Search.full(colors_path + "\\blocks\\COLOR"))
colors_list.extend(Buffle.Search.full(colors_path + "\\entity\\bed"))
colors_list.extend(Buffle.Search.full(colors_path + "\\items\\candles"))
colors_list.extend(Buffle.Search.full(colors_path + "\\items\\COLOR"))
Buffle.Outer.group(colors_list, ["light_blue", "black", "blue", "brown", "cyan", "gray", "green", "lime", "magenta", "pink", "purple", "silver", "white", "yellow", "orange", "red"])
color_swap()  # swaps back after shuffling
colors_list = []  # researches after color swap
colors_list.extend(Buffle.Search.full(colors_path + "\\blocks\\candles"))
colors_list.extend(Buffle.Search.full(colors_path + "\\blocks\\COLOR"))
colors_list.extend(Buffle.Search.full(colors_path + "\\entity\\bed"))
colors_list.extend(Buffle.Search.full(colors_path + "\\items\\candles"))
colors_list.extend(Buffle.Search.full(colors_path + "\\items\\COLOR"))
for file in colors_list:
    if "candles" not in file or "\\entity\\bed" not in file:
        Buffle.move(file, os.path.dirname(os.path.dirname(file)))


# entities
entities_path = changed_base + "\\resource_pack\\textures\\entities"


# environment
environment_path = changed_base + "\\resource_pack\\textures\\environment"
environment_list = Buffle.Search.full(environment_path + "\\DESTROY")
if random.random() >= 0.5:
    Buffle.Outer.reverse(environment_list)
environment_list = Buffle.Search.full(environment_path + "\\DESTROY")
for file in environment_list:
    Buffle.move(file, os.path.dirname(os.path.dirname(file)))
Buffle.Image.brightness(environment_path + "\\end_portal_colors.png", random.uniform(0.5, 2))
Buffle.Image.contrast(environment_path + "\\end_portal_colors.png", random.uniform(0.5, 2))
Buffle.Image.saturation(environment_path + "\\end_portal_colors.png", random.uniform(0.5, 2))


# UI
ui_path = changed_base + "\\resource_pack\\textures\\ui"
ui_list = Buffle.Search.full(ui_path + "\\SLOT")
if random.random() >= 0.5:
    Buffle.Outer.reverse(ui_list)
    Buffle.Image.flip(ui_list, False, True)
ui_list = Buffle.Search.full(ui_path + "\\SLOT")
for file in ui_list:
    Buffle.move(file, os.path.dirname(os.path.dirname(file)))

ui_list = Buffle.Search.full(ui_path + "\\BUBBLE")
if random.random() >= 0.5:
    Buffle.Outer.reverse(ui_list)
ui_list = Buffle.Search.full(ui_path + "\\BUBBLE")
for file in ui_list:
    Buffle.move(file, os.path.dirname(os.path.dirname(file)))

ui_list = Buffle.Search.full(ui_path + "\\ARMOR")
if random.random() >= 0.5:
    Buffle.Outer.reverse(ui_list)
    Buffle.Image.flip(ui_path + "\\armor_half.png", True, False)
ui_list = Buffle.Search.full(ui_path + "\\ARMOR")
for file in ui_list:
    Buffle.move(file, os.path.dirname(os.path.dirname(file)))

ui_list = Buffle.Search.full(ui_path + "\\HEART")
Buffle.Outer.group(ui_list, ["absorption", "freeze", "poison", "wither"])  # UPDATE MORE LATER
ui_list = Buffle.Search.full(ui_path + "\\HEART")
for file in ui_list:
    Buffle.move(file, os.path.dirname(os.path.dirname(file)))


# other
Buffle.Inner.normal(changed_base + "\\resource_pack\\textures\\flipbook_textures.json", '"ticks_per_frame": \d+')
Buffle.Inner.multiply(changed_base + "\\resource_pack\\textures\\flipbook_textures.json", '"ticks_per_frame": \d+', (0.5, 2), allow_zeros=False)

Buffle.Inner.normal(changed_base + "\\behavior_pack\\functions\\random_functions.mcfunction", "-TF-", replaces_manual=["False", "True", "True", "True"], duplicates=True)  # true on default
Buffle.Inner.normal(changed_base + "\\behavior_pack\\functions\\random_functions.mcfunction", "-FT-", replaces_manual=["False", "False", "False", "True"], duplicates=True)  # false on default
Buffle.Inner.normal(changed_base + "\\behavior_pack\\functions\\random_functions.mcfunction", "-WOS-", replaces_manual=["clear", "clear", "rain", "thunder"], duplicates=True)
Buffle.Inner.normal(changed_base + "\\behavior_pack\\functions\\random_functions.mcfunction", "-TOS-", replaces_manual=["day", "midnight", "night", "noon", "sunrise", "sunset"], duplicates=True)
Buffle.Inner.normal(changed_base + "\\behavior_pack\\functions\\random_functions.mcfunction", "-RTS-", replaces_manual=["1", "1", "1", "1", "2", "2", "2", "3", "3", "4"], duplicates=True)
Buffle.Inner.multiply(changed_base + "\\behavior_pack\\functions\\random_functions.mcfunction", "gamerule spawnradius 79", (0, 2))
Buffle.Inner.multiply(changed_base + "\\behavior_pack\\functions\\random_functions.mcfunction", "playersSleepingPercentage 50", (0, 2))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# finish
changed_base = Buffle.zip(changed_base)
changed_base = Buffle.redo_extension(changed_base, '.mcaddon')

# edits
Buffle.Display.methods.get_count()
Buffle.Display.search.get_count()
Buffle.Display.audio.get_count()
Buffle.Display.image.get_count()
Buffle.Display.outer.get_count()
Buffle.Display.inner.get_count()
Buffle.Display.filter.get_count()

"""
FUTURE UPDATES
multi-line searching
all files except
data shuffling between different variables 
Searching for data and what parts to randomize in that data
allow for better group scattering in inner
allow for multiple method files at once, for better readability
displaying group inner as wanted
alter displaying changed when no changes (FIX IT ALL)
make swaps work inside of methods
"""