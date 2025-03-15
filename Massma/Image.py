from Massma import random  # used for seeds
from Massma.Filter import *
import Massma
import numpy  # used for displaying variation
from scipy import ndimage  # used for displaying variation
from PIL import Image, ImageEnhance, ImageFilter, ImageOps  # Pillow


def saturation(files: str | list[str], factor: float, *, optimize: bool = False, masks: str | list[str] | None = None, resampling: int = 3,
               ignores: Ignore | list[Ignore] | None = None):
    # makes files always a list
    files = [files] if isinstance(files, str) else files
    ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
    masks = masks if isinstance(masks, list) else ([masks] if masks else [])
    try:
        # gets size of the largest path for better result formatting
        Massma.Display.image.set_source_length(max(files, key=len))

        for file in files:
            try:
                # checks if the file is in any of the ignores
                if ignores is None or not any(ignore(file) for ignore in ignores):
                    # adds saturation to image
                    image = Image.open(file)
                    new_image = image  # version of image after changes

                    if masks:
                        # only effects areas of image that are in the white parts of the mask image
                        for mask in masks:

                            mask = Image.open(mask).convert("1")  # the mask can only be black or white pixels
                            mask = mask.resize(image.size, resampling)  # makes make equal the size of the image

                            mask_image = ImageEnhance.Color(image).enhance(factor)  # alters image
                            new_image = Image.composite(mask_image, new_image, mask)

                    else:  # no mask is being used
                        new_image = ImageEnhance.Color(image).enhance(factor)  # alters image

                    new_image.save(file, optimize=optimize)  # saves image

                    # determines the changes made by method to display
                    # calculating and displaying the mean saturation of the image
                    hsv_image = image.convert("HSV")
                    hsv_new_image = new_image.convert("HSV")
                    image_mean = numpy.mean(numpy.array(hsv_image)[:, :, 1])
                    new_image_mean = numpy.mean(numpy.array(hsv_new_image)[:, :, 1])

                    Massma.Display.image.result(file, "saturation", image_mean, new_image_mean)
            except Exception as e:
                Massma.Display.image.result_error(file, "saturation", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "saturation", e)


def contrast(files: str | list[str], factor: float, *, optimize: bool = False, masks: str | list[str] | None = None, resampling: int = 3,
             ignores: Ignore | list[Ignore] | None = None):
    # makes files always a list
    files = [files] if isinstance(files, str) else files
    ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
    try:
        # gets size of the largest path for better result formatting
        Massma.Display.image.set_source_length(max(files, key=len))

        for file in files:
            try:
                # checks if the file is in any of the ignores
                if ignores is None or not any(ignore(file) for ignore in ignores):
                    # adds contrast to image
                    image = Image.open(file)
                    new_image = image  # version of image after changes

                    if masks:
                        # only effects areas of image that are in the white parts of the mask image
                        for mask in masks:
                            mask = Image.open(mask).convert("1")  # the mask can only be black or white pixels
                            mask = mask.resize(image.size, resampling)  # makes make equal the size of the image

                            mask_image = ImageEnhance.Contrast(image).enhance(factor)  # alters image
                            new_image = Image.composite(mask_image, new_image, mask)

                    else:  # no mask is being used
                        new_image = ImageEnhance.Contrast(image).enhance(factor)  # alters image

                    new_image.save(file, optimize=optimize)  # saves image

                    # determines the changes made by method to display
                    # calculating and displaying the standard deviation between brightness of the image
                    grayscale_image = image.convert("L")
                    grayscale_new_image = new_image.convert("L")
                    image_deviation = numpy.std(numpy.array(grayscale_image))
                    new_image_deviation = numpy.std(numpy.array(grayscale_new_image))

                    Massma.Display.image.result(file, "contrast", image_deviation, new_image_deviation)

            except Exception as e:
                Massma.Display.image.result_error(file, "contrast", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "contrast", e)


def brightness(files: str | list[str], factor: float, *, optimize: bool = False, masks: str | list[str] | None = None, resampling: int = 3,
               ignores: Ignore | list[Ignore] | None = None):
    # makes files always a list
    files = [files] if isinstance(files, str) else files
    ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
    try:
        # gets size of the largest path for better result formatting
        Massma.Display.image.set_source_length(max(files, key=len))

        for file in files:
            try:
                # checks if the file is in any of the ignores
                if ignores is None or not any(ignore(file) for ignore in ignores):
                    # adds brightness to image
                    image = Image.open(file)
                    new_image = image  # version of image after changes

                    if masks:
                        # only effects areas of image that are in the white parts of the mask image
                        for mask in masks:
                            mask = Image.open(mask).convert("1")  # the mask can only be black or white pixels
                            mask = mask.resize(image.size, resampling)  # makes make equal the size of the image

                            mask_image = ImageEnhance.Brightness(image).enhance(factor)  # alters image
                            new_image = Image.composite(mask_image, new_image, mask)

                    else:  # no mask is being used
                        new_image = ImageEnhance.Brightness(image).enhance(factor)  # alters image

                    new_image.save(file, optimize=optimize)  # saves image

                    # determines the changes made by method to display
                    # calculating and displaying the mean brightness of the image
                    grayscale_image = image.convert("L")
                    grayscale_new_image = new_image.convert("L")
                    image_mean = numpy.mean(numpy.array(grayscale_image))
                    new_image_mean = numpy.mean(numpy.array(grayscale_new_image))

                    Massma.Display.image.result(file, "brightness", image_mean, new_image_mean)

            except Exception as e:
                Massma.Display.image.result_error(file, "brightness", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "brightness", e)


def sharpness(files: str | list[str], factor: float, *, optimize: bool = False, masks: str | list[str] | None = None, resampling: int = 3,
              ignores: Ignore | list[Ignore] | None = None):
    # makes files always a list
    files = [files] if isinstance(files, str) else files
    ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
    try:
        # gets size of the largest path for better result formatting
        Massma.Display.image.set_source_length(max(files, key=len))

        for file in files:
            try:
                # checks if the file is in any of the ignores
                if ignores is None or not any(ignore(file) for ignore in ignores):
                    # adds sharpness to image
                    image = Image.open(file)
                    new_image = image  # version of image after changes

                    if masks:
                        # only effects areas of image that are in the white parts of the mask image
                        for mask in masks:
                            mask = Image.open(mask).convert("1")  # the mask can only be black or white pixels
                            mask = mask.resize(image.size, resampling)  # makes make equal the size of the image

                            mask_image = ImageEnhance.Sharpness(image).enhance(factor)  # alters image
                            new_image = Image.composite(mask_image, new_image, mask)

                    else:  # no mask is being used
                        new_image = ImageEnhance.Sharpness(image).enhance(factor)  # alters image

                    new_image.save(file, optimize=optimize)  # saves image

                    # determines the changes made by method to display
                    # calculating and displaying the variance of the laplacian of the image
                    # <<<FIND BETTER WAY TO MEASURE SHARPNESS>>>
                    gray_image = image.convert('L')  # Convert to grayscale
                    gray_new_image = new_image.convert('L')
                    image_array = numpy.array(gray_image)
                    new_image_array = numpy.array(gray_new_image)
                    laplacian_image = ndimage.laplace(image_array)
                    laplacian_new_image = ndimage.laplace(new_image_array)
                    image_variation = numpy.var(laplacian_image)
                    new_image_variation = numpy.var(laplacian_new_image)

                    Massma.Display.image.result(file, "sharpness", image_variation, new_image_variation)

            except Exception as e:
                Massma.Display.image.result_error(file, "sharpness", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "sharpness", e)


def invert(files: str | list[str]):
    pass


def flip(files: str | list[str]):
    pass


def mirror(files: str | list[str]):
    pass


def layer(files: str | list[str]):
    pass


def spread(files: str | list[str]):
    pass


def crop(files: str | list[str]):
    pass


def noise(files: str | list[str]):
    pass


def blur(files: str | list[str]):
    pass


def resize(files: str | list[str]):
    pass


def resolution(files: str | list[str]):
    pass


def quality(files: str | list[str]):
    pass


def tint(files: str | list[str]):
    pass