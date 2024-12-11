"""
Used to color the text and background while displaying results.
The purpose of this is to help keep color consistency between programs using this import, allowing consistent and easy
reading no matter what game is using this import to randomize files
"""
# Used to better communicate how the methods effected files
RED = '\033[31m'  # Marks the original value or trait after change or shuffle
GREEN = '\033[32m'  # Mark the new value or trait after change or shuffle
YELLOW = '\033[33m'  # Mark if value or trait is unchanged

# Used to better communicate the grouping of methods effected files
# Best to pick a unique color for each method or method type
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'

RED_BACKGROUND = ['\033[41m'] # Used to make Errors displayed with result easier to find and more noticeable
RESET = '\033[0m'  # removes all effects

