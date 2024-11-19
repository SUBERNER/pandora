import os
import random
import re

import Buffle


# used to collect and randomize text inside a multiple files
def multiple(source: str, contains: str):
    print(repr(contains))
    print(contains)
    placeholder = '<>TEMP<>'  # text used as a placeholder for replacing text
    original_matches = []
    files = [f for f in os.scandir(source) if f.is_file()]  # stores the actual files

    # gets data from the fills to be shuffled later
    for entry in files:
        print(entry)
        with open(entry, 'r') as file:
            text = file.read()  # stores all the data in a variable
        print(len(re.findall(contains, text)))
        print(*re.findall(contains, text))
        original_matches.extend(re.findall(contains, text))  # dumps all finds in an existing list
        text = re.sub(contains, placeholder, text)  # replaces contains with placeholder in text
        print("Length of original_matches:", len(original_matches))

        with open(entry, 'w') as file:  # saves changes to file temporarily
            file.write(text)

    files = [f for f in os.scandir(source) if f.is_file()]  # rescans files after changes made to them

    random_matches = original_matches.copy()
    random.shuffle(random_matches)
    print("Length of original_matches:", len(original_matches))
    print("Length of random_matches:", len(random_matches))

    # changes the file data and shuffles text
    for entry in files:
        print(entry)
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
def group(directory: str, find: list[str]):
    i = 0
    replace = '<>TEMP<>'  # text used as a placeholder for replacing text
    datas = []  # stores the data to be randomized later on
    os.chdir(directory)  # changes directory
    files = os.scandir()  # stores the actual files

    # gets data and alters file to prepare for randomizing text
    for file in files:
        if file.is_dir() or file.is_file():
            with open(file, 'r') as r_file:  # opens file
                group = []  # groups together data form a single file together
                data = r_file.read()  # stores all the data in a variable
                for string in find:
                    found = re.findall(string, data)  # stores all strings similar to the find
                    if len(found) != 0:
                        group.append(found[0])
                datas.append(group)

                for string in find:
                    # rewrites data to be alterable later
                    data = re.sub(find[find.index(string)], replace + "<" + str(find.index(string)) + ">", data)

            with open(file, 'w') as w_file:
                w_file.write(data)

    files = os.scandir()  # stores the actual files
    # changes the file data and randomizes text
    for file in files:
        if file.is_dir() or file.is_file():
            with open(file, 'r') as r_file:  # opens file
                data = r_file.read()  # stores all the data in a variable
            with open(file, 'w') as w_file:
                while data.count(replace) > 0:
                    random_strings = random.choice(datas)
                    for string in find:
                        data = data.replace(replace + "<" + str(find.index(string)) + ">", random_strings[find.index(string)], 1)
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










