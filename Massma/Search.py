from Massma import random  # used for seeds
from Massma.Filter import *
import Massma
import os


def full(source: str, *, deep_search: bool = False, inverse_search: bool = False, chance_files: float = 1, chance_folders: float = 1,
         ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None) -> list[str]:
    try:
        files = []  # will store all files found in this search

        if not inverse_search:  # ignores everything but the source if an inverse_search
            files.extend([f.path for f in os.scandir(source) if f.is_file()])  # gets all files inside source directory

        if deep_search:  # if enabled, will also go through all subfolders inside source
            folders = [f[0] for f in os.walk(source)]  # get all subfolders inside source
            for folder in folders:  # goes through each folder
                if chance_folders >= random.random():  # test chances to see if a folder will be seached
                    if folder == source:  # skips source folder, as it is already scanned in the first if
                        continue
                    files.extend([f.path for f in os.scandir(folder) if f.is_file()])  # gets all files inside source directory

        for file in files:   # test chances to see if files will stay in list
            if chance_files <= random.random():
                files.remove(file)

        Massma.Display.search.result(source, "full", 0, len(files))
        return files  # returns all files in a list
    except Exception as e:
        Massma.Display.audio.error_result(source, "full", e)
        return []


def name(source: str) -> list[str]:
    try:
        files = []  # will store all files found in this search

        Massma.Display.search.result(source, "name", len(files), 0)
        return files  # returns all files in a list
    except Exception as e:
        Massma.Display.audio.error_result(source, "name", e)
        return []


def content(source: str) -> list[str]:
    try:
        files = []  # will store all files found in this search

        Massma.Display.search.result(source, "content", len(files), 0)
        return files  # returns all files in a list
    except Exception as e:
        Massma.Display.audio.error_result(source, "content", e)
        return []