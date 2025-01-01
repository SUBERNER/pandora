import librosa
import soundfile as sf
import numpy as np
import Buffle


def volume(files: str | list[str], factor: float):
    """
    Adjusts the volume of the audio file(s).

    Parameter:
        files (str | list[str]): Path(s) of the audio file(s) to adjust.

        factor (float): Change in volume in decibels (dB).
            - 0.0: No change.
            - > 0.0: Increase volume.
            - < 0.0: Decrease volume.
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.outer.set_length(max(files, key=len))

        for file in files:
            try:
                audio, sample_rate = librosa.load(file, sr=None)
                gain = 10 ** (factor / 20)  # Convert dB to a linear scale
                new_audio = audio * gain  # Apply gain directly
                sf.write(file, new_audio, sample_rate)

                Buffle.Display.audio.result(file, "volume", factor, 0)
            except Exception as e:
                Buffle.Display.audio.error_result(file, "volume", str(e))
    except Exception as e:
        Buffle.Display.audio.error_result(files, "volume", str(e))


def pitch(files: str | list[str], factor: float):
    """
    Adjusts the pitch of the audio file(s).

    Parameter:
        files (str | list[str]): Path(s) of the audio file(s) to adjust.

        factor (float): Number of semitones to shift the pitch.
            - 0.0: No change.
            - > 0.0: Increase pitch (higher frequency).
            - < 0.0: Decrease pitch (lower frequency).
    """
    try:
        if isinstance(files, str):
            files = [files]

        Buffle.Display.outer.set_length(max(files, key=len))

        for file in files:
            try:
                audio, sample_rate = librosa.load(file, sr=None)
                new_audio = librosa.effects.pitch_shift(audio, sr=sample_rate, n_steps=factor)
                sf.write(file, new_audio, sample_rate)

                Buffle.Display.audio.result(file, "pitch", factor, 0)
            except Exception as e:
                Buffle.Display.audio.error_result(file, "pitch", str(e))
    except Exception as e:
        Buffle.Display.audio.error_result(files, "pitch", str(e))


def tempo(files: str | list[str], factor: float):
    """
    Adjusts the tempo of the audio file(s).

    Parameter:
        files (str | list[str]): Path(s) of the audio file(s) to adjust.

        factor (float): Multiplier for the tempo.
            - 1.0: No change.
            - > 1.0: Speed up the audio.
            - < 1.0: Slow down the audio.
    """
    try:
        if isinstance(files, str):
            files = [files]

        Buffle.Display.outer.set_length(max(files, key=len))

        for file in files:
            try:
                audio, sample_rate = librosa.load(file, sr=None)
                new_audio = librosa.effects.time_stretch(audio, rate=factor)
                sf.write(file, new_audio, sample_rate)

                Buffle.Display.audio.result(file, "tempo", factor, 0)
            except Exception as e:
                Buffle.Display.audio.error_result(file, "tempo", str(e))
    except Exception as e:
        Buffle.Display.audio.error_result(files, "tempo", str(e))


def reverse(files: str | list[str]):
    """
    Reverses the playback of the audio file(s).

    Parameter:
        files (str | list[str]): Path(s) of the audio file(s) to reverse.
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.outer.set_length(max(files, key=len))

        for file in files:
            try:
                audio, sample_rate = librosa.load(file, sr=None)
                new_audio = audio[::-1]  # reverses audio by flipping array
                sf.write(file, new_audio, sample_rate)

                Buffle.Display.audio.result(file, "reverse", True, False)
            except Exception as e:
                Buffle.Display.audio.error_result(file, "reverse", str(e.args))
    except Exception as e:
        Buffle.Display.audio.error_result(file, "reverse", str(e.args))


def trim(files: str | list[str], start: float, end: float):
    """
    Trims the audio file(s) to a specified start and end time.

    Parameter:
        files (str | list[str]): Path(s) of the audio file(s) to trim.

        start (float): Start time in seconds.

        end (float): End time in seconds.
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.outer.set_length(max(files, key=len))

        for file in files:
            try:
                audio, sample_rate = librosa.load(file, sr=None)
                start_sample = int(start * sample_rate)
                end_sample = int(end * sample_rate)
                new_audio = audio[start_sample:end_sample]
                sf.write(file, new_audio, sample_rate)

                Buffle.Display.audio.result(file, "trim", int(librosa.get_duration(y=new_audio, sr=sample_rate)), int(librosa.get_duration(y=audio, sr=sample_rate)))
            except Exception as e:
                Buffle.Display.audio.error_result(file, "trim", str(e.args))
    except Exception as e:
        Buffle.Display.audio.error_result(file, "trim", str(e.args))


def normalize(files: str | list[str], factor: float):
    """
    Normalizes the volume of the audio file(s) to a specified level.

    Parameter:
        files (str | list[str]): Path(s) of the audio file(s) to normalize.

        factor (float): Normalization factor to scale the volume.
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.outer.set_length(max(files, key=len))

        for file in files:
            try:
                audio, sample_rate = librosa.load(file, sr=None)
                new_audio = librosa.util.normalize(audio, axis=0) * factor  # changes the normalization
                sf.write(file, new_audio, sample_rate)

                Buffle.Display.audio.result(file, "normalize", np.sqrt(np.mean(new_audio**2)), np.sqrt(np.mean(audio**2)))
            except Exception as e:
                Buffle.Display.audio.error_result(file, "normalize", str(e.args))
    except Exception as e:
        Buffle.Display.audio.error_result(file, "normalize", str(e.args))


def quality(files: str | list[str], factor: float):
    """
    Adjusts the quality of the audio file(s) by resampling.

    Parameter:
        files (str | list[str]): Path(s) of the audio file(s) to adjust.

        factor (float): Quality adjustment factor.
            - 1.0: No change.
            - > 1.0: Increase quality (higher sampling rate).
            - < 1.0: Decrease quality (lower sampling rate).
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.outer.set_length(max(files, key=len))

        for file in files:
            try:
                audio, sample_rate = librosa.load(file, sr=None)
                new_sample_rate = int(sample_rate * factor)
                new_audio = librosa.resample(audio, orig_sr=sample_rate, target_sr=new_sample_rate)
                sf.write(file, new_audio, new_sample_rate)

                Buffle.Display.audio.result(file, "quality", new_sample_rate, sample_rate)
            except Exception as e:
                Buffle.Display.audio.error_result(file, "quality", str(e.args))
    except Exception as e:
        Buffle.Display.audio.error_result(file, "quality", str(e.args))


def mid(files: str | list[str], gain: float):
    """
    Boosts or reduces the mid frequencies of the audio file(s).

    Parameter:
        files (str | list[str]): Path(s) of the audio file(s) to adjust.

        gain (float): Gain factor in decibels (dB) for the mid frequencies.
            - 0.0: No change.
            - > 0.0: Boost mid frequencies.
            - < 0.0: Reduce mid frequencies.
    """
    try:
        if isinstance(files, str):
            files = [files]

        Buffle.Display.outer.set_length(max(files, key=len))

        for file in files:
            try:
                audio, sample_rate = librosa.load(file, sr=None)
                spectrogram = librosa.stft(audio)
                f_bin = librosa.fft_frequencies(sr=sample_rate)

                # Apply gain to mid frequencies (200 Hz - 2000 Hz)
                gain_factor = 10 ** (gain / 20)
                mid_filter = np.ones(spectrogram.shape[0])
                mid_filter[(f_bin >= 200) & (f_bin <= 2000)] = gain_factor

                # Apply filter and reconstruct audio
                modified_spectrogram = spectrogram * mid_filter[:, np.newaxis]
                new_audio = np.real(librosa.istft(modified_spectrogram))
                sf.write(file, new_audio, sample_rate)

                Buffle.Display.audio.result(file, "mid", gain, 0)
            except Exception as e:
                Buffle.Display.audio.error_result(file, "mid", str(e))
    except Exception as e:
        Buffle.Display.audio.error_result(files, "mid", str(e))



def bass(files: str | list[str], gain: float):
    """
    Boosts or reduces the bass frequencies of the audio file(s).

    Parameter:
        files (str | list[str]): Path(s) of the audio file(s) to adjust.

        gain (float): Gain factor in decibels (dB) for the bass frequencies.
            - 0.0: No change.
            - > 0.0: Boost bass frequencies.
            - < 0.0: Reduce bass frequencies.
    """
    try:
        if isinstance(files, str):
            files = [files]

        Buffle.Display.outer.set_length(max(files, key=len))

        for file in files:
            try:
                audio, sample_rate = librosa.load(file, sr=None)
                spectrogram = librosa.stft(audio)
                f_bin = librosa.fft_frequencies(sr=sample_rate)

                # Apply gain to bass frequencies (20-200 Hz)
                gain_factor = 10 ** (gain / 20)
                bass_filter = np.ones(spectrogram.shape[0])
                bass_filter[(f_bin >= 20) & (f_bin <= 200)] = gain_factor

                # Apply filter and reconstruct audio
                modified_spectrogram = spectrogram * bass_filter[:, np.newaxis]
                new_audio = np.real(librosa.istft(modified_spectrogram))
                sf.write(file, new_audio, sample_rate)

                Buffle.Display.audio.result(file, "bass", gain, 0)
            except Exception as e:
                Buffle.Display.audio.error_result(file, "bass", str(e))
    except Exception as e:
        Buffle.Display.audio.error_result(files, "bass", str(e))


def treble(files: str | list[str], gain: float):
    """
    Boosts or reduces the treble frequencies of the audio file(s).

    Parameter:
        files (str | list[str]): Path(s) of the audio file(s) to adjust.

        gain (float): Gain factor in decibels (dB) for the treble frequencies.
            - 0.0: No change
            - > 0.0: Boost treble frequencies.
            - < 0.0: Reduce treble frequencies.
    """
    try:
        if isinstance(files, str):
            files = [files]

        Buffle.Display.outer.set_length(max(files, key=len))

        for file in files:
            try:
                audio, sample_rate = librosa.load(file, sr=None)
                spectrogram = librosa.stft(audio)
                f_bin = librosa.fft_frequencies(sr=sample_rate)

                # Apply gain to treble frequencies (2000 Hz - Nyquist/2)
                gain_factor = 10 ** (gain / 20)
                treble_filter = np.ones(spectrogram.shape[0])
                treble_filter[(f_bin >= 2000) & (f_bin <= sample_rate // 2)] = gain_factor

                # Apply filter and reconstruct audio
                modified_spectrogram = spectrogram * treble_filter[:, np.newaxis]
                new_audio = np.real(librosa.istft(modified_spectrogram))
                sf.write(file, new_audio, sample_rate)

                Buffle.Display.audio.result(file, "treble", gain, 0)
            except Exception as e:
                Buffle.Display.audio.error_result(file, "treble", str(e))
    except Exception as e:
        Buffle.Display.audio.error_result(files, "treble", str(e))
