from Massma import random  # used for seeds
from Massma.Filter import *
import Massma
import os


def full(source: str, *, deep_search: bool = False, chance_files: float = 1, chance_folders: float = 1, chance_total: float = 1,
         ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None) -> list[str]:
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
                if (chance_files > random.random() and  # random change to be added or removed by filters
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
         logic: Logic = Logic.AND, ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None) -> list[str]:
    try:
        files = []  # will store all files found in this search
        filtered_files = []  # will store all files after chances and filters
        if chance_total >= random.random():  # test if method will happen
            # formats all filter correctly into lists
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])
            contains = [contains] if isinstance(contains, str) else contains

            if logic == Logic.AND:
                files.extend([f.path for f in os.scandir(source) if f.is_file() and all(re.search(contain, f.name) for contain in contains)])  # all patterns must match
            elif logic == Logic.OR:
                files.extend([f.path for f in os.scandir(source) if f.is_file() and any(re.search(contain, f.name) for contain in contains)])  # at least one must match
            elif logic == Logic.NAND:
                files.extend([f.path for f in os.scandir(source) if f.is_file() and not all(re.search(contain, f.name) for contain in contains)])  # opposite of AND
            elif logic == Logic.NOR:
                files.extend([f.path for f in os.scandir(source) if f.is_file() and not any(re.search(contain, f.name) for contain in contains)])  # opposite of OR
            elif logic == Logic.XOR:
                files.extend([f.path for f in os.scandir(source) if f.is_file() and sum(bool(re.search(contain, f.name)) for contain in contains) == 1])  # exactly one match
            elif logic == Logic.XNOR:
                files.extend([f.path for f in os.scandir(source) if f.is_file() and sum(bool(re.search(contain, f.name)) for contain in contains) != 1])  # opposite of XOR

            if deep_search:  # if enabled, will also go through all subfolders inside source
                folders = [f[0] for f in os.walk(source)]  # get all subfolders inside source
                for folder in folders:  # goes through each folder
                    if chance_folders >= random.random():  # test chances to see if a folder will be searched
                        if folder == source:  # skips source folder, as it is already scanned in the first if
                            continue
                        if logic == Logic.AND:
                            files.extend([f.path for f in os.scandir(folder) if f.is_file() and all(re.search(contain, f.name) for contain in contains)])  # all patterns must match
                        elif logic == Logic.OR:
                            files.extend([f.path for f in os.scandir(folder) if f.is_file() and any(re.search(contain, f.name) for contain in contains)])  # at least one must match
                        elif logic == Logic.NAND:
                            files.extend([f.path for f in os.scandir(folder) if f.is_file() and not all(re.search(contain, f.name) for contain in contains)])  # opposite of AND
                        elif logic == Logic.NOR:
                            files.extend([f.path for f in os.scandir(folder) if f.is_file() and not any(re.search(contain, f.name) for contain in contains)])  # opposite of OR
                        elif logic == Logic.XOR:
                            files.extend([f.path for f in os.scandir(folder) if f.is_file() and sum(bool(re.search(contain, f.name)) for contain in contains) == 1])  # exactly one match
                        elif logic == Logic.XNOR:
                            files.extend([f.path for f in os.scandir(folder) if f.is_file() and sum(bool(re.search(contain, f.name)) for contain in contains) != 1])  # opposite of XOR

            # determines what files should be altered or removed from search
            for file in files:  # test chances to see if files will stay in a list
                if (chance_files > random.random() and  # random change to be added or removed by filters
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
            logic: Logic = Logic.AND, ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None) -> list[str]:
    try:
        files = []  # will store all files found in this search
        filtered_files = []  # will store all files after chances and filters
        if chance_total >= random.random():  # test if method will happen
            # formats all filter correctly into lists
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])
            contains = [contains] if isinstance(contains, str) else contains

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
                    if ((logic == Logic.AND and all(re.search(contain, text) for contain in contains))  # all patterns must match
                    or (logic == Logic.OR and any(re.search(contain, text) for contain in contains))  # at least one must match
                    or (logic == Logic.NAND and not all(re.search(contain, text) for contain in contains))   # opposite of AND
                    or (logic == Logic.NOR and not any(re.search(contain, text) for contain in contains))   # opposite of OR
                    or (logic == Logic.XOR and sum(bool(re.search(contain, f.name)) for contain in contains) == 1)  # exactly one match
                    or (logic == Logic.XNOR and sum(bool(re.search(contain, f.name)) for contain in contains) != 1)):  # opposite of XOR

                        # if any of the logics work, it will alter and determine if it will be added to searched files
                        if (chance_files > random.random() and  # random change to be added or removed by filters
                                not (any(ignore(file) for ignore in ignores)) and
                                not (any(exclude(file) for exclude in excludes))):

                            # changed files as needed
                            for alter in alters:
                                alter(file)

                            filtered_files.append(file)

        Massma.Display.search.result(source, "content", 0, len(filtered_files))
        return filtered_files  # returns all files in a list
    except Exception as e:
        Massma.Display.search.result_error(source, "content", e)
        return []