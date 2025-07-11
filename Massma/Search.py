from Massma import random  # used for seeds
from Massma.Filter import *
import Massma
import os


def full(source: str, *, deep_search: bool = False, chance_files: float = 1, chance_folders: float = 1, chance_total: float = 1,
         ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None) -> list[str]:
    """
    Searches for all files within a directory.

    Parameters:
        source (str): The directory to search.

        deep_search (bool): If True, searches subdirectories as well. Defaults to False.

        chance_files (float): Probability (0-1) of each file being included. Defaults to 1.

        chance_folders (float): Probability (0-1) of searching each folder. Defaults to 1.

        chance_total (float): Probability (0-1) of the method executing. Defaults to 1.

        ignores (Ignore | list[Ignore] | None): Filters out specific files. Defaults to None.

        excludes (Exclude | list[Exclude] | None): Excludes files based on content. Defaults to None.

        alters (Alter | list[Alter] | None): Modifies files if found. Defaults to None.

    Returns:
        list[str]: A list of file paths matching the search criteria.
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
       Searches for files by name within a directory.

       Parameters:
           source (str): The directory to search.

           contains (str | list[str]): Substrings or patterns to match in file names.

           deep_search (bool): If True, searches subdirectories as well. Defaults to False.

           chance_files (float): Probability (0-1) of each file being included. Defaults to 1.

           chance_folders (float): Probability (0-1) of searching each folder. Defaults to 1.

           chance_total (float): Probability (0-1) of the method executing. Defaults to 1.

           logic (Logic): Logic rule for matching patterns (AND, OR, etc.). Defaults to Logic.AND.

           ignores (Ignore | list[Ignore] | None): Filters out specific files. Defaults to None.

           excludes (Exclude | list[Exclude] | None): Excludes files based on content. Defaults to None.

           alters (Alter | list[Alter] | None): Modifies files if found. Defaults to None.

           flags (list[re.RegexFlag]): List of `re` module flags to apply during regex matching.
            - re.A: ASCII-only matching.
            - re.I: Ignore case.
            - re.L: Locale dependent.
            - re.M: Multi-line mode.
            - re.S: Dot matches all (dotall).
            - re.U: Unicode matching.
            - re.X: Verbose (allow comments and whitespace).
            - Defaults to None (no flags).

       Returns:
           list[str]: A list of file paths matching the search criteria.
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
    Searches for files within a directory that contain specified substrings.

    Parameters:
        source (str): The root directory to begin the search.

        contains (str | list[str]): The substring(s) to search for in file content.

        deep_search (bool, optional): If True, searches subdirectories recursively. Defaults to False.

        chance_files (float, optional): Probability (0 to 1) of including a file in results. Defaults to 1.

        chance_folders (float, optional): Probability (0 to 1) of searching inside a folder. Defaults to 1.

        chance_total (float, optional): Probability (0 to 1) that the entire function runs. Defaults to 1.

        logic (Logic, optional): Defines how multiple substrings should be evaluated (AND, OR, etc.). Defaults to Logic.AND.

        ignores (Ignore | list[Ignore] | None, optional): List of Ignore filters to exclude specific files. Defaults to None.

        excludes (Exclude | list[Exclude] | None, optional): List of Exclude filters for conditional exclusion. Defaults to None.

        alters (Alter | list[Alter] | None, optional): List of Alter operations to modify file content. Defaults to None.

        flags (list[re.RegexFlag]): List of `re` module flags to apply during regex matching.
            - re.A: ASCII-only matching.
            - re.I: Ignore case.
            - re.L: Locale dependent.
            - re.M: Multi-line mode.
            - re.S: Dot matches all (dotall).
            - re.U: Unicode matching.
            - re.X: Verbose (allow comments and whitespace).
            - Defaults to None (no flags).

    Returns:
        list[str]: A list of file paths matching the search criteria.
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

        # gets size of the largest path for better result formatting
        file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
        Massma.Display.inner.set_source_length(max(file_paths, key=len))

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

        # gets size total files for better result formatting
        Massma.Display.search.set_source_length(0)

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



