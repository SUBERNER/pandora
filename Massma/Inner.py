from Massma import random  # used for seeds
from Massma.Filter import *
import Massma

def normal(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, flatten: bool = False, weight: int | list[int] | None = None, preset: str | list[str] | None = None, preshuffle: int | list[int] | None = None, chance_file: float = 1, chance_total: float = 1, chance_value: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass

def group(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, flatten: bool = False, weight: int | list[int] | None = None, preset: str | list[str] | None = None, preshuffle: int | list[int] | None = None, chance_file: float = 1, chance_total: float = 1, chance_value: float = 1,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass

def reverse(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, flatten: bool = False, weight: int | list[int] | None = None, preset: str | list[str] | None = None, preshuffle: int | list[int] | None = None, chance_file: float = 1, chance_total: float = 1, chance_value: float = 1,
            ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass

def rotate(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, flatten: bool = False, weight: int | list[int] | None = None, preset: str | list[str] | None = None, preshuffle: int | list[int] | None = None, chance_file: float = 1, chance_total: float = 1, chance_value: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass

def scale(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, chance_files: float = 1, chance_total: float = 1,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass

def offset(files: str | list[str], contains: str | list[str], *, duplicate: bool = False, chance_files: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None, flags: list[re.RegexFlag] = None):
    pass