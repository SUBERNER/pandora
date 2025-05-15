from Massma import random  # used for seeds
from Massma.Filter import *
import Massma
import librosa
import soundfile
import numpy

def volume(files: str | list[str], factor: float, *, chance_files: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.audio.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                        audio, sample_rate = librosa.load(file, sr=None, mono=False) # extracts audio data
                        new_audio = audio * factor # increased or decreases volume based on the factor my multiplying it
                        soundfile.write(file, new_audio, sample_rate)

                        # used for calculating the display data for the result made by this method
                        # gets and displays the root mean square to get the average volume
                        audio_results = float(numpy.sqrt(numpy.mean(audio ** 2)))
                        new_audio_results = float(numpy.sqrt(numpy.mean(new_audio ** 2)))

                        Massma.Display.audio.result(file, "volume", audio_results, new_audio_results)

                except Exception as e:
                    Massma.Display.audio.result_error(files, "volume", e)

    except Exception as e:
        Massma.Display.audio.result_error(len(files), "volume", e)

def pitch(files: str | list[str], factor: float, *, chance_files: float = 1, chance_total: float = 1,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.audio.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                        audio, sample_rate = librosa.load(file, sr=None, mono=False) # extracts audio data
                        new_audio = librosa.effects.pitch_shift(audio, sample_rate=sample_rate, n_steps=(12 * numpy.log2(factor)))
                        soundfile.write(file, new_audio, sample_rate)

                except Exception as e:
                    Massma.Display.audio.result_error(files, "pitch", e)

    except Exception as e:
        Massma.Display.audio.result_error(len(files), "pitch", e)

def tempo(files: str | list[str], factor: float, *, chance_files: float = 1, chance_total: float = 1,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.audio.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                        audio, sample_rate = librosa.load(file, sr=None, mono=False) # extracts audio data
                        new_audio = librosa.effects.time_stretch(audio, rate=(1 / factor))
                        soundfile.write(file, new_audio, sample_rate)

                except Exception as e:
                    Massma.Display.audio.result_error(files, "tempo", e)

    except Exception as e:
        Massma.Display.audio.result_error(len(files), "tempo", e)

def trim(files: str | list[str], *, chance_files: float = 1, chance_total: float = 1,
         ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.audio.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                except Exception as e:
                    Massma.Display.audio.result_error(files, "trim", e)

    except Exception as e:
        Massma.Display.audio.result_error(len(files), "trim", e)

def bass(files: str | list[str], *, chance_files: float = 1, chance_total: float = 1,
         ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.audio.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                except Exception as e:
                    Massma.Display.audio.result_error(files, "bass", e)

    except Exception as e:
        Massma.Display.audio.result_error(len(files), "bass", e)

def mids(files: str | list[str], *, chance_files: float = 1, chance_total: float = 1,
         ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.audio.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                except Exception as e:
                    Massma.Display.audio.result_error(files, "mid", e)

    except Exception as e:
        Massma.Display.audio.result_error(len(files), "mids", e)

def treble(files: str | list[str], *, chance_files: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.audio.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                except Exception as e:
                    Massma.Display.audio.result_error(files, "treble", e)

    except Exception as e:
        Massma.Display.audio.result_error(len(files), "treble", e)