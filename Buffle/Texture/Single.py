from PIL import Image, ImageEnhance # Pillow
import Buffle
# Used for altering single / non atlas textures or images


def rotate(file: str, degree: int, expand: bool = False, dump: bool = False):
    """
    Rotates the texture or image either
    :param file: Target file's directory
    :param degree: Degrees of rotation anti-clockwise
    :param expand: Expands image to entire fit the rotated texture or image
    :param dump: Moves files from the folder's directory to its parent's directory
    """
    image = Image.open(file)
    new_image = image.rotate(degree, expand=expand)

    new_image.save(file)

    if dump:
        file = Buffle.dump(file)
    Buffle.display_texture_results.result(file, "rotate", degree, 0)


#  flips the texture or image
def flip(file, horizontal: bool, vertical: bool, dump: bool = False):
    """
    Mirrors the texture or image
    :param file: Target file's directory
    :param horizontal: Mirrors the texture or image horizontally
    :param vertical: Flips / mirrors texture or image vertically
    :param dump: Moves files from the folder's directory to its parent's directory
    """
    image = Image.open(file)
    new_image = Image.open(file)

    if horizontal:
        new_image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    if vertical:
        new_image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

    new_image.save(file)

    if dump:
        file = Buffle.dump(file)
    Buffle.display_texture_results.result(file, "flip", [horizontal, vertical], [False, False])


def saturation(file: str, factor: float, dump: bool = False):
    """
    Alters the texture's or image's saturation or color intensity.
    :param file: Target file's directory or location.
    :param factor: Strength of the alteration,
                values of 1.0 will not affect the saturation,
                values less than 1.0 will decrease saturation,
                and values higher than 1.0 will increase saturation.
    :type factor: float
    :param dump: Moves files from the folder's directory to its parent's directory.
    :type file: str
    :type factor: float
    :type dump: bool
    """
    image = Image.open(file)
    new_image = ImageEnhance.Color(image).enhance(factor)  # alters image or texture
    new_image.save(file)

    if dump:  # dumps file to parent folder
        file = Buffle.dump(file)
    Buffle.display_texture_results.result(file, "saturation", factor, 1)


def contrast(file: str, factor: float, dump: bool = False):
    """
    Alters the texture's or image's contrast or range of brightness.
    :param file: Target file's directory or location.
    :param factor: Strength of the alteration,
                values of 1.0 will not affect the contrast,
                values less than 1.0 will decrease contrast,
                and values higher than 1.0 will increase contrast.
    :param dump: Moves files from the folder's directory to its parent's directory.
    :type file: str
    :type factor: float
    :type dump: bool
    """
    image = Image.open(file)
    new_image = ImageEnhance.Contrast(image).enhance(factor)
    new_image.save(file)

    if dump:
        file = Buffle.dump(file)
    Buffle.display_texture_results.result(file, "contrast", factor, 1)


def brightness(file: str, factor: float, dump: bool = False):
    """
    Alters the texture's or image's brightness or lightness.
    :param file: Target file's directory or location.
    :param factor: Strength of the alteration,
                values of 1.0 will not affect the brightness,
                values less than 1.0 will decrease brightness,
                and values higher than 1.0 will increase brightness.
    :param dump: Moves files from the folder's directory to its parent's directory.
    :type file: str
    :type factor: float
    :type dump: bool
    """
    image = Image.open(file)
    new_image = ImageEnhance.Brightness(image).enhance(factor)
    new_image.save(file)

    if dump:
        print(file)
        file = Buffle.dump(file)
    Buffle.display_texture_results.result(file, "brightness", factor, 1)


def sharpness(file: str, factor: float, dump: bool = False):
    """
    Alters the texture's or image's sharpness or clarity of detail.
    :param file: Target file's directory or location.
    :param factor: Strength of the alteration,
                values of 1.0 will not affect the sharpness,
                values less than 1.0 will decrease sharpness,
                and values higher than 1.0 will increase sharpness.
    :param dump: Moves files from the folder's directory to its parent's directory.
    :type file: str
    :type factor: float
    :type dump: bool
    """
    image = Image.open(file)
    new_image = ImageEnhance.Sharpness(image).enhance(factor)
    new_image.save(file)

    if dump:
        file = Buffle.dump(file)
    Buffle.display_texture_results.result(file, "sharpness", factor, 1)


def resolution(file: str, factor: float, dump: bool = False):
    """
    Alters the texture's or image's resolution or level of detail with pixels.
    :param file: Target file's directory or location.
    :param factor: Strength of the alteration,
                values of 1.0 will not affect the resolution,
                values less than 1.0 will decrease resolution,
                and values higher than 1.0 will increase resolution.
    :param dump: Moves files from the folder's directory to its parent's directory.
    :type file: str
    :type factor: float
    :type dump: bool
    """
    image = Image.open(file)
    new_image = image.resize((int(image.width * factor), int(image.height * factor)), Image.Resampling.NEAREST)
    new_image.save(file)

    if dump:
        file = Buffle.dump(file)
    Buffle.display_texture_results.result(file, "resolution", factor, 1)


def quality(file: str, factor: float, dump: bool = False):
    """
    Alters the texture's or image's quality or detail.
    :param file: Target file's directory or location.
    :param factor: Strength of the alteration,
                values of 1.0 will not affect the quality,
                values less than 1.0 will decrease quality,
                and values higher than 1.0 will increase quality.
    :param dump: Moves files from the folder's directory to its parent's directory.
    :type file: str
    :type factor: float
    :type dump: bool
    """
    image = Image.open(file)
    image.save(file, quality=int(factor * 100))

    if dump:
        file = Buffle.dump(file)
    Buffle.display_texture_results.result(file, "quality", factor, 1)




