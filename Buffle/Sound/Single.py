from pydub import AudioSegment
import os
import Buffle


def volume(files: str | list[str], factor: float):
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.outer.set_length(max(files, key=len))

        for file in files:
            try:
                ext = os.path.splitext(file)[1].replace('.', '')  # gets the files extension and removes dot
                sound = AudioSegment.from_file(file, format=ext)

                new_sound = sound + factor  # increases volume
                new_sound.export(file, format=ext)

                Buffle.Display.sound.result(file, "volume", factor, 0)
            except Exception as e:
                Buffle.Display.sound.error_result(file, "volume", str(e.args))
    except Exception as e:
        Buffle.Display.sound.error_result(files, "volume", str(e.args))


def pitch(files: str | list[str], factor: float):
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.outer.set_length(max(files, key=len))

        for file in files:
            try:
                ext = os.path.splitext(file)[1].replace('.', '')  # gets the files extension and removes dot
                sound = AudioSegment.from_file(file, format=ext)

                # makes pitch higher or lower
                new_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': int(sound.frame_rate * (2.0 ** factor))})
                new_sound.export(file, format=ext)

                Buffle.Display.sound.result(file, "pitch", factor, 0)
            except Exception as e:
                Buffle.Display.sound.error_result(file, "pitch", str(e.args))
    except Exception as e:
        Buffle.Display.sound.error_result(file, "pitch", str(e.args))


def reverse(files: str | list[str]):
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.outer.set_length(max(files, key=len))

        for file in files:
            try:
                ext = os.path.splitext(file)[1].replace('.', '')  # gets the files extension and removes dot
                sound = AudioSegment.from_file(file, format=ext)

                new_sound = sound.reverse()
                new_sound.export(file, format=ext)

                Buffle.Display.sound.result(file, "reverse", True, False)
            except Exception as e:
                Buffle.Display.sound.error_result(file, "reverse", str(e.args))
    except Exception as e:
        Buffle.Display.sound.error_result(file, "reverse", str(e.args))


def trim(files: str | list[str], start: float, end: float):
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.outer.set_length(max(files, key=len))

        # converts seconds into milliseconds
        start = int(start * 1000)
        end = int(end * 1000)

        for file in files:
            try:
                ext = os.path.splitext(file)[1].replace('.', '')  # gets the files extension and removes dot
                sound = AudioSegment.from_file(file, format=ext)

                new_sound = sound[start:end]  # trims audio
                new_sound.export(file, format=ext)

                Buffle.Display.sound.result(file, "trim", [start, end], [0, len(sound)])
            except Exception as e:
                Buffle.Display.sound.error_result(file, "trim", str(e.args))
    except Exception as e:
        Buffle.Display.sound.error_result(file, "trim", str(e.args))


def normalize(files: str | list[str], factor: float):
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.outer.set_length(max(files, key=len))

        for file in files:
            try:
                ext = os.path.splitext(file)[1].replace('.', '')  # gets the files extension and removes dot
                sound = AudioSegment.from_file(file, format=ext)

                new_dBFS = sound.dBFS * factor
                new_sound = sound.apply_gain(new_dBFS)
                new_sound.export(file, format=ext)

                Buffle.Display.sound.result(file, "normalize", new_dBFS, sound.dBFS)
            except Exception as e:
                Buffle.Display.sound.error_result(file, "normalize", str(e.args))
    except Exception as e:
        Buffle.Display.sound.error_result(file, "normalize", str(e.args))


def low_pass(files: str | list[str], factor: float):
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.outer.set_length(max(files, key=len))

        for file in files:
            try:
                ext = os.path.splitext(file)[1].replace('.', '')  # gets the files extension and removes dot
                sound = AudioSegment.from_file(file, format=ext)

                new_sound = sound.low_pass_filter(factor)
                new_sound.export(file, format=ext)

                Buffle.Display.sound.result(file, "low_pass", factor, 0)
            except Exception as e:
                Buffle.Display.sound.error_result(file, "low_pass", str(e.args))
    except Exception as e:
        Buffle.Display.sound.error_result(file, "low_pass", str(e.args))


def high_pass(files: str | list[str], factor: float):
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.outer.set_length(max(files, key=len))

        for file in files:
            try:
                ext = os.path.splitext(file)[1].replace('.', '')  # gets the files extension and removes dot
                sound = AudioSegment.from_file(file, format=ext)

                new_sound = sound.high_pass_filter(factor)
                new_sound.export(file, format=ext)

                Buffle.Display.sound.result(file, "high_pass", factor, 0)
            except Exception as e:
                Buffle.Display.sound.error_result(file, "high_pass", str(e.args))
    except Exception as e:
        Buffle.Display.sound.error_result(file, "high_pass", str(e.args))
