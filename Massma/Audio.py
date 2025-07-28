from Massma import random  # used for seeds
from Massma.Filter import *
import Massma
import ffmpeg
import tempfile
import os


def volume(files: str | list[str], factor: float, *, mask: tuple[float,float] | None = None, chance_files: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])

            # gets size of the largest path for better result formatting
            files = [os.path.abspath(file) for file in files]  # makes sure files are converted into the full bath for better displaying
            Massma.Display.audio.set_source_length(max(files, key=len))

            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                        # create a temporary version of the file so that the changes can be made,
                        # also gives the benefit that if the method fails, it will not save the changes to the file
                        suffix_file = os.path.splitext(file)[1] # gets files extension
                        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix_file).name # creates temporary file

                        # get file to then extract only the audio
                        input = ffmpeg.input(file)
                        audio = input.audio # stores version of audio file that will be used for comparing later
                        new_audio = audio # all changes will be make and saved to this version of the audio

                        if mask:
                            # only effects areas of audio that is in the range of the masks regions
                            mask_audio = audio.filter('atrim', start=mask[0], end=mask[1]) # trims the audio, creating a section of the altered audio to put on the non altered audio
                            mask_audio = mask_audio.filter('volume',factor)  # makes change to files volume by multiplying the current volume

                            # trims segments of the audio that will not be effected by the mask, and will later combine the 3 segments
                            pre_audio = new_audio.filter('atrim', end=mask[0]) # gets original audio before beginning of altered audio
                            post_audio = new_audio.filter('atrim', start=mask[1])  # gets original audio after end of altered audio

                            # combines the mask with the original segments to create the new audio
                            new_audio = ffmpeg.concat(pre_audio, mask_audio, post_audio, v=0, a=1)
                        else:
                            new_audio = audio.filter('volume',factor)  # makes change to files volume by multiplying the current volume

                        new_audio.output(temp_file).overwrite_output().run(quiet=True) # overwrite original file with changes
                        os.replace(temp_file, file)  # overwrites the old data with th new audio data

                        Massma.Display.audio.result(file, "volume", 1 , factor)

                except Exception as e:
                    Massma.Display.audio.result_error(file, "volume", e)

    except Exception as e:
        Massma.Display.audio.result_error(len(files), "volume", e)


def normalize(files: str | list[str], *, mask: tuple[float,float], chance_files: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])

            # gets size of the largest path for better result formatting
            files = [os.path.abspath(file) for file in files]  # makes sure files are converted into the full bath for better displaying
            Massma.Display.audio.set_source_length(max(files, key=len))

            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                        # create a temporary version of the file so that the changes can be made,
                        # also gives the benefit that if the method fails, it will not save the changes to the file
                        suffix_file = os.path.splitext(file)[1] # gets files extension
                        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix_file).name # creates temporary file

                        # get file to then extract only the audio
                        input = ffmpeg.input(file)
                        audio = input.audio  # stores version of audio file that will be used for comparing later
                        new_audio = audio  # all changes will be make and saved to this version of the audio

                        if mask:
                            # only effects areas of audio that is in the range of the masks regions
                            mask_audio = audio.filter('atrim', start=mask[0], end=mask[1])  # trims the audio, creating a section of the altered audio to put on the non altered audio
                            mask_audio = mask_audio.filter("loudnorm", i=-16, tp=-1.5, lra=11) # makes change to files volume, by normalizing and evening the volume

                            # trims segments of the audio that will not be effected by the mask, and will later combine the 3 segments
                            pre_audio = new_audio.filter('atrim', end=mask[0])  # gets original audio before beginning of altered audio
                            post_audio = new_audio.filter('atrim', start=mask[1])  # gets original audio after end of altered audio

                            # combines the mask with the original segments to create the new audio
                            new_audio = ffmpeg.concat(pre_audio, mask_audio, post_audio, v=0, a=1)
                        else:
                            new_audio = audio.filter("loudnorm", i=-16, tp=-1.5, lra=11) # makes change to files volume, by normalizing and evening the volume

                        new_audio.output(temp_file).overwrite_output().run(quiet=True)  # overwrite original file with changes
                        os.replace(temp_file, file)  # overwrites the old data with th new audio data

                        Massma.Display.audio.result(file, "normalize", False, True)

                except Exception as e:
                    Massma.Display.audio.result_error(file, "normalize", e)

    except Exception as e:
        Massma.Display.audio.result_error(len(files), "normalize", e)


def reverse(files: str | list[str], *, mask: tuple[float,float], chance_files: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])

            # gets size of the largest path for better result formatting
            files = [os.path.abspath(file) for file in files]  # makes sure files are converted into the full bath for better displaying
            Massma.Display.audio.set_source_length(max(files, key=len))

            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                        # create a temporary version of the file so that the changes can be made,
                        # also gives the benefit that if the method fails, it will not save the changes to the file
                        suffix_file = os.path.splitext(file)[1] # gets files extension
                        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix_file).name # creates temporary file

                        # get file to then extract only the audio
                        input = ffmpeg.input(file)
                        audio = input.audio  # stores version of audio file that will be used for comparing later
                        new_audio = audio  # all changes will be make and saved to this version of the audio

                        if mask:
                            # only effects areas of audio that is in the range of the masks regions
                            mask_audio = audio.filter('atrim', start=mask[0], end=mask[1])  # trims the audio, creating a section of the altered audio to put on the non altered audio
                            mask_audio = mask_audio.filter("areverse") # makes change to files by reversing the audio

                            # trims segments of the audio that will not be effected by the mask, and will later combine the 3 segments
                            pre_audio = new_audio.filter('atrim', end=mask[0])  # gets original audio before beginning of altered audio
                            post_audio = new_audio.filter('atrim', start=mask[1])  # gets original audio after end of altered audio

                            # combines the mask with the original segments to create the new audio
                            new_audio = ffmpeg.concat(pre_audio, mask_audio, post_audio, v=0, a=1)
                        else:
                            new_audio = audio.filter("areverse") # makes change to files by reversing the audio

                        new_audio.output(temp_file).overwrite_output().run(quiet=True)  # overwrite original file with changes
                        os.replace(temp_file, file)  # overwrites the old data with th new audio data

                        Massma.Display.audio.result(file, "reverse", False, True)

                except Exception as e:
                    Massma.Display.audio.result_error(file, "reverse", e)

    except Exception as e:
        Massma.Display.audio.result_error(len(files), "reverse", e)


def pitch(files: str | list[str], factor: float, *, mask: tuple[float,float], chance_files: float = 1, chance_total: float = 1,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])

            # gets size of the largest path for better result formatting
            files = [os.path.abspath(file) for file in files]  # makes sure files are converted into the full bath for better displaying
            Massma.Display.audio.set_source_length(max(files, key=len))

            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                        # create a temporary version of the file so that the changes can be made,
                        # also gives the benefit that if the method fails, it will not save the changes to the file
                        suffix_file = os.path.splitext(file)[1]  # gets files extension
                        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix_file).name  # creates temporary file

                        # get file to then extract only the audio
                        input = ffmpeg.input(file)
                        audio = input.audio  # stores version of audio file that will be used for comparing later
                        new_audio = audio  # all changes will be make and saved to this version of the audio

                        if mask:
                            # FINISH THIS LATER
                            # only effects areas of audio that is in the range of the masks regions
                            mask_audio = audio.filter('atrim', start=mask[0], end=mask[1])  # trims the audio, creating a section of the altered audio to put on the non altered audio
                            mask_audio = mask_audio.filter('asetrate', f'44100*{factor}').filter('aresample', '44100')

                            # trims segments of the audio that will not be effected by the mask, and will later combine the 3 segments
                            pre_audio = new_audio.filter('atrim', end=mask[0])  # gets original audio before beginning of altered audio
                            post_audio = new_audio.filter('atrim', start=mask[1])  # gets original audio after end of altered audio

                            # combines the mask with the original segments to create the new audio
                            new_audio = ffmpeg.concat(pre_audio, mask_audio, post_audio, v=0, a=1)
                        else:
                            new_audio = input.audio.filter('asetrate', f'44100*{factor}').filter('aresample', '44100')  # makes change to files tempo, which is the audio's frequency, by multiplying the audio's current sample rates

                        new_audio.output(temp_file).overwrite_output().run(quiet=True)  # overwrite original file with changes
                        os.replace(temp_file, file)  # overwrites the old data with th new audio data

                        Massma.Display.audio.result(file, "pitch", 1, factor)


                except Exception as e:
                    Massma.Display.audio.result_error(len(files), "pitch", e)

    except Exception as e:
        Massma.Display.audio.result_error(len(files), "pitch", e)

def tempo(files: str | list[str], factor: float, *, mask: tuple[float,float], chance_files: float = 1, chance_total: float = 1,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes data always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            excludes = excludes if isinstance(excludes, list) else ([excludes] if excludes else [])
            alters = alters if isinstance(alters, list) else ([alters] if alters else [])

            # gets size of the largest path for better result formatting
            files = [os.path.abspath(file) for file in files]  # makes sure files are converted into the full bath for better displaying
            Massma.Display.audio.set_source_length(max(files, key=len))

            for file in files:
                try:
                    if (chance_files >= random.random() and  # random change to be added or removed by filters
                            not (any(ignore(file) for ignore in ignores)) and
                            not (any(exclude(file) for exclude in excludes))):

                        # gives a chance to alter inside a file
                        if alters is not None:
                            for alter in alters:
                                alter(file)

                        # create a temporary version of the file so that the changes can be made,
                        # also gives the benefit that if the method fails, it will not save the changes to the file
                        suffix_file = os.path.splitext(file)[1]  # gets files extension
                        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix_file).name  # creates temporary file

                        # get file to then extract only the audio
                        input = ffmpeg.input(file)
                        audio = input.audio  # stores version of audio file that will be used for comparing later
                        new_audio = audio  # all changes will be make and saved to this version of the audio

                        if mask:
                            # only effects areas of audio that is in the range of the masks regions
                            mask_audio = audio.filter('atrim', start=mask[0], end=mask[1])  # trims the audio, creating a section of the altered audio to put on the non altered audio
                            mask_audio = mask_audio.filter('atempo', factor)  # makes change to files tempo, which is the audio's speed, by multiplying the audio's current speed

                            # trims segments of the audio that will not be effected by the mask, and will later combine the 3 segments
                            pre_audio = new_audio.filter('atrim', end=mask[0])  # gets original audio before beginning of altered audio
                            post_audio = new_audio.filter('atrim', start=mask[1])  # gets original audio after end of altered audio

                            # combines the mask with the original segments to create the new audio
                            new_audio = ffmpeg.concat(pre_audio, mask_audio, post_audio, v=0, a=1)
                        else:
                            new_audio = audio.filter('atempo', factor)  # makes change to files tempo, which is the audio's speed, by multiplying the audio's current speed

                        new_audio.output(temp_file).overwrite_output().run(quiet=True)  # overwrite original file with changes
                        os.replace(temp_file, file)  # overwrites the old data with th new audio data

                        Massma.Display.audio.result(file, "tempo", 1, factor)

                except Exception as e:
                    Massma.Display.audio.result_error(len(files), "tempo", e)

    except Exception as e:
        Massma.Display.audio.result_error(len(files), "tempo", e)