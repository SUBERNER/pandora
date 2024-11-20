import os
import random
import re

import Buffle


# used to collect and randomize text inside a multiple files
def multiple(source: str, contains: str):
    placeholder = '<>TEMP<>'  # text used as a placeholder for replacing text
    original_matches = []
    files = [f for f in os.scandir(source) if f.is_file()]  # stores the actual files

    # gets data from the fills to be shuffled later
    for entry in files:
        with open(entry, 'r') as file:
            text = file.read()  # stores all the data in a variable

        original_matches.extend(re.findall(contains, text))  # dumps all finds in an existing list
        text = re.sub(contains, placeholder, text)  # replaces contains with placeholder in text

        with open(entry, 'w') as file:  # saves changes to file temporarily
            file.write(text)

    files = [f for f in os.scandir(source) if f.is_file()]  # rescans files after changes made to them

    random_matches = original_matches.copy()
    random.shuffle(random_matches)

    # changes the file data and shuffles text
    for entry in files:
        with open(entry, 'r') as file:  # opens file
            text = file.read()  # stores all the data in a variable
        while text.count(placeholder) > 0:
            text = text.replace(placeholder, random_matches[0], 1)
            Buffle.display_text_results.result(source, "Text Shuffle", random_matches[0], original_matches[0])
            random_matches.pop(0)
            original_matches.pop(0)

        with open(entry, 'w') as file:
            file.write(text)


# used to collect and randomize text in groups inside a multiple files
def multiple_group(source: str, contains: list[str]):
    i = 0
    replace = '<>TEMP<>'  # text used as a placeholder for replacing text
    original_matches = []
    files = [f for f in os.scandir(source) if f.is_file()]  # stores the actual files

    # gets data and alters file to prepare for shuffling text
    for entry in files:
        with open(entry, 'r') as file:  # opens file
            text = file.read()  # stores all the data in a variable
            for index, contain in enumerate(contains):
                if len(re.findall(contain, text)) != 0:  # make sure something was found
                    original_matches[index].append(re.findall(contain, text)[0])  # dumps all finds in an existing group inside the list

            # for string in contains:
                # rewrites data to be alterable later
               # data = re.sub(contains[contains.index(string)], replace + "<" + str(contains.index(string)) + ">", data)

        with open(entry, 'w') as file:
            file.write(text)

    files = [f for f in os.scandir(source) if f.is_file()]  # rescans files after changes made to them

    # changes the file data and randomizes text
    for entry in files:
        with open(entry, 'r') as file:  # opens file
            text = file.read()  # stores all the data in a variable

        with open(entry, 'w') as file:
            while data.count(replace) > 0:
                random_strings = random.choice(datas)
                for string in contains:
                    data = data.replace(replace + "<" + str(contains.index(string)) + ">", random_strings[contains.index(string)], 1)
            datas.remove(random_strings)
            w_file.write(data)


# used to collect and randomize text inside a single file
def single(source: str, contains: str):
    placeholder = '<>TEMP<>'  # text used as a placeholder for replacing text
    if os.path.isfile(source):
        with open(source, 'r') as file:
            text = file.read()  # stores all the data in a variable

        original_matches = re.findall(contains, text)
        text = re.sub(contains, placeholder, text)  # replaces contains with placeholder in text

        random_matches = original_matches.copy()
        random.shuffle(random_matches)

        for random_match, original_match in zip(random_matches, original_matches):
            text = text.replace(placeholder, random_match, 1)
            Buffle.display_text_results.result(source, "Text Shuffle", random_match, original_match)

        with open(source, 'w') as file:
            file.write(text)










