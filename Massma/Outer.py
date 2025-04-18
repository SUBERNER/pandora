from Massma import random  # used for seeds
from Massma.Filter import *
import Massma

def normal(files: str | list[str], *, preset: str | list[str] | None = None, preshuffle: list[int] | None = None, chance_files: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            preset = preset if isinstance(preset, list) else ([preset] if preset else [])
            preshuffle = preshuffle if isinstance(preshuffle, list) else ([preshuffle] if preshuffle else [])
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])

            # gets size of the largest path for better result formatting
            Massma.Display.outer.set_source_length(max(files, key=len))

            hash_files = []  # stores all files in their hash format
            filtered_files = []  # stores all files after chances and filters

            # renames files to avoid conflict
            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # generates temporary hash name for the file
                        hash_name = f"{hash(file)}{os.path.splitext(os.path.basename(file))[1]}"  # generates unique name for file
                        hash_file = os.path.join(os.path.dirname(file), hash_name)  # creates a path for the file

                        # adds both to lists
                        hash_files.append(hash_file)
                        filtered_files.append(file)

                except Exception as e:
                    Massma.Display.outer.result_error(file, "normal", e)


            # shuffles files
            if preset:  # preset list of files being shuffled instead of the ones originally used
                pass
            else:
                if preshuffle :  # preset format on how the files will be shuffled
                    pass
                else:  # normal randomizing of files
                    random_files = filtered_files.copy()
                    random.shuffle(random_files)

            # alters files
            for hash_file, new_file, original_file in zip(hash_files, random_files, filtered_files):
                os.rename(os.path.abspath(hash_file), os.path.abspath(new_file)) # renames file
                Massma.Display.outer.result(os.path.abspath(original_file), "normal",os.path.basename(original_file), os.path.basename(new_file)) # displays changed


    except Exception as e:
        Massma.Display.outer.result_error(len(files), "normal", e)

def group(files: str | list[str], *, preset: str | list[str] | None = None, preshuffle: list[int] | None = None, chance_files: float = 1, chance_total: float = 1,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass

def reverse(files: str | list[str], *, preset: str | list[str] | None = None, preshuffle: list[int] | None = None, chance_files: float = 1, chance_total: float = 1,
            ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass

def rotate(files: str | list[str], *, preset: str | list[str] | None = None, preshuffle: list[int] | None = None, chance_files: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass

