from Massma import random  # used for seeds
from Massma.Filter import *
import Massma

def normal(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, flatten: bool = False, weight: int | list[int] | None = None, presets: str | list[str] | None = None, preshuffle: int | list[int] | None = None, chance_files: float = 1, chance_contains: float = 1, chance_total: float = 1, chance_data: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            contains = [contains] if isinstance(contains, str) else contains
            presets = presets if isinstance(presets, list) else ([presets] if presets else [])
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

            # used for replacing and chance filtering out matches
            # group(0) only grabs first match found
            def replace(match):
                if chance_data >= random.random():
                    filtered_matches.append(match.group(0))
                    return hash_contain  # will replace data with hash
                # runs when it fails the chance files, adding empty value to keep order and structure to the preshuffle
                filtered_matches.append(None)  # notify system that file name will not be used in the shuffle
                return match.group(0)  # does not replace data with hash

            # determines if contain will be used
            for contain in contains:
                if chance_contains >= random.random():  # test if a contain will even be used
                    filtered_contains.append(contain)  # contain that was randomly filtered
                else:
                    filtered_contains.append(None)  # notify system that contains name will not be used in the shuffle and will all finds with None

            # finding all the matches in file data and storing them to later be shuffled
            for file in files:
                try:
                    # goes through all filters needed to mak
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):
                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                        with open(file, 'r') as f:
                            data = f.read()  # stores all the data in a variable

                            for filtered_contain in filtered_contains:
                                # goes through each filtered contain and calls the replace method
                                # allowing for found matches to have a chance of being filtered out, and if now they will be stored and replaced
                                data = re.sub(filtered_contain, replace, data, flags=flags)

                        with open(file, 'w') as f:  # saves changes to file temporarily
                            f.write(data)

                    # even if the file is skipped, it will still need to go through the file
                    # ass it needs to get all the match data and replace it with None, to keep the preshuffle working
                    else:
                        pass

                except Exception as e:
                    Massma.Display.inner.result_error(files, "normal", e)

        # shuffles data inside files
        # PROGRAM IS CURRENTLY PICKY ABOUT LIST SIZES, THEY ALL MUST BE THE SAME
        # SIZES OF PRESET AND PRESHUFFLED MUST BE THE SAME AS FILTERED FILES AND HASH FILES

        if preshuffle:  # preset format on how the files will be shuffled
            # goes through each number in the preshuffle list to determine where an item should go
            # the numbers in the preshuffle set determine the new indexes of elements in a list
            random_matches = [None] * len(filtered_matches)  # sets preset length
            for index, match in zip(preshuffle, filtered_matches):
                random_matches[index] = match

        else:  # normal randomizing of files
            random_matches = filtered_matches.copy()
            random.shuffle(random_matches)

        print(filtered_matches)

        # removes all None values caused by failing the chance file data
        # the none values are used to solve the problem with preshuffles and chances not being in sync
        random_matches = [match for match in random_matches if match is not None]
        filtered_matches = [match for match in filtered_matches if match is not None]  # souly to display changes correctly

    except Exception as e:
        Massma.Display.inner.result_error(len(files), "normal", e)


def group(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, flatten: bool = False, weight: int | list[int] | None = None, presets: str | list[str] | None = None, preshuffle: int | list[int] | None = None, chance_files: float = 1, chance_contains: float = 1, chance_total: float = 1, chance_data: float = 1,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            contains = [contains] if isinstance(contains, str) else contains
            presets = presets if isinstance(presets, list) else ([presets] if presets else [])
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

def scale(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, chance_files: float = 1, chance_total: float = 1,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass

def offset(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, chance_files: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass
