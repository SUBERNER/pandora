from pydub import AudioSegment
import os
import Buffle


def volume(files: str | list[str], factor: float):
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        ext = os.path.splitext(file)[1].replace('.', '')  # gets the files extension and removes dot
        sound = AudioSegment.from_file(file, format=ext)

        new_sound = sound + factor  # increases volume
        new_sound.export(file, format=ext)

        Buffle.Display.sound.result(file, f"{Buffle.Display.Color.MAGENTA}volume{Buffle.Display.Color.RESET}", factor, 0)


def pitch(files: str | list[str], factor: float):
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        ext = os.path.splitext(file)[1].replace('.', '')  # gets the files extension and removes dot
        sound = AudioSegment.from_file(file, format=ext)

        # makes pitch higher or lower
        new_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': int(sound.frame_rate * (2.0 ** factor))})
        new_sound.export(file, format=ext)

        Buffle.Display.sound.result(file, f"{Buffle.Display.Color.MAGENTA}pitch{Buffle.Display.Color.RESET}", factor, 0)


def reverse(files: str | list[str]):
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        ext = os.path.splitext(file)[1].replace('.', '')  # gets the files extension and removes dot
        sound = AudioSegment.from_file(file, format=ext)

        new_sound = sound.reverse()
        new_sound.export(file, format=ext)

        Buffle.Display.sound.result(file, f"{Buffle.Display.Color.MAGENTA}reverse{Buffle.Display.Color.RESET}", True, False)


def trim(files: str | list[str], start: float, end: float):
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    # converts seconds into milliseconds
    start = int(start * 1000)
    end = int(end * 1000)

    for file in files:
        ext = os.path.splitext(file)[1].replace('.', '')  # gets the files extension and removes dot
        sound = AudioSegment.from_file(file, format=ext)

        new_sound = sound[start:end]  # trims audio
        new_sound.export(file, format=ext)

        Buffle.Display.sound.result(file, f"{Buffle.Display.Color.MAGENTA}trim{Buffle.Display.Color.RESET}", [start, end], [0, len(sound)])


def normalize(files: str | list[str], factor: float):
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        ext = os.path.splitext(file)[1].replace('.', '')  # gets the files extension and removes dot
        sound = AudioSegment.from_file(file, format=ext)

        new_dBFS = sound.dBFS * factor
        new_sound = sound.apply_gain(new_dBFS)
        new_sound.export(file, format=ext)

        Buffle.Display.sound.result(file, f"{Buffle.Display.Color.MAGENTA}normalize{Buffle.Display.Color.RESET}", new_dBFS, sound.dBFS)


def low_pass(files: str | list[str], factor: float):
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        ext = os.path.splitext(file)[1].replace('.', '')  # gets the files extension and removes dot
        sound = AudioSegment.from_file(file, format=ext)

        new_sound = sound.low_pass_filter(factor)
        new_sound.export(file, format=ext)

        Buffle.Display.sound.result(file, f"{Buffle.Display.Color.MAGENTA}low_pass{Buffle.Display.Color.RESET}", factor, 0)


def high_pass(files: str | list[str], factor: float):
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        ext = os.path.splitext(file)[1].replace('.', '')  # gets the files extension and removes dot
        sound = AudioSegment.from_file(file, format=ext)

        new_sound = sound.high_pass_filter(factor)
        new_sound.export(file, format=ext)

        Buffle.Display.sound.result(file, f"{Buffle.Display.Color.MAGENTA}high_pass{Buffle.Display.Color.RESET}", factor, 0)

