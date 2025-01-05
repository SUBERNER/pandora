import os
import random
import re

import uuid
import Buffle


# used to collect and randomize text inside a multiple files
def normal(files: str | list[str], contains: str | list[str]):
    # makes files and contains always a list
    if isinstance(files, str):
        files = [files]
    if isinstance(contains, str):
        contains = [contains]

    # gets size of largest path for better result formatting
    Buffle.Display.inner.set_length(max(files, key=len))

    placeholder = f"{uuid.uuid4().hex}"  # text used as a placeholder for replacing text

    # gets data from the fills to be shuffled later
    original_matches = []
    for entry in files:
        with open(entry, 'r') as file:
            text = file.read()  # stores all the data in a variable

        for contain in contains:
            original_matches.extend(re.findall(contain, text))  # dumps all finds in an existing list
            text = re.sub(contain, placeholder, text)  # replaces contains with placeholder in text

        with open(entry, 'w') as file:  # saves changes to file temporarily
            file.write(text)

    random_matches = original_matches.copy()
    random.shuffle(random_matches)

    # changes the file data and shuffles text
    for index, entry in enumerate(files):
        with open(entry, 'r') as file:  # opens file
            text = file.read()  # stores all the data in a variable
        while text.count(placeholder) > 0:
            text = text.replace(placeholder, random_matches[0], 1)
            Buffle.Display.inner.result(files[index], "Normal Text Shuffle", random_matches.pop(0), original_matches.pop(0))

        with open(entry, 'w') as file:
            file.write(text)


# used to collect and randomize text in groups inside a multiple files
def group(source: str, contains: list[str], limit: int=None):
    placeholder = '<>TEMP<>'  # text used as a placeholder for replacing text
    original_matches = []
    files = [f for f in os.scandir(source) if f.is_file()]  # stores the actual files

    # gets data and alters file to prepare for shuffling text
    for entry in files:
        group_matches = [[] for index in contains]  # groups text together to me shuffled together
        valid_group = True  # checks if file should be ignored

        with open(entry, 'r') as file:  # opens file
            text = file.read()  # stores all the data in a variable
            for index, contain in enumerate(contains):
                if len(re.findall(contain, text)) != 0:  # make sure something was found
                    group_matches[index].extend(re.findall(contain, text))  # dumps all finds in an existing group inside the list
                else:
                    valid_group = False
                    break
            if not valid_group:  # if a section in the group is empty, it ignores the rest of the folder
                continue

            # only takes full groups, not those with information missing
            # determines the limit of the amount of groups is made
            group_limit = len(min(group_matches, key=len))  # Find the smallest list length
            if limit != None and limit <= group_limit:
                group_limit = limit
            # trimes all group sections to the length of the smallest section in the group
            group_matches = [group[:group_limit] for group in group_matches]  # Slice each list

            # formats the groups to be shuffled later
            group_format = []
            for group in range(group_limit):
                for contain in range(len(contains)):
                    group_format.append([group_matches[contain][group] for contain in range(len(contains))])
                    print(group_format)
            original_matches.append(group_format)

            for index, contain in enumerate(contains):
                # rewrites data to be alterable later
                text = re.sub(contains[index], placeholder + f"<{index}>", text, group_limit)
        with open(entry, 'w') as file:
            file.write(text)

    files = [f for f in os.scandir(source) if f.is_file()]  # rescans files after changes made to them

    random_matches = original_matches.copy()
    random.shuffle(random_matches)

    # shuffles the groups back into the files
    for entry in files:
        with open(entry, 'r') as file:  # opens file
            text = file.read()  # stores all the data in a variable

            while placeholder in text:
                for index in range(len(contains)):
                    text = text.replace(placeholder + f"<{index}>", random_matches[0][0][index], 1)
                    Buffle.Display.inner.result(source, "Group Text Shuffle", random_matches[0][0][index], original_matches[0][0][index])

                random_matches.pop(0)
                original_matches.pop(0)

        with open(entry, 'w') as file:
            file.write(text)










