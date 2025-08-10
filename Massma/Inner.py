import re
from Massma import random  # used for seeds
from Massma.Filter import *
import Massma
import math

def normal(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, flatten: bool = False, preset: str | list[str] | None = None, preshuffle: int | list[int] | None = None, chance_files: float = 1, chance_contains: float = 1, chance_total: float = 1, chance_data: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            contains = [contains] if isinstance(contains, str) else contains
            preset = preset if isinstance(preset, list) else ([preset] if preset else [])
            preshuffle = preshuffle if isinstance(preshuffle, list) else ([preshuffle] if preshuffle else [])
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])
            flags = 0 if flags is None else sum(flags)  # Combine selected flags or default to 0 (no flags)

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.inner.set_source_length(max(file_paths, key=len))

            hash_contain = f"{hash(contains[0])}"  # stores the hash of one of the contains to indicate where data is shuffled
            filtered_contains = []  # stores all the contains that will be used
            filtered_matches = []  # stores all the matches that will be shuffled and used

            # determines if contain will be used
            for contain in contains:
                if chance_contains >= random.random():  # test if a contain will even be used
                    filtered_contains.append(contain)  # contain that was randomly filtered
                else:
                    filtered_contains.append(None)  # notify system that contains name will not be used in the shuffle and will all finds with None

            # finding all the matches in file data and storing them to later be shuffled
            for file in files:
                try:
                    skipped_file = False # indicates if a file all the matches are set to None instead of keeping matches
                    # goes through all filters needed to make
                    # random change to be added or removed by filters
                    if chance_files < random.random(): # if file fails the chance, it will set all the matches to none
                       skipped_file =  True # will now set all matches to None

                    if not (any(ignore(file) for ignore in ignores)) and not (any(exclude(file) for exclude in excludes)):
                        # gives a chance to alter inside a file
                        # FILES ARE NOT ALTERED WHEN SKIPPED!!!
                        if alters is not None and skipped_file == False:
                            for alter in alters:
                                alter(file)

                        with open(file, 'r') as f:
                            data = f.read()  # stores all the data in a variable

                            # used for replacing and chance filtering out matches
                            # group(0) only grabs first match found
                            def replace(match):
                                if chance_data >= random.random():
                                    filtered_matches.append(match.group(0))
                                    return hash_contain  # will replace data with hash
                                # runs when it fails the chance files, adding empty value to keep order and structure to the preshuffle
                                filtered_matches.append(None)  # notify system that file name will not be used in the shuffle
                                return match.group(0)  # does not replace data with hash

                            # goes throw each contain for a file to find matches
                            for filtered_contain, contain in zip(filtered_contains, contains):
                                # goes through each filtered contain and calls the replace method
                                # allowing for found matches to have a chance of being filtered out, and if now they will be stored and replaced
                                if filtered_contain is not None and skipped_file == False: # normally adds found data
                                    data = re.sub(filtered_contain, replace, data, flags=flags)
                                else:  # still gets the data from ignored contained, this is to make sure preshuffle is accurate and in sync, will also do this if file is suppose to be skipped
                                    matches = len(re.findall(contain, data, flags=flags)) # gets a number of all the matches to determine the amounts of nons needed
                                    filtered_matches.extend([None] * matches)  # adds the exact amounts of Nones as there are matches

                        with open(file, 'w') as f:  # saves changes to file temporarily
                            f.write(data)

                except Exception as e:
                    Massma.Display.inner.result_error(file, "normal", e)

            # all of this below shuffles data inside files
            if preshuffle:  # preshuffle format on how the files will be shuffled and does not work with any duplicate based features
                # goes through each number in the preshuffle list to determine where an item should go
                # the numbers in the preshuffle set determine the new indexes of elements in a list
                if preset:
                    random_matches = [None] * len(preset)  # sets preshuffle length
                    for index, match in zip(preshuffle, preset):
                        random_matches[index] = match
                else:
                    random_matches = [None] * len(filtered_matches)  # sets preshuffle length
                    for index, match in zip(preshuffle, filtered_matches):
                        random_matches[index] = match

            else:  # creates a list of the filtered matches for shuffling in the next steps, like the others above without anything fancy to it
                if preset: # ignores all data found in files and injects data from contains, THIS SHOULD BE DONE WITH DUPLICATE
                    random_matches = preset.copy()
                else:
                    random_matches = filtered_matches.copy()

            # removes all None values caused by failing the chance file data
            # the none values are used to solve the problem with preshuffles and chances not being in sync
            random_matches = [match for match in random_matches if match is not None]
            filtered_matches = [match for match in filtered_matches if match is not None]  # souly to display changes correctly

            # flatting and duplication for the shuffled lists
            if duplicate: # allows for the same data to be given to multiple different files instead of just one
                if flatten: # removes all redundant and duplicate data before
                    flatten_matches = list(set(random_matches))  # Remove duplicates and allowing for highly more even distribution of data
                    # Remove duplicates and allowing for highly more even distribution of data
                    random_matches = random.choices(flatten_matches, k=len(filtered_matches))  # Fills list back up
                else:
                    random_matches = random.choices(random_matches, k=len(filtered_matches))  # Fills list back up

            elif not preshuffle:  # normal shuffle, only if there was no preshuffle used
                random.shuffle(random_matches)

            # enters all the data back into the files in a shuffle order
            for file in files:
                with open(file, 'r') as f:  # opens file
                    data = f.read()  # stores all the data from the file
                    while data.count(hash_contain) > 0:  # continues loop until there are 0 hashes left
                        data = data.replace(hash_contain, random_matches[0], 1)
                        Massma.Display.inner.result(file, "normal", filtered_matches.pop(0), random_matches.pop(0))

                    # saves all the changes made
                    with open(file, 'w') as f:
                        f.write(data)

    except Exception as e:
        Massma.Display.inner.result_error(len(files), "normal", e)
    Massma.Display.inner.set_source_length(0)  # resets source length after a method ends


def group(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, flatten: bool = False, preset: str | list[str] | None = None, preshuffle: int | list[int] | None = None, chance_files: float = 1, chance_total: float = 1, chance_data: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            contains = [contains] if isinstance(contains, str) else contains
            preset = preset if isinstance(preset, list) else ([preset] if preset else [])
            preshuffle = preshuffle if isinstance(preshuffle, list) else ([preshuffle] if preshuffle else [])
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])
            flags = 0 if flags is None else sum(flags)  # Combine selected flags or default to 0 (no flags)

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.inner.set_source_length(max(file_paths, key=len))

            hash_contains = []  # stores the hash of each contain to indicate where data is shuffled in each group
            filtered_contains = []  # stores all the contains that will be used
            filtered_groups = [[] for index in contains]  # stores all the matches in seperate groups and filtered before being combined
            group_matches = [[] for index in contains] # temporarily stores all matches into groups to them be filtered and given to filtered matches in a group organized format
            filtered_matches = []  # stores groups of matches after they are combined and will be shuffled and used

            # reminiscent of when chance_contain was used, do plan to bring it back, but just not now
            for contain in contains:
                    filtered_contains.append(contain)  # contain that was randomly filtered
                    hash_contains.append(f"{hash(contain)}") # hash that was generated and randomly filtered


            # finding all the matches in file data and storing them to later be shuffled
            for file in files:
                try:
                    skipped_file = False # indicates if a file all the matches are set to None instead of keeping matches
                    # goes through all filters needed to make
                    # random change to be added or removed by filters
                    if chance_files < random.random(): # if file fails the chance, it will set all the matches to none
                       skipped_file =  True # will now set all matches to None

                    if not (any(ignore(file) for ignore in ignores)) and not (any(exclude(file) for exclude in excludes)):
                        # gives a chance to alter inside a file
                        # FILES ARE NOT ALTERED WHEN SKIPPED!!!
                        if alters is not None and skipped_file == False:
                            for alter in alters:
                                alter(file)

                        with open(file, 'r') as f:
                            data = f.read()  # stores all the data in a variable

                            # goes throw each contain for a file to find matches
                            # indexes each contain so it can orderly organize the groups
                            for index, (filtered_contain, contain, hash_contain) in enumerate(zip(filtered_contains, contains, hash_contains)):

                                if filtered_contain is not None and skipped_file == False: # normally adds found data
                                    matches = re.findall(filtered_contain, data, flags=flags) # finds all data in one contain
                                    group_matches[index] = matches # adds and replaces previous matches to then be filtered and added to filtered matches
                                else:  # still gets the data from ignored contained, this is to make sure preshuffle is accurate and in sync, will also do this if file is suppose to be skipped
                                    matches = len(re.findall(contain, data, flags=flags)) # gets a number of all the matches to determine the amounts of nons needed
                                    # below adds the exact amounts of Nones as there are matches
                                    group_matches[index] = [None] * matches # adds and replaces previous matches to then be filtered and added to filtered matches

                            # shrink group to smallest contain
                            group_limit = len(min(group_matches, key=len)) # finds the smallest contain group
                            group_matches = [group[:group_limit] for group in group_matches] # makes all contain groups as small as the smallest group

                            # the for loops are separate do to making sure that all contains in one group will all be None, instead of some
                            if chance_data >= random.random():
                                # goes though each piece of match found, filteres it, and adds the hash to where it would be
                                for index, group in enumerate(group_matches): # goes though each group of contains, not each contain
                                    if group: # only if the list of matches in contains is not empty
                                        filtered_groups[index].extend(group)
                            else: # this is the same as the other one, but all matches are replaced with None, this is for better preshuffling
                                for index, group in enumerate(group_matches):  # goes though each group of contains, not each contain
                                    if group:  # only if the list of matches in contains is not empty
                                        group = [None] * len(group)  # converts all matches in a group into None as it failed the chance filter
                                        group_matches[index] = group # reenters the Nones into the original group, so it can correctly hash the data
                                        filtered_groups[index].extend(group)

                            # goes through adding the filtered matches hashes back into the data so they can be shuffled and reentered later
                            for group in zip(*group_matches): # converts matches into proper groups within a list to then be added
                                if all(match is None for match in group): # skips all since all the data is simply none
                                    continue
                                for index, matches in enumerate(group): # goes through each match inside the groups
                                    if filtered_contains[index] is not None: # only looks and replaces data for contain if not skipped by chance
                                        # used for replacing and chance filtering out matches
                                        # group(0) only grabs first match found
                                        def replace(match):
                                            if all(matches is not None for matches in group):  # test if all matches are None. essentially if the group is skipped
                                                return hash_contains[index]  # will replace data with hash that is assigned to that contain
                                            # runs when it fails the chance files, adding empty value to keep order and structure to the preshuffle
                                            return match.group(0)  # does not replace data with hash

                                        data = re.sub(matches, replace, data, 1, flags=flags) # replaces the data with the hash if there are no Nones

                        with open(file, 'w') as f:  # saves changes to file temporarily
                            f.write(data)

                except Exception as e:
                    Massma.Display.inner.result_error(file, "group", e)

            # combines the group of matches into their own list allowing for easier shuffling and managing
            for group in zip(*filtered_groups):  # separates the groups and combines them into groups contains 1 of each contain
                filtered_matches.append(list(group))  # puts them pack together and appends to the list to be shuffled

            # all of this below shuffles data inside files
            if preshuffle:  # preshuffle format on how the files will be shuffled and does not work with any duplicate based features
                # goes through each number in the preshuffle list to determine where an item should go
                # the numbers in the preshuffle set determine the new indexes of elements in a list
                # each None will be formated like Nones caused by chance data
                if preset:
                    random_matches = [[None for index in filtered_contains]] * len(filtered_matches)  # sets preshuffle length
                    for index, match in zip(preshuffle, preset):
                        random_matches[index] = match
                else:
                    random_matches = [[None for index in filtered_contains]] * len(filtered_matches)  # sets preshuffle length
                    for index, match in zip(preshuffle, filtered_matches):
                        random_matches[index] = match

            else:  # creates a list of the filtered matches for shuffling in the next steps, like the others above without anything fancy to it
                if preset:  # ignores all data found in files and injects data from contains, THIS SHOULD BE DONE WITH DUPLICATE
                    random_matches = preset.copy()
                else:
                    random_matches = filtered_matches.copy()

            # removes all None values caused by failing the chance file data
            # the None values are in any of the groups used to solve the problem with preshuffles and chances not being in sync
            random_matches = [group for group in random_matches if all(match is not None for match in group)]
            filtered_matches = [group for group in filtered_matches if all(match is not None for match in group)]  # souly to display changes correctly

            # flatting and duplication for the shuffled lists
            if duplicate:  # allows for the same data to be given to multiple different files instead of just one
                if flatten:  # removes all redundant and duplicate data before
                    flatten_matches = []  # Remove duplicates and allowing for highly more evenly distribution of data
                    for match in random_matches: # checks if the value in unique
                        if match not in flatten_matches:
                            flatten_matches.append(match)

                    random_matches = random.choices(flatten_matches, k=len(filtered_matches))  # Fills list back up
                else:
                    random_matches = random.choices(random_matches, k=len(filtered_matches))  # Fills list back up

            elif not preshuffle:  # normal shuffle, only if there was no preshuffle used
                random.shuffle(random_matches)

            # enters all the data back into the files in a shuffled order
            for file in files:
                with open(file, 'r') as f:  # opens file
                    data = f.read()  # stores all the data from the file
                    # only need to check on of the contains as there should never be more than the other in hash contains
                    while data.count(hash_contains[0]) > 0:  # continues loop until there are 0 hashes left
                        for index, hash_contain in enumerate(hash_contains): # used the index to get the correct match
                            data = data.replace(hash_contain, random_matches[0][index], 1)
                        Massma.Display.inner.result(file, "group", filtered_matches.pop(0), random_matches.pop(0))

                    # saves all the changes made
                    with open(file, 'w') as f:
                        f.write(data)

    except Exception as e:
        Massma.Display.inner.result_error(len(files), "group", e)
    Massma.Display.inner.set_source_length(0)  # resets source length after a method ends


def scale(files: str | list[str], contains: str | list[str], range: tuple[float, float] | tuple[int, int], *, fair_range: bool = False, decimals: bool = False, zeros: bool = True, rounding: int = 2, minmaxing: bool = False, minmax_matching: bool = True, clamp_matching: bool = False,
          clamps_outer: tuple[float, float] | tuple[int, int] | None = None, clamps_inner: tuple[float, float] | tuple[int, int] | None = None, chance_files: float = 1, chance_contains: float = 1, chance_total: float = 1, chance_data: float = 1,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            contains = [contains] if isinstance(contains, str) else contains
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])
            flags = 0 if flags is None else sum(flags)  # Combine selected flags or default to 0 (no flags)

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.inner.set_source_length(max(file_paths, key=len))

            hash_contain = f"{hash(contains[0])}"  # stores the hash of one of the contains to indicate where data is swapped
            filtered_contains = []  # stores all the contains that will be used

            # determines if contain will be used
            for contain in contains:
                if chance_contains >= random.random():  # test if a contain will even be used
                    filtered_contains.append(contain)  # contain that was randomly filtered
                else:
                    filtered_contains.append(None)  # notify system that contains name will not be used in the shuffle and will all finds with None

            # finding all the matches in file data and storing them to be added or subtracted
            for file in files:
                try:
                    if chance_files < random.random(): # if file fails the chance, it will move on to the next file, not effected the current file
                        continue # moves to next file

                    # goes here instead as they need to be reset after every file, as the scaled data is not shuffled between or in files
                    filtered_matches = []  # stores all the matches that will be scaled and used
                    altered_matches = []  # matches altered from scaling and will be put back into the files

                    # test the files in filters to see if they should be ignored
                    if not (any(ignore(file) for ignore in ignores)) and not (any(exclude(file) for exclude in excludes)):
                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                        with open(file, 'r') as f:
                            data = f.read()  # stores all the data in a variable

                            # used for replacing and chance filtering out matches
                            # group(0) only grabs first match found
                            def replace(match):
                                if chance_data >= random.random():
                                    filtered_matches.append(match.group(0))
                                    return hash_contain  # will replace data with hash
                                return match.group(0)  # does not replace data with hash


                            # goes throw each contain for a file to find matches
                            for filtered_contain, contain in zip(filtered_contains, contains):
                                # goes through each filtered contain and calls the replace method
                                # allowing for found matches to have a chance of being filtered out, and if now they will be stored and replaced
                                if filtered_contain is not None:  # normally adds found data
                                    data = re.sub(filtered_contain, replace, data, flags=flags)

                            with open(file, 'w') as f:  # saves changes to file temporarily
                                f.write(data)

                        # goes though each match collected scaled up or down, and then put back inside its original location in the file
                        for filtered_match in filtered_matches:
                            values = re.findall(r"-?\d+\.?\d*", filtered_match)  # finds all the numbers to scale in the filtered_match
                            altered_match = re.sub(r"-?\d+\.?\d*", hash_contain ,filtered_match) # temporarily replaces with hashes to replace later with new values

                            # altering and scaling data inside matches
                            reroll_attempts = 0  # the current attempts to reroll the values, if it get to 10000, then the code does not scale the match provided
                            while True: #continues this loop as long as rerolling is required, if a reroll happens, then loop is activated again
                                altered_values = []  # will store all the vales altered so that they can be put in the altered match
                                reroll = False # store if while loop should continue, if true, the while loop will happen again
                                # when a reroll happens, all values are redone to make sure infinite loops do not occur if the first value is always bigger than the second

                                # the logs and exp make it so that even if a user enters a value like (0.5,2) it will not cause
                                for value in values:
                                    # everything below scales the value and then adds attributes and criteria to the value to make sure its the correct value
                                    if isinstance(range, tuple) and all(isinstance(datatype, int) for datatype in range):  # makes the value generated a integer
                                        value = int(value)
                                        if fair_range: # makes the distribution in chances more even instead of choosing numbers outside -1 and 1
                                            altered_value = value * math.exp(random.uniform(math.log(range[0]), math.log(range[1])))  # Random between range in integer values
                                        else:
                                            altered_value = value * random.uniform(range[0], range[1])  # Random between range in integer values
                                    elif isinstance(range, tuple) and all(isinstance(datatype, float) for datatype in range):  # makes the value generated a integer
                                        value = float(value)
                                        if fair_range: # makes the distribution in chances more even instead of choosing numbers outside -1 and 1
                                            altered_value = value * math.exp(random.uniform(math.log(range[0]), math.log(range[1])))  # Random between range in float values
                                        else:
                                            altered_value = value * random.uniform(range[0], range[1])  # Random between range in float values
                                    else: # if user inputs a float and int in tuple, defaults to float
                                        value = float(value)
                                        if fair_range: # makes the distribution in chances more even instead of choosing numbers outside -1 and 1
                                            altered_value = value * math.exp(random.uniform(math.log(range[0]), math.log(range[1])))  # Random between range in float values
                                        else:
                                            altered_value = value * random.uniform(range[0], range[1])  # Random between range in float values
                                    # if decimals is true, it will stay as a decimal and float form, round value
                                    if decimals:
                                        altered_value = round(altered_value, rounding)
                                    else:  # if value will not be in decimal form, it will round to the nearing whoe number
                                        altered_value = round(altered_value)

                                    # clamps the value to make sure the value is within the desired range
                                    # clamps_outer makes sure that the value is not over the desired bounds
                                    # clamps_inner makes sure that the value is not under the desired values
                                    # if matching is used, that means it can also equal the clamps, and cannot be equal to clamps if matching is off
                                    if clamps_outer is not None or clamps_inner is not None:
                                        if ((not clamp_matching and not (clamps_outer and clamps_outer[0] <= altered_value <= clamps_outer[1] and not (clamps_inner and clamps_inner[0] <= altered_value <= clamps_inner[1])))
                                         or (clamp_matching and not ((not (clamps_outer and clamps_outer[0] <= altered_value <= clamps_outer[1])) and (clamps_inner and clamps_inner[0] <= altered_value <= clamps_inner[1])))):

                                            reroll = True # requires while true loop to reactive after fully altering the value
                                            break # as reroll happens, skips rest of values loop, as everything else is wrong

                                    # test if altered value is a zero and if zeros are a sufficient value option
                                    if not zeros and altered_value == 0:
                                        reroll = True  # requires while true loop to reactive after fully altering the value
                                        break  # as reroll happens, skips rest of values loop, as everything else is wrong

                                    # tests if the vales are minmax, this mean that each value is bigger or the same as the previous one added to the altered_values list
                                    # if a values does not pass this, reroll happens, and this is skipped if no values have been given yet
                                    # matching allows the altered value to be the same as the previous minmax value
                                    if altered_values and minmaxing: # runs if something is in the list to start a minmax test
                                        if (altered_values[-1] > altered_value and minmax_matching) or (altered_values[-1] >= altered_value and not minmax_matching): # test the last added value into the list with the newly added value
                                            reroll = True # requires while true loop to reactive after fully altering the value
                                            break # as reroll happens, skips rest of values loop, as everything else is wrong

                                    # stores all altered values to later be put back in the altered match
                                    altered_values.append(altered_value)

                                if not reroll: # no reroll is needed
                                    # adds the altered values back into the altered match to then be put back into data
                                    for altered_value in altered_values:
                                        altered_match = re.sub(hash_contain, str(altered_value), altered_match, 1) # adds back each altered value in order`

                                    altered_matches.append(altered_match) # adds to list to be added back to data later
                                    break # ends the while true loop, stopping the reroll loop
                                else: # adds one to the reroll tries and then tries again
                                    reroll_attempts += 1
                                if reroll_attempts >= 10000:  # too many attempts where made, does not change the match and moves to the next filtered match
                                    # adds the none altered version of the match to be put back in the data
                                    altered_matches.append(filtered_match)  # adds the filtered match in as the other failed
                                    Massma.Display.inner.result_warning(file, "scale", 'value unaltered due to unfulfilled constraints')
                                    break  # ends the while true loop, stopping the reroll loop


                        # get back the data from the file to renter the scaled values back into the file and display the changes
                        with open(file, 'r') as f:
                            data = f.read()  # stores all the data in a variable

                            while data.count(hash_contain) > 0:  # continues loop until there are 0 hashes left
                                data = data.replace(hash_contain, altered_matches[0], 1)
                                Massma.Display.inner.result(file, "scale", filtered_matches.pop(0), altered_matches.pop(0))

                        with open(file, 'w') as f:  # saves changes made after all the scaling
                            f.write(data)

                except Exception as e:
                    Massma.Display.inner.result_error(file, "scale", e)

    except Exception as e:
        Massma.Display.inner.result_error(len(files), "scale", e)
    Massma.Display.inner.set_source_length(0)  # resets source length after a method ends

def offset(files: str | list[str], contains: str | list[str], range: tuple[float, float] | tuple[int, int], *, fair_range: bool = False, decimals: bool = False, zeros: bool = True, rounding: int = 2, minmaxing: bool = False, minmax_matching: bool = True, clamp_matching: bool = False,
           clamps_outer: tuple[float, float] | tuple[int, int] | None = None, clamps_inner: tuple[float, float] | tuple[int, int] | None = None, chance_files: float = 1, chance_contains: float = 1, chance_total: float = 1, chance_data: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            contains = [contains] if isinstance(contains, str) else contains
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])
            flags = 0 if flags is None else sum(flags)  # Combine selected flags or default to 0 (no flags)

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.inner.set_source_length(max(file_paths, key=len))

            hash_contain = f"{hash(contains[0])}"  # stores the hash of one of the contains to indicate where data is swapped
            filtered_contains = []  # stores all the contains that will be used

            # determines if contain will be used
            for contain in contains:
                if chance_contains >= random.random():  # test if a contain will even be used
                    filtered_contains.append(contain)  # contain that was randomly filtered
                else:
                    filtered_contains.append(None)  # notify system that contains name will not be used in the shuffle and will all finds with None

            # finding all the matches in file data and storing them to be added or subtracted
            for file in files:
                try:
                    if chance_files < random.random(): # if file fails the chance, it will move on to the next file, not effected the current file
                        continue # moves to next file

                    # goes here instead as they need to be reset after every file, as the offseted data is not shuffled between or in files
                    filtered_matches = []  # stores all the matches that will be offseted and used
                    altered_matches = []  # matches altered from scaling and will be put back into the files

                    # test the files in filters to see if they should be ignored
                    if not (any(ignore(file) for ignore in ignores)) and not (any(exclude(file) for exclude in excludes)):
                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                        with open(file, 'r') as f:
                            data = f.read()  # stores all the data in a variable

                            # used for replacing and chance filtering out matches
                            # group(0) only grabs first match found
                            def replace(match):
                                if chance_data >= random.random():
                                    filtered_matches.append(match.group(0))
                                    return hash_contain  # will replace data with hash
                                return match.group(0)  # does not replace data with hash


                            # goes throw each contain for a file to find matches
                            for filtered_contain, contain in zip(filtered_contains, contains):
                                # goes through each filtered contain and calls the replace method
                                # allowing for found matches to have a chance of being filtered out, and if now they will be stored and replaced
                                if filtered_contain is not None:  # normally adds found data
                                    data = re.sub(filtered_contain, replace, data, flags=flags)

                            with open(file, 'w') as f:  # saves changes to file temporarily
                                f.write(data)

                        # goes though each match collected offseted up or down, and then put back inside its original location in the file
                        for filtered_match in filtered_matches:
                            values = re.findall(r"-?\d+\.?\d*", filtered_match)  # finds all the numbers to offset in the filtered_match
                            altered_match = re.sub(r"-?\d+\.?\d*", hash_contain ,filtered_match) # temporarily replaces with hashes to replace later with new values

                            # altering and scaling data inside matches
                            reroll_attempts = 0  # the current attempts to reroll the values, if it get to 10000, then the code does not offset the match provided
                            while True: #continues this loop as long as rerolling is required, if a reroll happens, then loop is activated again
                                altered_values = []  # will store all the vales altered so that they can be put in the altered match
                                reroll = False # store if while loop should continue, if true, the while loop will happen again
                                # when a reroll happens, all values are redone to make sure infinite loops do not occur if the first value is always bigger than the second

                                for value in values:
                                    # everything below offsets the value and then adds attributes and criteria to the value to make sure its the correct value
                                    if isinstance(range, tuple) and all(isinstance(datatype, int) for datatype in range):  # makes the value generated a integer
                                        value = int(value)
                                        if fair_range:  # makes the distribution in chances more even instead of choosing numbers outside -1 and 1
                                            altered_value = value + math.exp(random.uniform(math.log(range[0]), math.log(range[1])))  # Random between range in integer values
                                        else:
                                            altered_value = value + random.uniform(range[0], range[1])  # Random between range in integer values
                                    elif isinstance(range, tuple) and all(isinstance(datatype, float) for datatype in range):  # makes the value generated a integer
                                        value = float(value)
                                        if fair_range:  # makes the distribution in chances more even instead of choosing numbers outside -1 and 1
                                            altered_value = value + math.exp(random.uniform(math.log(range[0]), math.log(range[1])))  # Random between range in float values
                                        else:
                                            altered_value = value + random.uniform(range[0], range[1])  # Random between range in float values
                                    else:  # if user inputs a float and int in tuple, defaults to float
                                        value = float(value)
                                        if fair_range:  # makes the distribution in chances more even instead of choosing numbers outside -1 and 1
                                            altered_value = value + math.exp(random.uniform(math.log(range[0]), math.log(range[1])))  # Random between range in float values
                                        else:
                                            altered_value = value + random.uniform(range[0], range[1])  # Random between range in float values

                                        # if decimals is true, it will stay as a decimal and float form, round value
                                        if decimals:
                                            altered_value = round(altered_value, rounding)
                                        else:  # if value will not be in decimal form, it will round to the nearing whoe number
                                            altered_value = round(altered_value)

                                    # if decimals is true, it will stay as a decimal and float form, round value
                                    if decimals:
                                        altered_value = round(altered_value, rounding)
                                    else:  # if value will not be in decimal form, then it will be converted to an integer format
                                        altered_value = round(altered_value)


                                    # clamps the value to make sure the value is within the desired range
                                    # clamps_outer makes sure that the value is not over the desired bounds
                                    # clamps_inner makes sure that the value is not under the desired values
                                    # if matching is used, that means it can also equal the clamps, and cannot be equal to clamps if matching is off
                                    if clamps_outer is not None or clamps_inner is not None:
                                        if ((not clamp_matching and not (clamps_outer and clamps_outer[0] <= altered_value <= clamps_outer[1] and not (clamps_inner and clamps_inner[0] <= altered_value <= clamps_inner[1])))
                                         or (clamp_matching and not ((not (clamps_outer and clamps_outer[0] <= altered_value <= clamps_outer[1])) and (clamps_inner and clamps_inner[0] <= altered_value <= clamps_inner[1])))):

                                            reroll = True # requires while true loop to reactive after fully altering the value
                                            break # as reroll happens, skips rest of values loop, as everything else is wrong

                                    # test if altered value is a zero and if zeros are a sufficient value option
                                    if not zeros and altered_value == 0:
                                        reroll = True  # requires while true loop to reactive after fully altering the value
                                        break  # as reroll happens, skips rest of values loop, as everything else is wrong

                                    # tests if the vales are minmax, this mean that each value is bigger or the same as the previous one added to the altered_values list
                                    # if a values does not pass this, reroll happens, and this is skipped if no values have been given yet
                                    # matching allows the altered value to be the same as the previous minmax value
                                    if altered_values and minmaxing: # runs if something is in the list to start a minmax test
                                        if (altered_values[-1] > altered_value and minmax_matching) or (altered_values[-1] >= altered_value and not minmax_matching): # test the last added value into the list with the newly added value
                                            reroll = True # requires while true loop to reactive after fully altering the value
                                            break # as reroll happens, skips rest of values loop, as everything else is wrong

                                    # stores all altered values to later be put back in the altered match
                                    altered_values.append(altered_value)

                                if not reroll: # no reroll is needed
                                    # adds the altered values back into the altered match to then be put back into data
                                    for altered_value in altered_values:
                                        altered_match = re.sub(hash_contain, str(altered_value), altered_match, 1) # adds back each altered value in order`

                                    altered_matches.append(altered_match) # adds to list to be added back to data later
                                    break # ends the while true loop, stopping the reroll loop
                                else: # adds one to the reroll tries and then tries again
                                    reroll_attempts += 1
                                if reroll_attempts >= 10000:  # too many attempts where made, does not change the match and moves to the next filtered match
                                    # adds the none altered version of the match to be put back in the data
                                    altered_matches.append(filtered_match)  # adds the filtered match in as the other failed
                                    Massma.Display.inner.result_warning(file, "offset", 'value unaltered due to unfulfilled constraints')
                                    break  # ends the while true loop, stopping the reroll loop


                        # get back the data from the file to renter the offseted values back into the file and display the changes
                        with open(file, 'r') as f:
                            data = f.read()  # stores all the data in a variable

                            while data.count(hash_contain) > 0:  # continues loop until there are 0 hashes left
                                data = data.replace(hash_contain, altered_matches[0], 1)
                                Massma.Display.inner.result(file, "offset", filtered_matches.pop(0), altered_matches.pop(0))

                        with open(file, 'w') as f:  # saves changes made after all the scaling
                            f.write(data)

                except Exception as e:
                    Massma.Display.inner.result_error(file, "offset", e)

    except Exception as e:
        Massma.Display.inner.result_error(len(files), "offset", e)
    Massma.Display.inner.set_source_length(0)  # resets source length after a method ends