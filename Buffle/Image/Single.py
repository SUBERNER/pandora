from Buffle import random  # used for seeds
from PIL import Image, ImageEnhance, ImageFilter, ImageOps  # Pillow
import numpy as np
import os
import Buffle
# Used for altering single or non atlas images


def rotate(files: str | list[str], degree: int, *, expand: bool = False, fillcolor: tuple[int, int, int] | None = None, resampling: int = 2, optimize: bool = False):
    """
    Rotates the image clockwise or counterclockwise.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to rotate.

        degree (int): Degrees of rotation.
            - 0: No rotation.
            - > 0: Rotate clockwise.
            - < 0: Rotate counterclockwise.

    keyword parameter:
        expand (bool): Whether to expand the resolution to fit the entire image after rotation. Defaults to False.

        fillcolor (tuple[int, int, int] | None): Background color for revealed areas. Only used if expand=True. Defaults to None.

        resampling (int): Resampling filter to use during rotating. Defaults to 2 (BILINEAR).
            - 0: NEAREST
            - 1: LANCZOS
            - 2: BILINEAR
            - 3: BICUBIC
            - 4: BOX
            - 5: HAMMING

        optimize (bool): If True, optimizes the image file during saving, reducing file size without compromising quality. Defaults to False.
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.image.set_length(max(files, key=len))

        for file in files:
            try:
                image = Image.open(file)
                new_image = image.rotate(-degree, expand=expand, fillcolor=fillcolor, resample=resampling)

                new_image.save(file, optimize=optimize)

                Buffle.Display.image.result(file, "rotate", degree, 0)
            except Exception as e:
                Buffle.Display.image.error_result(file, "rotate", str(e.args))
    except Exception as e:
        Buffle.Display.image.error_result(files, "rotate", str(e.args))


def flip(files: str | list[str], horizontal: bool, vertical: bool, *, optimize: bool = False):
    """
    Flips the image vertically and/or horizontally.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to flip.

        horizontal (bool): Whether to flip the image horizontally (mirror image).

        vertical (bool): Whether to flip the image vertically (upside down).

    Keyword Parameter:
        optimize (bool): If True, optimizes the image file during saving, reducing file size without compromising quality. Defaults to False.
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.image.set_length(max(files, key=len))

        for file in files:
            try:
                image = Image.open(file)
                new_image = Image.open(file)

                if horizontal:
                    new_image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
                if vertical:
                    new_image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

                new_image.save(file, optimize=optimize)
                Buffle.Display.image.result(file, "flip", [horizontal, vertical], [False, False])
            except Exception as e:
                Buffle.Display.image.error_result(file, "flip", str(e.args))
    except Exception as e:
        Buffle.Display.image.error_result(files, "flip", str(e.args))


def resize(files: str | list[str], width: int, height: int, *, resampling: int = 2, optimize: bool = False):
    """
    Resizes the image's dimensions.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to resize.

        width (int): New width of the image.

        height (int): New height of the image.

    keyword parameter:
        resampling (int): Resampling filter to use during resizing. Defaults to 2 (BILINEAR).
            - 0: NEAREST
            - 1: LANCZOS
            - 2: BILINEAR
            - 3: BICUBIC
            - 4: BOX
            - 5: HAMMING

        optimize (bool): If True, optimizes the image file during saving, reducing file size without compromising quality. Defaults to False.
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.image.set_length(max(files, key=len))

        for file in files:
            try:
                image = Image.open(file)

                new_image = image.resize((width, height), resampling)
                new_image.save(file, optimize=optimize)

                new_image.save(file)
                Buffle.Display.image.result(file, f"resize", new_image.size, image.size)
            except Exception as e:
                Buffle.Display.image.error_result(file, "resize", str(e.args))
    except Exception as e:
        Buffle.Display.image.error_result(files, "resize", str(e.args))


def invert(files: str | list[str], *, optimize: bool = False):
    """
    Inverts the image's colors.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to invert.

    Keyword Parameter:
        optimize (bool): If True, optimizes the image file during saving, reducing file size without compromising quality. Defaults to False.
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.image.set_length(max(files, key=len))

        for file in files:
            try:
                image = Image.open(file)

                new_image = ImageOps.invert(image)
                new_image.save(file, optimize=optimize)

                new_image.save(file)
                Buffle.Display.image.result(file, "invert", True, False)
            except Exception as e:
                Buffle.Display.image.error_result(file, "invert", str(e.args))
    except Exception as e:
        Buffle.Display.image.error_result(files, "invert", str(e.args))


def noise(files: str | list[str], factor: float, *, mean: float = 0, range: tuple[int, int] = (0, 255), optimize: bool = False):
    """
    Adds random variation (noise) to the image's pixels.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to apply noise to.

        factor (float): Strength of the noise.
            - 0.0: No noise.
            - Negative values: Decrease noise.
            - < 1.0: Increase noise.

    Keyword Parameter:
        mean (float): Mean value of the noise distribution. Defaults to 0.
            - 0.0: Noise is centered (equal positive and negative variation).
            - < 0.0: Noise skews negative.
            - > 0.0: Noise skews positive.

        range (tuple[int, int]): Minimum and maximum bounds for pixel values. Defaults to (0, 255).

        optimize (bool): If True, optimizes the image file during saving, reducing file size without compromising quality. Defaults to False.
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.image.set_length(max(files, key=len))

        for file in files:
            try:
                image = Image.open(file)
                image_array = np.array(image)  # converts to array

                # generates noice for the brightness of the image
                noise_array = np.random.normal(mean, factor, image_array.shape[:2])  # Only one channel for brightness
                if len(image_array.shape) == 3:  # If the image is RGB
                    noise_array = noise_array[:, :, np.newaxis]  # Add channel dimension for broadcasting

                # adds the noise to the image
                adjusted_array = image_array + noise_array
                adjusted_array = np.clip(adjusted_array, range[0], range[1])  # Keeps values between 0 and 255

                # converts back into an image
                new_image = Image.fromarray(adjusted_array.astype(np.uint8))
                new_image.save(file, optimize=optimize)

                # determines the changes made by method to display
                image_change = np.sum(np.abs(adjusted_array - image_array) > 1) / image_array.size * 100

                Buffle.Display.image.result(file, "noise", image_change, 0)
            except Exception as e:
                Buffle.Display.image.error_result(file, "noise", str(e.args))
    except Exception as e:
        Buffle.Display.image.error_result(files, "noise", str(e.args))


def blur(files: str | list[str], factor: float, *, optimize: bool = False):
    """
    Applies a Gaussian blur to the image.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to blur.

        factor (float): Radius of the blur.
            - 0.0: No blur.
            - < 0.0: Increase blur radius.

    Keyword Parameter:
        optimize (bool): If True, optimizes the image file during saving, reducing file size without compromising quality. Defaults to False.
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.image.set_length(max(files, key=len))

        for file in files:
            try:
                image = Image.open(file)

                # adds blur to image
                new_image = image.filter(ImageFilter.GaussianBlur(radius=factor))
                new_image.save(file, optimize=optimize)

                Buffle.Display.image.result(file, "blur", factor, 0)
            except Exception as e:
                Buffle.Display.image.error_result(file, "blur", str(e.args))
    except Exception as e:
        Buffle.Display.image.error_result(files, "blur", str(e.args))


def saturation(files: str | list[str], factor: float, *, optimize: bool = False):
    """
    Adjusts the image's saturation (color intensity).

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to adjust saturation for.

        factor (float): Saturation adjustment factor.
            - 1.0: No change.
            - < 1.0: Decrease saturation.
            - > 1.0: Increase saturation.

    Keyword Parameter:
        optimize (bool): If True, optimizes the image file during saving, reducing file size without compromising quality. Defaults to False.
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.image.set_length(max(files, key=len))

        for file in files:
            try:
                image = Image.open(file)
                new_image = ImageEnhance.Color(image).enhance(factor)  # alters image
                new_image.save(file, optimize=optimize)

                # determines the changes made by method to display
                hsv_image = image.convert("HSV")
                hsv_new_image = new_image.convert("HSV")
                image_mean = np.mean(np.array(hsv_image)[:, :, 1])
                new_image_mean = np.mean(np.array(hsv_new_image)[:, :, 1])

                Buffle.Display.image.result(file, "saturation", new_image_mean, image_mean)
            except Exception as e:
                Buffle.Display.image.error_result(file, "saturation", str(e.args))
    except Exception as e:
        Buffle.Display.image.error_result(files, "saturation", str(e.args))


def contrast(files: str | list[str], factor: float, optimize: bool = False):
    """
    Adjusts the image's contrast (range of brightness).

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to adjust contrast for.

        factor (float): Contrast adjustment factor.
            - 1.0: No change.
            - < 1.0: Decrease contrast.
            - > 1.0: Increase contrast.

    Keyword Parameter:
        optimize (bool): If True, optimizes the image file during saving, reducing file size without compromising quality. Defaults to False.
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.image.set_length(max(files, key=len))

        for file in files:
            try:
                image = Image.open(file)
                new_image = ImageEnhance.Contrast(image).enhance(factor)
                new_image.save(file, optimize=optimize)

                # determines the changes made by method to display
                grayscale_image = image.convert("L")
                grayscale_new_image = new_image.convert("L")
                image_mean = np.std(np.array(grayscale_image))
                new_image_mean = np.std(np.array(grayscale_new_image))

                Buffle.Display.image.result(file, "contrast", new_image_mean, image_mean)
            except Exception as e:
                Buffle.Display.image.error_result(file, "contrast", str(e.args))
    except Exception as e:
        Buffle.Display.image.error_result(files, "contrast", str(e.args))


def brightness(files: str | list[str], factor: float, *, optimize: bool = False):
    """
    Adjusts the image's brightness.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to adjust brightness for.

        factor (float): Brightness adjustment factor.
            - 1.0: No change.
            - < 1.0: Decrease brightness.
            - > 1.0: Increase brightness.

    Keyword Parameter:
        optimize (bool): If True, optimizes the image file during saving, reducing file size without compromising quality. Defaults to False.
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.image.set_length(max(files, key=len))

        for file in files:
            try:
                image = Image.open(file)
                new_image = ImageEnhance.Brightness(image).enhance(factor)
                new_image.save(file, optimize=optimize)

                # determines the changes made by method to display
                grayscale_image = image.convert("L")
                grayscale_new_image = new_image.convert("L")
                image_mean = np.mean(np.array(grayscale_image))
                new_image_mean = np.mean(np.array(grayscale_new_image))

                Buffle.Display.image.result(file, "brightness", new_image_mean, image_mean)
            except Exception as e:
                Buffle.Display.image.error_result(file, "brightness", str(e.args))
    except Exception as e:
        Buffle.Display.image.error_result(files, "brightness", str(e.args))


def sharpness(files: str | list[str], factor: float, *, optimize: bool = False):
    """
    Adjusts the image's sharpness (clarity of detail).

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to adjust sharpness for.

        factor (float): Sharpness adjustment factor.
            - 1.0: No change.
            - < 1.0: Decrease sharpness.
            - > 1.0: Increase sharpness.

    Keyword Parameter:
        optimize (bool): If True, optimizes the image file during saving, reducing file size without compromising quality. Defaults to False.
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.image.set_length(max(files, key=len))

        for file in files:
            try:
                image = Image.open(file)
                new_image = ImageEnhance.Sharpness(image).enhance(factor)
                new_image.save(file, optimize=optimize)

                Buffle.Display.image.result(file, "sharpness", factor, 1)
            except Exception as e:
                Buffle.Display.image.error_result(file, "sharpness", str(e.args))
    except Exception as e:
        Buffle.Display.image.error_result(files, "sharpness", str(e.args))


def resolution(files: str | list[str], factor: float, *, resampling: int = 2, optimize: bool = False):
    """
    Adjusts the image's resolution by scaling its dimensions.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to adjust resolution for.
        factor (float): Scaling factor for resolution.
            - 1.0: No change.
            - < 1.0: Decrease resolution.
            - > 1.0: Increase resolution.

    Keyword Parameter:
        resampling (int): Resampling filter to use during scaling. Defaults to 2 (BILINEAR).
            - 0: NEAREST
            - 1: LANCZOS
            - 2: BILINEAR
            - 3: BICUBIC
            - 4: BOX
            - 5: HAMMING

        optimize (bool): If True, optimizes the image file during saving, reducing file size without compromising quality. Defaults to False.
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.image.set_length(max(files, key=len))

        for file in files:
            try:
                image = Image.open(file)
                new_image = image.resize((int(image.width * factor), int(image.height * factor)), resampling)
                new_image.save(file, optimize=optimize)

                Buffle.Display.image.result(file, "resolution", new_image.size, image.size)
            except Exception as e:
                Buffle.Display.image.error_result(file, "resolution", str(e.args))
    except Exception as e:
        Buffle.Display.image.error_result(files, "resolution", str(e.args))


def quality(files: str | list[str], factor: float, *, optimize: bool = False):
    """
    Adjusts the image's quality and detail.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to adjust quality for.

        factor (float): Quality adjustment factor.
            - 1.0: No change.
            - < 1.0: Decrease quality.
            - > 1.0: Increase quality.
    Keyword Parameter:
        optimize (bool): If True, optimizes the image file during saving, reducing file size without compromising quality. Defaults to False.
    """
    try:
        # makes files always a list
        if isinstance(files, str):
            files = [files]

        # gets size of largest path for better result formatting
        Buffle.Display.image.set_length(max(files, key=len))

        for file in files:
            try:
                image = Image.open(file)
                original_size = os.path.getsize(file)  # used for displaying changes from method
                original_format = image.format  # gets original format after conversion
                original_mode = image.mode  # gets the original mode of the image such as "RGBA" or "RGB"

                # converts to include the alpha channel
                if image.mode != "RGBA":
                    image = image.convert("RGBA")
                    image.format = original_format  # add format back

                # gets images alpha channel
                alpha_image = image.split()[-1]  # Get the alpha channel
                # converts image to lossy and changes quality
                image.convert("RGB").save(file, format="JPEG", quality=int(factor * 100))

                # adds back alpha channel if one exists
                new_image = Image.open(file)
                new_image = new_image.convert(original_mode)
                if original_mode == "RGBA":
                    new_image = Image.composite(new_image, image, alpha_image)
                new_image.save(file, format=image.format.upper(), quality=100, optimize=optimize)

                Buffle.Display.image.result(file, "quality", os.path.getsize(file), original_size)
            except Exception as e:
                Buffle.Display.image.error_result(file, "quality", str(e.args))
    except Exception as e:
        Buffle.Display.image.error_result(files, "quality", str(e.args))