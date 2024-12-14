import os
import shutil

import Buffle.Display.Result
# Methods will not be accessed from this file but from Buffle itself
# These are to be used from the player from the parent folder Buffle and to be use dy other .py files


def dump(source: str, delete: bool = False):
    """
    Moves files from the folder's directory to its parent's directory
    :param source: Target folder's directory / location
    :type source: str
    :param delete: Deletes the target folder's directory / location after dumped
    :type delete: bool
    :return destination
    """
    return move(source, os.path.dirname(source), delete)


def move(source: str, destination: str, delete: bool = False):
    """
    Moves files from one folder or a single file to another folder
    :param source: File's old directory / location
    :type source: str
    :param destination: File's new directory / location
    :type destination: str
    :param delete: Deletes the source folder's directory / location after moved
    :type delete: bool
    :return destination
    """
    if source is os.path.isdir(source):  # multiple files in a folder
        for file in os.scandir(source):
            shutil.move(file, destination)

        os.scandir(source)
        if delete:
            os.remove(source)

    if source is os.path.isfile(source):  # single file in a folder
        shutil.move(source, destination)

    return destination

