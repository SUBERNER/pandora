from Massma import random  # used for seeds
from Massma.Filter import *
import Massma

def normal(files: str | list[str], *, preshuffle: list[int] | None = None, chance_files: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            preshuffle = preshuffle if isinstance(preshuffle, list) else ([preshuffle] if preshuffle else [])
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.outer.set_source_length(max(file_paths, key=len))

            hash_files = []  # stores all files in their hash format
            filtered_files = []  # stores all files after chances and filters

            # renames files to avoid conflict
            for index, file in enumerate(files):
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                        # generates temporary hash name for the file
                        hash_name = f"{hash(file)}{os.path.splitext(os.path.basename(file))[1]}"  # generates unique name for file
                        hash_file = os.path.join(os.path.dirname(file), hash_name)  # creates a path for the file
                        os.rename(os.path.abspath(file), hash_file)  # changes file name to hash name
                        # adds both to lists
                        hash_files.append(hash_file)
                        filtered_files.append(file)  # stores file names being used

                    else:  # runs when it fails the chance files, adding empty value to keep order and structure to the preshuffle
                        filtered_files.append(None)  # notify system that file name will not be used in the shuffle

                except Exception as e:
                    Massma.Display.outer.result_error(file, "normal", e)

            # shuffles files
            # PROGRAM IS CURRENTLY PICKY ABOUT LIST SIZES, THEY ALL MUST BE THE SAME
            # SIZES OF PRESHUFFLED MUST BE THE SAME AS FILTERED FILES AND HASH FILES

            if preshuffle:  # preshuffle format on how the files will be shuffled
                # goes through each number in the preshuffle list to determine where an item should go
                # the numbers in the preshuffle set determine the new indexes of elements in a list
                random_files = [None] * len(filtered_files)  # sets preshuffle length
                for index, file in zip(preshuffle, filtered_files):
                    random_files[index] = file

            else:  # normal randomizing of files
                random_files = filtered_files.copy()
                random.shuffle(random_files)

            # removes all None values caused by failing the chance files
            # the none values are used to solve the problem with preshuffles and chances not being in sync
            random_files = [file for file in random_files if file is not None]
            filtered_files = [file for file in filtered_files if file is not None] # souly to display changes correctly

            # alters files
            for hash_file, new_file, original_file in zip(hash_files, random_files, filtered_files):
                os.rename(os.path.abspath(hash_file), os.path.abspath(new_file))  # renames file
                Massma.Display.outer.result(os.path.abspath(original_file), "normal", os.path.basename(original_file), os.path.basename(new_file)) # displays changed

    except Exception as e:
        Massma.Display.outer.result_error(len(files), "normal", e)

def group(files: str | list[str], contains: str | list[str], *, preshuffle: list[int] | None = None, chance_files: float = 1, chance_contains: float = 1, chance_total: float = 1,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            contains = [contains] if isinstance(contains, str) else contains
            preshuffle = preshuffle if isinstance(preshuffle, list) else ([preshuffle] if preshuffle else [])
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])
            flags = 0 if flags is None else sum(flags)  # Combine selected flags or default to 0 (no flags)

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.outer.set_source_length(max(file_paths, key=len))

            hash_contains = []  # stores all contains in their hash format
            hash_files = []  # stores all files in their hash format
            filtered_files = []  # stores all files after chances and filters
            filtered_contains = []  # stores all contains that will be used in the shuffle

            # determines if contain will be used
            for index, contain in enumerate(contains):
                if chance_contains >= random.random():  # test if a contain will even be used
                    hash_contains.append(str(hash(contain)))  # converts hash into a string
                    filtered_contains.append(contain)  # stores contains being used
                else: # runs when it fails the chance contains, adding empty value to keep order and structure to the preshuffle
                    filtered_contains.append(None) # notify system that contain will not be used in the shuffle

            # goes though each file and chancing contains found with temporary values
            # renames files to avoid conflict
            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                        # this for loop will temporary skip all nopes
                        for index, contain in enumerate([contain for contain in filtered_contains if contain is not None]): # goes though each contain
                            if re.search(contain, os.path.basename(file), flags=flags):  # used regex
                                # the re.sub uses regex, be careful with how you enter strings
                                hash_name = re.sub(contain, hash_contains[index], os.path.basename(file), flags=flags)  # new name for the file
                                hash_file = os.path.join(os.path.dirname(file), hash_name) # creates the full file name with the hash
                                os.rename(os.path.abspath(file), hash_file)  # changes file name to hash name

                                # adds both to lists
                                hash_files.append(hash_file)
                                filtered_files.append(file)

                except Exception as e:
                    Massma.Display.outer.result_error(file, "group", e)

            # shuffles files
            # PROGRAM IS CURRENTLY PICKY ABOUT LIST SIZES, THEY ALL MUST BE THE SAME
            # SIZES OF PRESHUFFLED MUST BE THE SAME AS FILTERED FILES AND HASH FILES
            if preshuffle:  # preshuffle format on how the files will be shuffled
                # goes through each number in the preshuffle list to determine where an item should go
                # the numbers in the preshuffle set determine the new indexes of elements in a list
                random_contains = [0] * len(filtered_contains)  # sets preshuffle length
                for index, file in zip(preshuffle, filtered_contains):
                    random_contains[index] = file

            else:  # normal randomizing of files
                random_contains = filtered_contains.copy()
                random.shuffle(random_contains)

            # removes all None values caused by failing the chance contains
            # the none values are used to solve the problem with preshuffles and chances not being in sync
            random_contains = [contain for contain in random_contains if contain is not None]

            # CANNOT HAVE 2 DIFFERENT HASHES IN ONE FILE NAME
            # alters file group names
            for hash_file, original_file in zip(hash_files, filtered_files):
                for hash_contain, random_contain, filtered_contain in zip(hash_contains, random_contains, filtered_contains):  # tests each contain on a file and inserts the correct one based on the hash
                    if hash_contain in hash_file:  # finding the correct group
                        new_name = os.path.basename(hash_file).replace(hash_contain, random_contain)
                        os.rename(os.path.abspath(hash_file), os.path.abspath(os.path.join(os.path.dirname(hash_file), new_name)))  # renames file
                        Massma.Display.outer.result(os.path.abspath(original_file), "group", os.path.basename(original_file), new_name)  # displays changed

    except Exception as e:
        Massma.Display.outer.result_error(len(files), "group", e)

