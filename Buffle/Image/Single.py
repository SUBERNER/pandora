from PIL import Image, ImageEnhance, ImageFilter, ImageOps  # Pillow
import numpy as np
import Buffle
# Used for altering single or non atlas textures


def rotate(files: str | list[str], degree: int, expand: bool = False):
    """
    Rotates the texture either clockwise or anti-clockwise.
    :param files: Target files' directory or location.
    :param degree: Degrees of rotation,
                values of 0 will not cause rotation,
                values less than 0 will cause clockwise rotation,
                and values higher than 0 will cause anti-clockwise rotation.
    :param expand: Expands resolution to fit entire image after rotation.
    :type files: str | list[str]
    :type degree: int
    :type expand: bool
    """
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        image = Image.open(file)
        new_image = image.rotate(degree, expand=expand)

        new_image.save(file)

        Buffle.Display.image.result(file, f"{Buffle.Display.Color.MAGENTA}rotate{Buffle.Display.Color.RESET}", degree, 0)


def flip(files: str | list[str], horizontal: bool, vertical: bool):
    """
    Flips the texture vertically and horizontally.
    :param files: Target files' directory or location.
    :param horizontal: Mirrors or flips the texture horizontally.
    :param vertical: Mirrors or flips texture vertically.
    :type files: str | list[str]
    :type horizontal: bool
    :type vertical: bool
    """
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        image = Image.open(file)
        new_image = Image.open(file)

        if horizontal:
            new_image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        if vertical:
            new_image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

        new_image.save(file)
        Buffle.Display.image.result(file, f"{Buffle.Display.Color.MAGENTA}flip{Buffle.Display.Color.RESET}", [horizontal, vertical], [False, False])


def resize(files: str | list[str], width: int, height: int):
    """
    Resizes the texture's width and height
    :param files: Target files' directory or location.
    :param width: Stretches or squeezes the texture width(x).
    :param height: Stretches or squeezes the texture height(y).
    :type files: str | list[str]
    :type width: int
    :type height: int
    """
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        image = Image.open(file)

        new_image = image.resize((width, height), Image.Resampling.BILINEAR)
        new_image.save(file)

        new_image.save(file)
        Buffle.Display.image.result(file, f"{Buffle.Display.Color.MAGENTA}resize{Buffle.Display.Color.RESET}", new_image.size, image.size)


def invert(files: str | list[str]):
    """
    Inverts the texture's colors to the opposite hue
    :param files: Target files' directory or location.
    :type files: str | list[str]
    """
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        image = Image.open(file)

        new_image = ImageOps.invert(image)
        new_image.save(file)

        new_image.save(file)
        Buffle.Display.image.result(file, f"{Buffle.Display.Color.MAGENTA}invert{Buffle.Display.Color.RESET}", new_image.size, image.size)


def noise(files: str | list[str], factor: float):
    """
    Alters the texture's pixels with random variation.
    :param files: Target files' directory or location.
    :param factor: Strength of the alteration,
                values of 0.0 will not affect the noise,
                values less than 0.0 will decrease noise,
                and values higher than 0.0 will increase noise.
    :type files: files: str | list[str]
    :type factor: float
    :type factor: average
    """
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        image = Image.open(file)
        image_array = np.array(image)  # converts to array

        # generates noice for the brightness of the image
        noise_array = np.random.normal(0, factor, image_array.shape[:2])  # Only one channel for brightness
        if len(image_array.shape) == 3:  # If the image is RGB
            noise_array = noise_array[:, :, np.newaxis]  # Add channel dimension for broadcasting

        # adds the noise to the image
        adjusted_array = image_array + noise_array
        adjusted_array = np.clip(adjusted_array, 0, 255)  # Keeps values between 0 and 255

        # converts back into an image
        new_image = Image.fromarray(adjusted_array.astype(np.uint8))
        new_image.save(file)

        Buffle.Display.image.result(file, f"{Buffle.Display.Color.MAGENTA}noise{Buffle.Display.Color.RESET}", factor, 0)


def blur(files: str | list[str], factor: float):
    """
    Alters the texture's contrast and visibility.
    :param files: Target files' directory or location.
    :param factor: Strength of the alteration,
                values of 0.0 will not cause blurring
                and values less than or higher than 0.0 will increase blurring
    :type files: files: str | list[str]
    :type factor: float
    """
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        image = Image.open(file)

        # adds blur to image
        new_image = image.filter(ImageFilter.GaussianBlur(radius=factor))
        new_image.save(file)

        Buffle.Display.image.result(file, f"{Buffle.Display.Color.MAGENTA}blur{Buffle.Display.Color.RESET}", factor, 0)


def saturation(files: str | list[str], factor: float):
    """
    Alters the texture's saturation or color intensity.
    :param files: Target files' directory or location.
    :param factor: Strength of the alteration,
                values of 1.0 will not affect the saturation,
                values less than 1.0 will decrease saturation,
                and values higher than 1.0 will increase saturation.
    :type files: files: str | list[str]
    :type factor: float
    """
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        image = Image.open(file)
        new_image = ImageEnhance.Color(image).enhance(factor)  # alters image or texture
        new_image.save(file)

        Buffle.Display.image.result(file, f"{Buffle.Display.Color.MAGENTA}saturation{Buffle.Display.Color.RESET}", factor, 1)


def contrast(files: str | list[str], factor: float):
    """
    Alters the texture's contrast or range of brightness.
    :param files: Target files' directory or location.
    :param factor: Strength of the alteration,
                values of 1.0 will not affect the contrast,
                values less than 1.0 will decrease contrast,
                and values higher than 1.0 will increase contrast.
    :type files: files: str | list[str]
    :type factor: float
    """
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        image = Image.open(file)
        new_image = ImageEnhance.Contrast(image).enhance(factor)
        new_image.save(file)

        Buffle.Display.image.result(file, f"{Buffle.Display.Color.MAGENTA}contrast{Buffle.Display.Color.RESET}", factor, 1)


def brightness(files: str | list[str], factor: float):
    """
    Alters the texture's brightness or lightness.
    :param files: Target files' directory or location.
    :param factor: Strength of the alteration,
                values of 1.0 will not affect the brightness,
                values less than 1.0 will decrease brightness,
                and values higher than 1.0 will increase brightness.
    :type files: str | list[str]
    :type factor: float
    """
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        image = Image.open(file)
        new_image = ImageEnhance.Brightness(image).enhance(factor)
        new_image.save(file)

        Buffle.Display.image.result(file, f"{Buffle.Display.Color.MAGENTA}brightness{Buffle.Display.Color.RESET}", factor, 1)


def sharpness(files: str | list[str], factor: float):
    """
    Alters the texture's sharpness or clarity of detail.
    :param files: Target files' directory or location.
    :param factor: Strength of the alteration,
                values of 1.0 will not affect the sharpness,
                values less than 1.0 will decrease sharpness,
                and values higher than 1.0 will increase sharpness.
    :type files: str | list[str]
    :type factor: float
    """
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        image = Image.open(file)
        new_image = ImageEnhance.Sharpness(image).enhance(factor)
        new_image.save(file)

        Buffle.Display.image.result(file, f"{Buffle.Display.Color.MAGENTA}sharpness{Buffle.Display.Color.RESET}", factor, 1)


def resolution(files: str | list[str], factor: float):
    """
    Alters the texture's resolution or level of detail with pixels.
    :param files: Target files' directory or location.
    :param factor: Strength of the alteration,
                values of 1.0 will not affect the resolution,
                values less than 1.0 will decrease resolution,
                and values higher than 1.0 will increase resolution.
    :type files: str | list[str]
    :type factor: float
    """
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        image = Image.open(file)
        new_image = image.resize((int(image.width * factor), int(image.height * factor)), Image.Resampling.BILINEAR)
        new_image.save(file)

        Buffle.Display.image.result(file, f"{Buffle.Display.Color.MAGENTA}resolution{Buffle.Display.Color.RESET}", factor, 1)


def quality(files: str | list[str], factor: float):
    """
    Alters the texture's quality or detail.
    :param files: Target files' directory or location.
    :param factor: Strength of the alteration,
                values of 1.0 will not affect the quality,
                values less than 1.0 will decrease quality,
                and values higher than 1.0 will increase quality.
    :type files: str | list[str]
    :type factor: float
    """
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    for file in files:
        image = Image.open(file)
        image.save(file, quality=int(factor * 100))

        Buffle.Display.image.result(file, f"{Buffle.Display.Color.MAGENTA}quality{Buffle.Display.Color.RESET}", factor, 1)


