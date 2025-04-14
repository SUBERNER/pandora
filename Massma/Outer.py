from Massma import random  # used for seeds
from Massma.Filter import *
import Massma

def normal(files: str | list[str], *, duplicate: bool = False, flatten: bool = False, weight: int | list[int] | None = None, preset: str | list[str] | None = None, preshuffle: list[int] | None = None, chance_files: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            weight = weight if isinstance(weight, list) else ([weight] if weight else [])
            preset = preset if isinstance(preset, list) else ([preset] if preset else [])
            preshuffle = preshuffle if isinstance(preshuffle, list) else ([preshuffle] if preshuffle else [])
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])

            # gets size of the largest path for better result formatting
            Massma.Display.outer.set_source_length(max(files, key=len))

    except Exception as e:
        Massma.Display.outer.result_error(len(files), "normal", e)

def group(files: str | list[str], *, duplicate: bool = False, flatten: bool = False, weight: list[int] | None = None, preset: str | list[str] | None = None, preshuffle: list[int] | None = None, chance_files: float = 1, chance_total: float = 1,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass

def reverse(files: str | list[str], *, duplicate: bool = False, flatten: bool = False, weight: list[int] | None = None, preset: str | list[str] | None = None, preshuffle: list[int] | None = None, chance_files: float = 1, chance_total: float = 1,
            ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass

def rotate(files: str | list[str], *, duplicate: bool = False, flatten: bool = False, weight: list[int] | None = None, preset: str | list[str] | None = None, preshuffle: list[int] | None = None, chance_files: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass

