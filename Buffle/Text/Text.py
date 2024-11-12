import os
import shutil
import random
import re



# used to collect and randomize text inside a multiple files
def multiple(directory: str, find: str):
    replace = '<>TEMP<>'  # text used as a placeholder for replacing text
    datas = []  # stores the data to be randomized later on
    os.chdir(directory)  # changes directory
    files = os.scandir()  # stores the actual files

    # gets data and alters file to prepare for randomizing text
    for file in files:
        if file.is_dir() or file.is_file():
            with open(file, 'r') as r_file:  # opens file
                data = r_file.read()  # stores all the data in a variable
                found = re.findall(find, data)  # stores all strings similar to the find
                if len(found) != 0:
                    for f in found:  # removes data from array in found
                        datas.append(f)

                # rewrites data to be alterable later
                data = re.sub(find, replace, data)

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
                    random_string = random.choice(datas)
                    data = data.replace(replace, random_string, 1)
                    datas.remove(random_string)
                w_file.write(data)


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
def single(file: str, find: str):
    replace = '<>TEMP<>'  # text used as a placeholder for replacing text
    datas = []  # stores the data to be randomized later on

    # gets data and alters file to prepare for randomizing text
    if os.path.isfile(file):
        with open(file, 'r') as r_file:  # opens file
            data = r_file.read()  # stores all the data in a variable
            found = re.findall(find, data)  # stores all strings similar to the find
            if len(found) != 0:
                for f in found:  # removes data from array in found
                    datas.append(f)
            else:
                print(find + " not exist")

            # rewrites data to be alterable later
            data = re.sub(find, replace, data)

        with open(file, 'w') as w_file:
            w_file.write(data)


    # changes the file data and randomizes text
    if os.path.isfile(file):
        with open(file, 'r') as r_file:  # opens file
            data = r_file.read()  # stores all the data in a variable
        with open(file, 'w') as w_file:
            while data.count(replace) > 0:
                random_string = random.choice(datas)
                data = data.replace(replace, random_string, 1)
                datas.remove(random_string)
            w_file.write(data)

