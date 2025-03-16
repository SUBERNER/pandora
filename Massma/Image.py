from Massma import random  # used for seeds
from Massma.Filter import *
import Massma
import numpy
import io
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

                    Massma.Display.image.result(file, "saturation", 0, factor)
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

                    Massma.Display.image.result(file, "contrast", 0, factor)

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

                    Massma.Display.image.result(file, "brightness", 0, factor)

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

                    Massma.Display.image.result(file, "sharpness", 0, factor)

            except Exception as e:
                Massma.Display.image.result_error(file, "sharpness", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "sharpness", e)


def invert(files: str | list[str], *, optimize: bool = False, masks: str | list[str] | None = None, resampling: int = 3,
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
                    # makes image inverse color
                    image = Image.open(file)
                    new_image = image  # version of image after changes

                    if masks:
                        # only effects areas of image that are in the white parts of the mask image
                        for mask in masks:
                            mask = Image.open(mask).convert("1")  # the mask can only be black or white pixels
                            mask = mask.resize(image.size, resampling)  # makes make equal the size of the image

                            mask_image = ImageOps.invert(image)  # alters image
                            new_image = Image.composite(mask_image, new_image, mask)

                    else:  # no mask is being used
                        new_image = ImageOps.invert(image)  # alters image

                    new_image.save(file, optimize=optimize)  # saves image

                    Massma.Display.image.result(file, "invert", False, True)

            except Exception as e:
                Massma.Display.image.result_error(file, "invert", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "invert", e)


def flip(files: str | list[str], *, optimize: bool = False,
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
                    # flips image vertically
                    image = Image.open(file)
                    new_image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)  # alters image
                    new_image.save(file, optimize=optimize)  # saves image

                    Massma.Display.image.result(file, "flip", False, True)

            except Exception as e:
                Massma.Display.image.result_error(file, "flip", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "flip", e)


def mirror(files: str | list[str], *, optimize: bool = False,
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
                    # flips image horizontally
                    image = Image.open(file)
                    new_image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)  # alters image
                    new_image.save(file, optimize=optimize)  # saves image

                    Massma.Display.image.result(file, "mirror", False, True)

            except Exception as e:
                Massma.Display.image.result_error(file, "mirror", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "mirror", e)


def layer(files: str | list[str]):
    pass


def spread(files: str | list[str]):
    pass


def crop(files: str | list[str]):
    pass


def noise(files: str | list[str]):
    pass


def blur(files: str | list[str], factor: float, *, optimize: bool = False, masks: str | list[str] | None = None, resampling: int = 3,
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
                    # makes image blurrier
                    image = Image.open(file)
                    new_image = image  # version of image after changes

                    if masks:
                        # only effects areas of image that are in the white parts of the mask image
                        for mask in masks:
                            mask = Image.open(mask).convert("1")  # the mask can only be black or white pixels
                            mask = mask.resize(image.size, resampling)  # makes make equal the size of the image

                            mask_image = image.filter(ImageFilter.GaussianBlur(radius=factor))  # alters image  # alters image
                            new_image = Image.composite(mask_image, new_image, mask)

                    else:  # no mask is being used
                        new_image = image.filter(ImageFilter.GaussianBlur(radius=factor))  # alters image

                    new_image.save(file, optimize=optimize)  # saves image

                    Massma.Display.image.result(file, "blur", 0, factor)

            except Exception as e:
                Massma.Display.image.result_error(file, "blur", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "blur", e)


def resize(files: str | list[str], size: tuple[int, int] | list[int], *, optimize: bool = False, resampling: int = 3,
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
                    # changes resolution of the image
                    image = Image.open(file)
                    new_image = image.resize((size[0], size[1]), resampling)
                    new_image.save(file, optimize=optimize)

                    Massma.Display.image.result(file, "resize", image.size, new_image.size)

            except Exception as e:
                Massma.Display.image.result_error(file, "resize", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "resize", e)


def resolution(files: str | list[str], factor: float, *, optimize: bool = False, resampling: int = 3,
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
                    # increases or decreases image resolution
                    image = Image.open(file)
                    new_image = image.resize((int(image.width * factor), int(image.height * factor)), resampling)
                    new_image.save(file, optimize=optimize)

                    Massma.Display.image.result(file, "resolution", image.size, new_image.size)

            except Exception as e:
                Massma.Display.image.result_error(file, "resolution", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "resolution", e)


def quality(files: str | list[str], factor: float, *, optimize: bool = False, resampling: int = 3, masks: str | list[str] | None = None,
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
                buffer = io.BytesIO()  # holds image while being worked on
                # checks if the file is in any of the ignores
                if ignores is None or not any(ignore(file) for ignore in ignores):
                    image = Image.open(file)
                    new_image = image  # placeholder for modified image
                    original_size = os.path.getsize(file)  # used for displaying size changes

                    if masks:
                        # apply each mask separately, like how brightness works
                        for mask in masks:
                            mask = Image.open(mask).convert("1")  # Convert mask to binary (black/white)
                            mask = mask.resize(image.size, resampling)  # Resize mask with high-quality resampling

                            # convert masked area to a JPEG
                            buffer_image = new_image.convert("RGB")  # convert image for JPEG processing
                            buffer_image.save(buffer, format="JPEG", quality=int(factor * 100))
                            mask_image = Image.open(buffer).convert(new_image.mode)  # Convert back to original mode

                            # apply the compressed image only in the masked areas
                            new_image = Image.composite(mask_image, new_image, mask)

                    else:  # no mask is being used
                        # convert the entire image to lower quality
                        image.convert("RGB").save(buffer, format="JPEG", quality=int(factor * 100))
                        new_image = Image.open(buffer).convert(image.mode)

                    new_image.save(file, format=image.format.upper(), quality=100, optimize=optimize)

                    Massma.Display.image.result(file, "quality", original_size, os.path.getsize(file))

            except Exception as e:
                Massma.Display.image.result_error(file, "quality", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "quality", e)


def tint(files: str | list[str]):
    pass