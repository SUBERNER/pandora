from PIL import Image, ImageEnhance  # Pillow


#  rotates the texture or image
def rotate(file: str, degree: int):
    image = Image.open(file)
    new_image = image.rotate(degree)
    new_image.save(file)


#  flips the texture or image
def flip(file, horizontal: bool, vertical: bool):
    image = Image.open(file)
    new_image = None

    if not horizontal and not vertical:
        print(file + "")
        return
    if horizontal:
        new_image = image.transpose(image.transpose.FLIP_LEFT_RIGHT)
    if vertical:
        new_image = image.transpose(image.transpose.FLIP_TOP_BOTTOM)

    new_image.save(file)


# alters the texture's or image's saturation
def saturation(file: str, factor: float):
    image = Image.open(file)
    new_image = ImageEnhance.Color(image).enhance(factor)
    new_image = ImageEnhance.Color(image)
    new_image.save(file)


# alters the texture's or image's contrast
def contrast(file: str, factor: float):
    image = Image.open(file)
    new_image = ImageEnhance.Contrast(image).enhance(factor)
    new_image.save(file)


# alters the texture's or image's brightness
def brightness(file: str, factor: float):
    image = Image.open(file)
    new_image = ImageEnhance.Brightness(image).enhance(factor)
    new_image.save(file)


# alters the texture's or image's sharpness
def sharpness(file: str, factor: float):
    image = Image.open(file)
    new_image = ImageEnhance.Sharpness(image).enhance(factor)
    new_image.save(file)


# alters the texture's or image's resolution
def resolution(file: str, factor: float):
    image = Image.open(file)
    new_image = image.resize(image.height * factor, image.width * factor)
    new_image.save(file)


# alters the texture's or image's resolution
def quality(file: str, factor: float):
    image = Image.open(file)
    image.save(file, quality=factor * 100)





