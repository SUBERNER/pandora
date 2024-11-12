from PIL import Image, ImageEnhance # Pillow
import Buffle
# Used for altering single / non atlas textures or images


def rotate(file: str, degree: int, expand: bool = False, dump: bool = False):
    """
    Rotates the texture or image
    :param file: Target file's directory / location
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
    Flips / mirrors the texture or image
    :param file: Target file's directory / location
    :param horizontal: Flips / mirrors texture or image horizontally
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
    Alters the texture's or image's saturation
    :param file: Target file's directory / location
    :param factor: Strength of the alteration
    :param dump: Moves files from the folder's directory to its parent's directory
    """
    image = Image.open(file)
    new_image = ImageEnhance.Color(image).enhance(factor)

    new_image.save(file)

    if dump:
        file = Buffle.dump(file)
    Buffle.display_texture_results.result(file, "saturation", factor, 1)


def contrast(file: str, factor: float, dump: bool = False):
    """
    Alters the texture's or image's contrast
    :param file: Target file's directory / location
    :param factor: Strength of the alteration
    :param dump: Moves files from the folder's directory to its parent's directory
    """
    image = Image.open(file)
    new_image = ImageEnhance.Contrast(image).enhance(factor)

    new_image.save(file)

    if dump:
        file = Buffle.dump(file)
    Buffle.display_texture_results.result(file, "contrast", factor, 1)


def brightness(file: str, factor: float, dump: bool = False):
    """
    Alters the texture's or image's brightness
    :param file: Target file's directory / location
    :param factor: Strength of the alteration
    :param dump: Moves files from the folder's directory to its parent's directory
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
    Alters the texture's or image's sharpness
    :param file: Target file's directory / location
    :param factor: Strength of the alteration
    :param dump: Moves files from the folder's directory to its parent's directory
    """
    image = Image.open(file)
    new_image = ImageEnhance.Sharpness(image).enhance(factor)

    new_image.save(file)

    if dump:
        file = Buffle.dump(file)
    Buffle.display_texture_results.result(file, "sharpness", factor, 1)


def resolution(file: str, factor: float, dump: bool = False):
    """
    Alters the texture's or image's resolution
    :param file: Target file's directory / location
    :param factor: Strength of the alteration
    :param dump: Moves files from the folder's directory to its parent's directory
    """
    image = Image.open(file)
    new_image = image.resize((int(image.width * factor), int(image.height * factor)), Image.Resampling.NEAREST)

    new_image.save(file)

    if dump:
        file = Buffle.dump(file)
    Buffle.display_texture_results.result(file, "resolution", factor, 1)


def quality(file: str, factor: float, dump: bool = False):
    """
    Alters the texture's or image's quality
    :param file: Target file's directory / location
    :param factor: Strength of the alteration
    :param dump: Moves files from the folder's directory to its parent's directory
    """
    image = Image.open(file)

    image.save(file, quality=int(factor * 100))

    if dump:
        file = Buffle.dump(file)
    Buffle.display_texture_results.result(file, "quality", factor, 1)




