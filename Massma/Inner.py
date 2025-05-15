from Massma import random  # used for seeds
from Massma.Filter import *
import Massma

def normal(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, flatten: bool = False, weight: int | list[int] | None = None, presets: str | list[str] | None = None, preshuffle: int | list[int] | None = None, chance_files: float = 1, chance_contains: float = 1, chance_total: float = 1, chance_values: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            contains = [contains] if isinstance(contains, str) else contains
            presets = presets if isinstance(presets, list) else ([presets] if presets else [])
            preshuffle = preshuffle if isinstance(preshuffle, list) else ([preshuffle] if preshuffle else [])
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])
            flags = 0 if flags is None else sum(flags)  # Combine selected flags or default to 0 (no flags)

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.inner.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                        with open(file, 'r') as f:
                            data = f.read()  # stores all the data in a variable

                        for contain in contains:
                            pass

                except Exception as e:
                    Massma.Display.inner.result_error(files, "normal", e)

    except Exception as e:
        Massma.Display.inner.result_error(len(files), "normal", e)

def group(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, flatten: bool = False, weight: int | list[int] | None = None, presets: str | list[str] | None = None, preshuffle: int | list[int] | None = None, chance_files: float = 1, chance_contains: float = 1, chance_total: float = 1, chance_values: float = 1,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            contains = [contains] if isinstance(contains, str) else contains
            presets = presets if isinstance(presets, list) else ([presets] if presets else [])
            preshuffle = preshuffle if isinstance(preshuffle, list) else ([preshuffle] if preshuffle else [])
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])
            flags = 0 if flags is None else sum(flags)  # Combine selected flags or default to 0 (no flags)

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.inner.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                        with open(file, 'r') as f:
                            data = f.read()  # stores all the data in a variable

                        for contain in contains:
                            pass

                except Exception as e:
                    Massma.Display.inner.result_error(files, "group", e)

    except Exception as e:
        Massma.Display.inner.result_error(len(files), "group", e)

def scale(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, chance_files: float = 1, chance_total: float = 1,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass

def offset(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, chance_files: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass