from Massma import random  # used for seeds
from Massma.Filter import *
import Massma
import os


def full(source: str, *, deep_search: bool = False, chance_files: float = 1, chance_folders: float = 1, chance_total: float = 1,
         ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None) -> list[str]:
    """
    Searches and returns all files found within a directory

    Parameters:
        source (str): The directory of selected files to be searched
        deep_search (bool): Allows for also searching inside folders within the selected source directory, defaults to
        chance_files (float): Probability between 0 (0%) and 1 (100%) of each file being selected, defaults to 1
        chance_total (float): Probability between 0 (0%) and 1 (100%) of any files being selected, defaults to 1
        chance_folder (float): Probability between 0 (0%) and 1 (100%) of each folder being selected, defaults to 1
        ignores (Filter.Ignore|list[Filter.Ignore]): Filter object(s) that skips files from being selected based on file directory, defaults to None
        excludes (Filter.Exclude|list[Filter.Exclude]): Filter object(s) that skips files from being selected based on file data, defaults to None
        alters (Filter.Alter|list[Filter.Alter]): Filter object(s) that alter files data based on existing file data, defaults to None
    
    Returns:
        list[str]: file paths matching the search pattern
    """
    try:
        files = []  # will store all files found in this search
        filtered_files = []  # will store all files after chances and filters
        if chance_total >= random.random():  # test if method will happen
            # formats all filter correctly into lists
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])

            files.extend([f.path for f in os.scandir(source) if f.is_file()])  # gets all files inside source directory

            if deep_search:  # if enabled, will also go through all subfolders inside source
                folders = [f[0] for f in os.walk(source)]  # get all subfolders inside source
                for folder in folders:  # goes through each folder
                    if chance_folders >= random.random():  # test chances to see if a folder will be searched
                        if folder == source:  # skips source folder, as it is already scanned in the first if
                            continue
                        files.extend([f.path for f in os.scandir(folder) if f.is_file()])  # gets all files inside source directory

            # determines what files should be altered or removed from search
            for file in files:  # test chances to see if files will stay in a list
                if (chance_files >= random.random() and  # random change to be added or removed by filters
                        not (any(ignore(file) for ignore in ignores)) and
                        not (any(exclude(file) for exclude in excludes))):

                    # changed files as needed
                    for alter in alters:
                        alter(file)

                    filtered_files.append(file)

        Massma.Display.search.result(source, "full", 0, len(filtered_files))
        return filtered_files  # returns all files in a list
    except Exception as e:
        Massma.Display.search.result_error(source, "full", e)
        return []


def name(source: str, contains: str | list[str], *, deep_search: bool = False, chance_files: float = 1, chance_folders: float = 1, chance_total: float = 1,
         logic: Logic = Logic.AND, ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None) -> list[str]:
    """
    Searches and returns files found within a directory based on file name

    Parameters:
        source (str): The directory of selected files to be searched
        contains (str|list[str]): Substring(s) used for selecting files by matching text in file names
        deep_search (bool): Allows for also searching inside folders within the selected source directory, defaults to
        chance_files (float): Probability between 0 (0%) and 1 (100%) of each file being selected, defaults to 1
        chance_total (float): Probability between 0 (0%) and 1 (100%) of any files being selected, defaults to 1
        chance_folder (float): Probability between 0 (0%) and 1 (100%) of each folder being selected, defaults to 1
        logic (Logic): BIG WORDS, defaults to Logic.AND
        ignores (Filter.Ignore|list[Filter.Ignore]): Filter object(s) that skips files from being selected based on file directory, defaults to None
        excludes (Filter.Exclude|list[Filter.Exclude]): Filter object(s) that skips files from being selected based on file data, defaults to None
        alters (Filter.Alter|list[Filter.Alter]): Filter object(s) that alter files data based on existing file data, defaults to None
        flags (list[re.RegexFlag]):

    Returns:
        list[str]: file paths matching the search pattern

    Notes:
        contains use BIG WORDS (re/Regex)
        logic patterns:
        - Logic.AND: All contains must match
        - Logic.NAND: Opposite of AND
        - Logic.OR: At least one must match
        - Logic.NOR: Opposite of OR
        - Logic.XOR: Exactly one match
        - Logic.XNOR: opposite of XOR
        BIG WORDS (re/Regex) flags:
        - re.A: ASCII-only matching
        - re.I: Ignore case
        - re.L: Locale dependent
        - re.M: Multi-line mode
        - re.S: Dot matches all
        - re.U: Unicode matching.
        - re.X: Verbose

    """
    try:
        files = []  # will store all files found in this search
        filtered_files = []  # will store all files after chances and filters
        if chance_total >= random.random():  # test if method will happen
            # formats all filter correctly into lists
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])
            contains = [contains] if isinstance(contains, str) else contains
            flags = 0 if flags is None else sum(flags)  # Combine selected flags or default to 0 (no flags)

            if logic == Logic.AND:
                files.extend([f.path for f in os.scandir(source) if f.is_file() and all(re.search(contain, f.name, flags=flags) for contain in contains)])  # all patterns must match
            elif logic == Logic.OR:
                files.extend([f.path for f in os.scandir(source) if f.is_file() and any(re.search(contain, f.name, flags=flags) for contain in contains)])  # at least one must match
            elif logic == Logic.NAND:
                files.extend([f.path for f in os.scandir(source) if f.is_file() and not all(re.search(contain, f.name, flags=flags) for contain in contains)])  # opposite of AND
            elif logic == Logic.NOR:
                files.extend([f.path for f in os.scandir(source) if f.is_file() and not any(re.search(contain, f.name, flags=flags) for contain in contains)])  # opposite of OR
            elif logic == Logic.XOR:
                files.extend([f.path for f in os.scandir(source) if f.is_file() and sum(bool(re.search(contain, f.name, flags=flags)) for contain in contains) == 1])  # exactly one match
            elif logic == Logic.XNOR:
                files.extend([f.path for f in os.scandir(source) if f.is_file() and sum(bool(re.search(contain, f.name, flags=flags)) for contain in contains) != 1])  # opposite of XOR

            if deep_search:  # if enabled, will also go through all subfolders inside source
                folders = [f[0] for f in os.walk(source)]  # get all subfolders inside source
                for folder in folders:  # goes through each folder
                    if chance_folders >= random.random():  # test chances to see if a folder will be searched
                        if folder == source:  # skips source folder, as it is already scanned in the first if
                            continue
                        if logic == Logic.AND:
                            files.extend([f.path for f in os.scandir(folder) if f.is_file() and all(re.search(contain, f.name, flags=flags) for contain in contains)])  # all patterns must match
                        elif logic == Logic.OR:
                            files.extend([f.path for f in os.scandir(folder) if f.is_file() and any(re.search(contain, f.name, flags=flags) for contain in contains)])  # at least one must match
                        elif logic == Logic.NAND:
                            files.extend([f.path for f in os.scandir(folder) if f.is_file() and not all(re.search(contain, f.name, flags=flags) for contain in contains)])  # opposite of AND
                        elif logic == Logic.NOR:
                            files.extend([f.path for f in os.scandir(folder) if f.is_file() and not any(re.search(contain, f.name, flags=flags) for contain in contains)])  # opposite of OR
                        elif logic == Logic.XOR:
                            files.extend([f.path for f in os.scandir(folder) if f.is_file() and sum(bool(re.search(contain, f.name, flags=flags)) for contain in contains) == 1])  # exactly one match
                        elif logic == Logic.XNOR:
                            files.extend([f.path for f in os.scandir(folder) if f.is_file() and sum(bool(re.search(contain, f.name, flags=flags)) for contain in contains) != 1])  # opposite of XOR

            # determines what files should be altered or removed from search
            for file in files:  # test chances to see if files will stay in a list
                if (chance_files >= random.random() and  # random change to be added or removed by filters
                        not (any(ignore(file) for ignore in ignores)) and
                        not (any(exclude(file) for exclude in excludes))):

                    # changed files as needed
                    for alter in alters:
                        alter(file)

                    filtered_files.append(file)

        Massma.Display.search.result(source, "name", 0, len(filtered_files))
        return filtered_files  # returns all files in a list
    except Exception as e:
        Massma.Display.search.result_error(source, "name", e)
        return []


def content(source: str, contains: str | list[str], *, deep_search: bool = False, chance_files: float = 1, chance_folders: float = 1, chance_total: float = 1,
            logic: Logic = Logic.AND, ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None) -> list[str]:
    """
    Searches and returns files found within a directory based on data inside files

    Parameters:
        source (str): The directory of selected files to be searched
        contains (str|list[str]): Substring(s) used for selecting files by matching text inside files
        deep_search (bool): Allows for also searching inside folders within the selected source directory, defaults to
        chance_files (float): Probability between 0 (0%) and 1 (100%) of each file being selected, defaults to 1
        chance_total (float): Probability between 0 (0%) and 1 (100%) of any files being selected, defaults to 1
        chance_folder (float): Probability between 0 (0%) and 1 (100%) of each folder being selected, defaults to 1
        logic (Logic): BIG WORDS, defaults to Logic.AND
        ignores (Filter.Ignore|list[Filter.Ignore]): Filter object(s) that skips files from being selected based on file directory, defaults to None
        excludes (Filter.Exclude|list[Filter.Exclude]): Filter object(s) that skips files from being selected based on file data, defaults to None
        alters (Filter.Alter|list[Filter.Alter]): Filter object(s) that alter files data based on existing file data, defaults to None
        flags (list[re.RegexFlag]): BIG WORDS, defaults to None

        Returns:
            list[str]: file paths matching the search pattern

        Notes:
            contains use BIG WORDS (re/Regex)
            logic patterns:
            - Logic.AND: All contains must match
            - Logic.NAND: Opposite of AND
            - Logic.OR: At least one must match
            - Logic.NOR: Opposite of OR
            - Logic.XOR: Exactly one match
            - Logic.XNOR: opposite of XOR
            BIG WORDS (re/Regex) flags:
            - re.A: ASCII-only matching
            - re.I: Ignore case
            - re.L: Locale dependent
            - re.M: Multi-line mode
            - re.S: Dot matches all
            - re.U: Unicode matching.
            - re.X: Verbose
        """
    try:
        files = []  # will store all files found in this search
        filtered_files = []  # will store all files after chances and filters
        if chance_total >= random.random():  # test if method will happen
            # formats all filter correctly into lists
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])
            contains = [contains] if isinstance(contains, str) else contains
            flags = 0 if flags is None else sum(flags)  # Combine selected flags or default to 0 (no flags)

            files.extend([f.path for f in os.scandir(source) if f.is_file()])  # gets all files inside source directory

            if deep_search:  # if enabled, will also go through all subfolders inside source
                folders = [f[0] for f in os.walk(source)]  # get all subfolders inside source
                for folder in folders:  # goes through each folder
                    if chance_folders >= random.random():  # test chances to see if a folder will be searched
                        if folder == source:  # skips source folder, as it is already scanned in the first if
                            continue
                        files.extend([f.path for f in os.scandir(folder) if f.is_file()])  # gets all files inside source directory

            # determines what files should be altered or removed from search
            # determines if substring is or is not inside file
            for file in files:  # test chances to see if files will stay in a list
                with open(file, 'r') as f:
                    text = f.read()
                    if ((logic == Logic.AND and all(re.search(contain, text, flags=flags) for contain in contains))  # all patterns must match
                    or (logic == Logic.OR and any(re.search(contain, text, flags=flags) for contain in contains))  # at least one must match
                    or (logic == Logic.NAND and not all(re.search(contain, text, flags=flags) for contain in contains))   # opposite of AND
                    or (logic == Logic.NOR and not any(re.search(contain, text, flags=flags) for contain in contains))   # opposite of OR
                    or (logic == Logic.XOR and sum(bool(re.search(contain, f.name, flags=flags)) for contain in contains) == 1)  # exactly one match
                    or (logic == Logic.XNOR and sum(bool(re.search(contain, f.name, flags=flags)) for contain in contains) != 1)):  # opposite of XOR

                        # if any of the logics work, it will alter and determine if it will be added to searched files
                        if (chance_files >= random.random() and  # random change to be added or removed by filters
                                not (any(ignore(file) for ignore in ignores)) and
                                not (any(exclude(file) for exclude in excludes))):

                            # changed files as needed
                            for alter in alters:
                                alter(file)

                            # beginning source is simply how many files it went through
                            filtered_files.append(len(file))

        Massma.Display.search.result(source, "content", 0, len(filtered_files))
        return filtered_files  # returns all files in a list
    except Exception as e:
        Massma.Display.search.result_error(source, "content", e)
        return []


def inner(files: str | list[str], grouping: bool, *, contains: str | list[str] | None = None,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, flags: list[re.RegexFlag] = None) -> list[str]:
    try:
        # makes data always a list
        files = [files] if isinstance(files, str) else files
        contains = [contains] if isinstance(contains, str) else contains
        ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
        excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
        flags = 0 if flags is None else sum(flags)  # Combine selected flags or default to 0 (no flags)

        filtered_contains = []  # stores all the contains that will be used
        filtered_matches = []  # stores all the matches that will be shuffled and used

        if grouping:  # used to get data from inner group like method
            # finding all the matches in file data and storing them to later be shuffled
            for file in files:
                try:
                    # goes through all filters needed to make
                    if not (any(ignore(file) for ignore in ignores)) and not (any(exclude(file) for exclude in excludes)): # could filter out files
                        with open(file, 'r') as f:
                            data = f.read()  # stores all the data in a variable

                            # used for replacing and chance filtering out matches
                            # group(0) only grabs first match found
                            def replace(match):
                                filtered_matches.append(match.group(0))
                                return match.group(0)  # does not replace data with hash

                            # goes throw each contain for a file to find matches
                            for filtered_contain, contain in zip(filtered_contains, contains):
                                # allowing for found matches to have a chance of being filtered out, and if now they will be stored and replaced
                                data = re.sub(filtered_contain, replace, data, flags=flags)

                except Exception as e:
                    Massma.Display.inner.result_error(file, "inner", e)
        else:  # used to get data from inner normal like method
            pass

    except Exception as e:
        print(e)
        Massma.Display.inner.result_error(len(files), "inner", e)


# YES, I do understand that outer search method is absolutely useless, has no value, and are just worse version of other searches,
# however, I am petty and like order, if there is going to be an inner search then there is going to be an outer search
def outer(files: str | list[str], grouping: bool, *, contains: str | list[str] | None = None,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None) -> list[str]:
    try:
        # makes data always a list
        files = [files] if isinstance(files, str) else files
        contains = [contains] if isinstance(contains, str) else contains
        ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
        excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])

        filtered_data = []  # stores all files or contains after and filters

        if grouping: # used to get data from outer group like method
            #  goes through each file checking if they pass the filters and storing them to be returned to user
            for contain in contains:
                try:
                    filtered_data.append(contain)  # stores contains to data being sent back

                except Exception as e:
                    Massma.Display.search.result_error(len(files), "outer", e)
                    return []  # returns an empty list

        else:  # used to get data from outer normal like method
            #  goes through each file checking if they pass the filters and storing them to be returned to user
            for file in files:
                try:
                    if (not (any(ignore(file) for ignore in ignores))
                       and not (any(exclude(file) for exclude in excludes))):  # change to be filtered

                        # adds file to list
                        filtered_data.append(file)  # stores file names being used

                except Exception as e:
                    Massma.Display.search.result_error(file, "outer", e)
                    return []  # returns an empty list


        # displays and the returns list after finding all the data
        Massma.Display.search.result(len(files), "outer", 0, len(filtered_data))
        return filtered_data  # returns a list of all data that was found and would have been altered

    except Exception as e:
        Massma.Display.search.result_error(len(files), "outer", e)
        return []  # returns an empty list



