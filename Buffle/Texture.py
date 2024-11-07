from PIL import Image, ImageEnhance  # Pillow
import Buffle


# rotates the texture or image
def rotate(file: str, degree: int):
    image = Image.open(file)
    new_image = image.rotate(degree, expand=True)

    new_image.save(file)

    if Buffle.display_all_results():
        Buffle.result(file, "rotate", degree, 0)


#  flips the texture or image
def flip(file, horizontal: bool, vertical: bool):
    image = Image.open(file)
    new_image = Image.open(file)

    if horizontal:
        new_image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    if vertical:
        new_image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

    new_image.save(file)

    if Buffle.display_texture_results():
        Buffle.result(file, "flip", [horizontal, vertical], [False, False])


# alters the texture's or image's saturation
def saturation(file: str, factor: float):
    image = Image.open(file)
    new_image = ImageEnhance.Color(image).enhance(factor)

    new_image.save(file)

    if Buffle.display_texture_results():
        Buffle.result(file, "saturation", factor, 1)


# alters the texture's or image's contrast
def contrast(file: str, factor: float):
    image = Image.open(file)
    new_image = ImageEnhance.Contrast(image).enhance(factor)

    new_image.save(file)

    if Buffle.display_texture_results():
        Buffle.result(file, "contrast", factor, 1)


# alters the texture's or image's brightness
def brightness(file: str, factor: float):
    image = Image.open(file)
    new_image = ImageEnhance.Brightness(image).enhance(factor)

    new_image.save(file)

    if Buffle.display_texture_results():
        Buffle.result(file, "brightness", factor, 1)


# alters the texture's or image's sharpness
def sharpness(file: str, factor: float):
    image = Image.open(file)
    new_image = ImageEnhance.Sharpness(image).enhance(factor)

    new_image.save(file)

    if Buffle.display_texture_results():
        Buffle.__result(file, "sharpness", factor, 1)


# alters the texture's or image's resolution
def resolution(file: str, factor: float):
    image = Image.open(file)
    new_image = image.resize((int(image.width * factor), int(image.height * factor)), Image.Resampling.NEAREST)

    new_image.save(file)

    if Buffle.display_texture_results():
        Buffle.result(file, "resolution", factor, 1)


# alters the texture's or image's resolution
def quality(file: str, factor: float):
    image = Image.open(file)

    image.save(file, quality=int(factor * 100))

    if Buffle.display_texture_results():
        Buffle.result(file, "quality", factor, 1)




