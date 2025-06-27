import re

from Massma import random  # used for seeds
from Massma.Filter import *
import Massma

def normal(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, flatten: bool = False, preset: str | list[str] | None = None, preshuffle: int | list[int] | None = None, weights: int | list[int] | None = None, chance_files: float = 1, chance_contains: float = 1, chance_total: float = 1, chance_data: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            contains = [contains] if isinstance(contains, str) else contains
            preset = preset if isinstance(preset, list) else ([preset] if preset else [])
            preshuffle = preshuffle if isinstance(preshuffle, list) else ([preshuffle] if preshuffle else [])
            weights = weights if isinstance(weights, list) else ([weights] if weights else [])
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
                       skipped_file =  True # will not set all matches to None

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
                    Massma.Display.inner.result_error(files, "normal", e)

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

            # if no weight is assigned, this will set all to 1 to make sure random.choices does not break
            # if a user enters any amount of weights, this will not run, causing errors occur if the wrong amount is givin
            # STILL NEEDS WORK ON
            if not weights:
                weights = [1] * len(filtered_matches)  # adds the exact amounts of 0 weights as there are filtered matches

            # flatting and duplication for the shuffled lists
            # additionally weight can be used to calibrate the duplication to your needs
            if duplicate: # allows for the same data to be given to multiple different files instead of just one
                if flatten: # removes all redundant and duplicate data before
                    flatten_matches = list(set(random_matches))  # Remove duplicates and allowing for highly more even distribution of data
                    random_matches = random.choices(flatten_matches, k=len(filtered_matches), weights=weights)  # Fills list back up
                else:
                    random_matches = random.choices(random_matches, k=len(filtered_matches), weights=weights)  # Fills list back up

            elif not preshuffle:  # normal shuffle, only if there was no preshuffle used
                random.shuffle(random_matches)

            # enters all the data back into the files in a shuffle order
            for file in files:
                with open(file, 'r') as f:  # opens file
                    data = f.read()  # stores all the data from the file
                    while data.count(hash_contain) > 0:  #continies loop until there are 0 hashes left
                        data = data.replace(hash_contain, random_matches[0], 1)
                        Massma.Display.inner.result(file, "normal", filtered_matches.pop(0), random_matches.pop(0))

                    # saves all the changes made
                    with open(file, 'w') as f:
                        f.write(data)

    except Exception as e:
        print(e)
        Massma.Display.inner.result_error(len(files), "normal", e)


def group(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, flatten: bool = False, weight: int | list[int] | None = None, preshuffle: int | list[int] | None = None, chance_files: float = 1, chance_contains: float = 1, chance_total: float = 1, chance_data: float = 1,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            contains = [contains] if isinstance(contains, str) else contains
            preshuffle = preshuffle if isinstance(preshuffle, list) else ([preshuffle] if preshuffle else [])
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])
            flags = 0 if flags is None else sum(flags)  # Combine selected flags or default to 0 (no flags)

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.inner.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                        with open(file, 'r') as f:
                            data = f.read()  # stores all the data in a variable

                        for contain in contains:
                            pass

                except Exception as e:
                    Massma.Display.inner.result_error(files, "group", e)

    except Exception as e:
        Massma.Display.inner.result_error(len(files), "group", e)

def scale(files: str | list[str], range: tuple[float, float] | tuple[int, int], *, zeros: bool = False, decimals: bool = False, rounding: int = 0,clamps_outer: tuple[float, float] | tuple[int, int] | None = None, clamps_inner: tuple[float, float] | tuple[int, int] | None = None,
          chance_files: float = 1, chance_total: float = 1, chance_data: float = 1,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass

def offset(files: str | list[str], range: tuple[float, float] | tuple[int, int], *, zeros: bool = False, decimals: bool = False, rounding: int = 0, clamps_outer: tuple[float, float] | tuple[int, int] | None = None, clamps_inner: tuple[float, float] | tuple[int, int] | None = None,
           chance_files: float = 1, chance_total: float = 1, chance_data: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass
