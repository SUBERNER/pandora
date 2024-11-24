from PIL import Image, ImageEnhance  # Pillow
import Buffle
# Used for altering single or non atlas textures


def rotate(file: str, degree: int, expand: bool = False, dump: bool = False):
    """
    Rotates the texture either clockwise or anti-clockwise.
    :param file: Target file's directory or location.
    :param degree: Degrees of rotation,
                values of 0 will not cause rotation,
                values less than 0 will cause clockwise rotation,
                and values higher than 0 will cause anti-clockwise rotation.
    :param expand: Expands resolution to fit entire image after rotation.
    :param dump: Moves files from the folder's directory to its parent's directory.
    :type file: str
    :type degree: int
    :type expand: bool
    :type dump: bool
    """
    image = Image.open(file)
    new_image = image.rotate(degree, expand=expand)

    new_image.save(file)

    if dump:
        file = Buffle.dump(file)
    Buffle.display_texture_results.result(file, "rotate", degree, 0)


def flip(file: str, horizontal: bool, vertical: bool, dump: bool = False):
    """
    Flips the texture either vertically or horizontally.
    :param file: Target file's directory or location.
    :param horizontal: Mirrors or flips the texture horizontally.
    :param vertical: Mirrors or flips texture vertically.
    :param dump: Moves files from the folder's directory to its parent's directory.
    :type file: str
    :type horizontal: bool
    :type vertical: bool
    :type dump: bool
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


def tint(file: str, color: tuple[int, int, int], alpha: float = 0.5, dump: bool = False):
    """
    Alters the texture's saturation or color intensity.
    :param file: Target file's directory or location.
    :param color: Strength of the alteration,
                values of 1.0 will not affect the saturation,
                values less than 1.0 will decrease saturation,
                and values higher than 1.0 will increase saturation.
    :param dump: Moves files from the folder's directory to its parent's directory.
    :type file: str
    :type color: tuple[int, int, int]
    :type alpha: float
    :type dump: bool
    """
    image = Image.open(file).convert('RGBA')
    overlay_image = Image.new('RGBA', image.size, color)

    new_image = Image.blend(image, overlay_image, alpha)  # adds a tint overlay to the image

    if "A" in image.getbands():  # checks for alpha channel
        # Composite over a solid background color
        background_image = Image.new("RGBA", image.size, (255, 255, 255) + (255,))
        new_image = Image.alpha_composite(background_image, new_image)

    new_image.convert('RGB').save(file)  # converts and saves new image

    if dump:  # dumps file to parent folder
        file = Buffle.dump(file)
    Buffle.display_texture_results.result(file, "saturation", (color, alpha), ((0, 0, 0), 0))


def saturation(file: str, factor: float, dump: bool = False):
    """
    Alters the texture's saturation or color intensity.
    :param file: Target file's directory or location.
    :param factor: Strength of the alteration,
                values of 1.0 will not affect the saturation,
                values less than 1.0 will decrease saturation,
                and values higher than 1.0 will increase saturation.
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
    Alters the texture's contrast or range of brightness.
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
    Alters the texture's brightness or lightness.
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
    Alters the texture's sharpness or clarity of detail.
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
    Alters the texture's resolution or level of detail with pixels.
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
    new_image = image.resize((int(image.width * factor), int(image.height * factor)), Image.Resampling.BILINEAR)
    new_image.save(file)

    if dump:
        file = Buffle.dump(file)
    Buffle.display_texture_results.result(file, "resolution", factor, 1)


def quality(file: str, factor: float, dump: bool = False):
    """
    Alters the texture's quality or detail.
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


