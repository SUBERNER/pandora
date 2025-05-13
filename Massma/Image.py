from Massma import random  # used for seeds
from Massma.Filter import *
import Massma
import numpy
from PIL import Image, ImageEnhance, ImageFilter, ImageOps  # Pillow


def saturation(files: str | list[str], factor: float, *, optimize: bool = False, masks: str | list[str] | None = None, resampling: int = 3, chance_files: float = 1, chance_masks: float = 1, chance_total: float = 1,
               ignores: Ignore | list[Ignore] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes files always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            masks = masks if isinstance(masks, list) else ([masks] if masks else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.image.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if chance_files >= random.random():  # test if a file will be edited
                        # checks if the file is in any of the ignores
                        if ignores is None or not any(ignore(file) for ignore in ignores):
                            # adds saturation to image
                            image = Image.open(file)
                            new_image = image  # version of image after changes

                            if masks:
                                # only effects areas of image that are in the white parts of the mask image
                                for mask in masks:
                                    if chance_masks >= random.random():  # test if a file's mask will be edited
                                        mask = Image.open(mask).convert("L")  # the mask can only be black or white pixels
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


def contrast(files: str | list[str], factor: float, *, optimize: bool = False, masks: str | list[str] | None = None, resampling: int = 3, chance_files: float = 1, chance_masks: float = 1, chance_total: float = 1,
             ignores: Ignore | list[Ignore] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes files always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            masks = masks if isinstance(masks, list) else ([masks] if masks else [])

            # gets size of the largest path for better result formatting
            Massma.Display.image.set_source_length(max(files, key=len))

            for file in files:
                try:
                    if chance_files >= random.random():  # test if a file will be edited
                        # checks if the file is in any of the ignores
                        if ignores is None or not any(ignore(file) for ignore in ignores):
                            # adds contrast to image
                            image = Image.open(file)
                            new_image = image  # version of image after changes

                            if masks:
                                # only effects areas of image that are in the white parts of the mask image
                                for mask in masks:
                                    if chance_masks >= random.random():  # test if a file's mask will be edited
                                        mask = Image.open(mask).convert("L")  # the mask can only be black or white pixels
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


def brightness(files: str | list[str], factor: float, *, optimize: bool = False, masks: str | list[str] | None = None, resampling: int = 3, chance_files: float = 1, chance_masks: float = 1, chance_total: float = 1,
               ignores: Ignore | list[Ignore] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes files always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            masks = masks if isinstance(masks, list) else ([masks] if masks else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.image.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if chance_files >= random.random():  # test if a file will be edited
                        # checks if the file is in any of the ignores
                        if ignores is None or not any(ignore(file) for ignore in ignores):
                            # adds brightness to image
                            image = Image.open(file)
                            new_image = image  # version of image after changes

                            if masks:
                                # only effects areas of image that are in the white parts of the mask image
                                for mask in masks:
                                    if chance_masks >= random.random():  # test if a file's mask will be edited
                                        mask = Image.open(mask).convert("L")  # the mask can only be black or white pixels
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


def sharpness(files: str | list[str], factor: float, *, optimize: bool = False, masks: str | list[str] | None = None, resampling: int = 3, chance_files: float = 1, chance_masks: float = 1, chance_total: float = 1,
              ignores: Ignore | list[Ignore] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes files always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            masks = masks if isinstance(masks, list) else ([masks] if masks else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.image.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if chance_files >= random.random():  # test if a file will be edited
                        # checks if the file is in any of the ignores
                        if ignores is None or not any(ignore(file) for ignore in ignores):
                            # adds sharpness to image
                            image = Image.open(file)
                            new_image = image  # version of image after changes

                            if masks:
                                # only effects areas of image that are in the white parts of the mask image
                                for mask in masks:
                                    if chance_masks >= random.random():  # test if a file's mask will be edited
                                        mask = Image.open(mask).convert("L")  # the mask can only be black or white pixels
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


def invert(files: str | list[str], *, optimize: bool = False, masks: str | list[str] | None = None, resampling: int = 3, chance_files: float = 1, chance_masks: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes files always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            masks = masks if isinstance(masks, list) else ([masks] if masks else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.image.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if chance_files >= random.random():  # test if a file will be edited
                        # checks if the file is in any of the ignores
                        if ignores is None or not any(ignore(file) for ignore in ignores):
                            # makes image inverse color
                            image = Image.open(file)
                            new_image = image  # version of image after changes

                            if masks:
                                # only effects areas of image that are in the white parts of the mask image
                                for mask in masks:
                                    if chance_masks >= random.random():  # test if a file's mask will be edited
                                        mask = Image.open(mask).convert("L")  # the mask can only be black or white pixels
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


def flip(files: str | list[str], *, optimize: bool = False, chance_files: float = 1, chance_total: float = 1,
         ignores: Ignore | list[Ignore] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes files always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.image.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if chance_files >= random.random():  # test if a file will be edited
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


def mirror(files: str | list[str], *, optimize: bool = False, chance_files: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes files always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.image.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if chance_files >= random.random():  # test if a file will be edited
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


def rotate(files: str | list[str], degree: int, *, optimize: bool = False, resampling: int = 3, expand: bool = False, chance_files: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes files always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.image.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if chance_files >= random.random():  # test if a file will be edited
                        # checks if the file is in any of the ignores
                        if ignores is None or not any(ignore(file) for ignore in ignores):
                            # flips image horizontally
                            image = Image.open(file)
                            new_image = image.rotate(-degree, expand=expand, resample=resampling)  # alters image
                            new_image.save(file, optimize=optimize)  # saves image

                            Massma.Display.image.result(file, "rotate", 0, degree)

                except Exception as e:
                    Massma.Display.image.result_error(file, "rotate", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "rotate", e)


def layer(files: str | list[str], layers: str | list[str], *, optimize: bool = False, masks: str | list[str] | None = None, resampling: int = 3, chance_files: float = 1, chance_masks: float = 1, chance_total: float = 1,
          ignores: Ignore | list[Ignore] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes files always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            masks = masks if isinstance(masks, list) else ([masks] if masks else [])
            layers = layers if isinstance(layers, list) else ([layers] if layers else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.image.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if chance_files >= random.random():  # test if a file will be edited
                        # checks if the file is in any of the ignores
                        if ignores is None or not any(ignore(file) for ignore in ignores):
                            # adds more images to existing images
                            image = Image.open(file)
                            new_image = image  # version of image after changes

                            for layer in layers:  # goes through and adds layers in the order provided in the layer list
                                layer_image = Image.open(layer).convert("RGBA")  # makes sure its transparent
                                layer_image = layer_image.resize(image.size, resampling)  # makes make equal the size of the image

                                if masks:
                                    # only effects areas of image that are in the white parts of the mask image
                                    for mask in masks:
                                        if chance_masks >= random.random():  # test if a file's mask will be edited
                                            mask = Image.open(mask).convert("L")  # makes sure image is grayscale
                                            mask = mask.resize(image.size, resampling)  # makes make equal the size of the image
                                            mask = mask.split()[3]  # get the alpha channel for better masking

                                            new_image.paste(layer_image, (0, 0), mask)  # add layer onto the image in order
                                else:
                                    new_image.paste(layer_image, (0, 0), layer_image.split()[3])  # add layer onto the image in order

                            new_image.save(file, optimize=optimize)

                            Massma.Display.image.result(file, "layer", False, True)

                except Exception as e:
                    Massma.Display.image.result_error(file, "layer", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "layer", e)


def crop(files: str | list[str], dimensions: tuple[int, int, int, int], *, optimize: bool = False, chance_files: float = 1, chance_total: float = 1,
         ignores: Ignore | list[Ignore] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes files always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.image.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if chance_files >= random.random():  # test if a file will be edited
                        # checks if the file is in any of the ignores
                        if ignores is None or not any(ignore(file) for ignore in ignores):
                            # crops image
                            image = Image.open(file)
                            new_image = image.crop(dimensions)
                            new_image.save(file, optimize=optimize)  # saves image

                            Massma.Display.image.result(file, "crop", image.size, new_image.size)

                except Exception as e:
                    Massma.Display.image.result_error(file, "crop", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "crop", e)


def noise(files: str | list[str], mean: float, standard_deviation: float, *, optimize: bool = False, masks: str | list[str] | None = None, resampling: int = 3, chance_files: float = 1, chance_masks: float = 1, chance_total: float = 1,
          ignores: Ignore | list[Ignore] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes files always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            masks = masks if isinstance(masks, list) else ([masks] if masks else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.image.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if chance_files >= random.random():  # test if a file will be edited
                        # checks if the file is in any of the ignores
                        if ignores is None or not any(ignore(file) for ignore in ignores):
                            # makes image blurrier
                            image = Image.open(file)
                            new_image = image  # version of image after changes

                            # Calculates the noice
                            array_image = numpy.array(image)  # converts image into an array
                            noise = numpy.random.normal(mean, standard_deviation, array_image.shape)  # creates the noise map
                            noise_image = array_image + noise
                            noise_image = numpy.clip(noise_image, 0, 255).astype(numpy.uint8)

                            if masks:
                                # only effects areas of the image that are in the white parts of the mask image
                                for mask in masks:
                                    if chance_masks >= random.random():  # test if a file's mask will be edited
                                        mask = Image.open(mask).convert("L")  # the mask can only be black or white pixels
                                        mask = mask.resize(image.size, resampling)  # makes make equal the size of the image

                                        mask_image = Image.fromarray(noise_image)  # alters image
                                        new_image = Image.composite(mask_image, new_image, mask)

                            else:  # no mask is being used
                                new_image = Image.fromarray(noise_image)  # alters image

                            new_image.save(file, optimize=optimize)  # saves image

                            Massma.Display.image.result(file, "noise", [0, 0], [mean, standard_deviation])

                except Exception as e:
                    Massma.Display.image.result_error(file, "noise", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "noise", e)


def blur(files: str | list[str], factor: float, *, optimize: bool = False, masks: str | list[str] | None = None, resampling: int = 3, chance_files: float = 1, chance_masks: float = 1, chance_total: float = 1,
         ignores: Ignore | list[Ignore] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes files always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])
            masks = masks if isinstance(masks, list) else ([masks] if masks else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.image.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if chance_files >= random.random():  # test if a file will be edited
                        # checks if the file is in any of the ignores
                        if ignores is None or not any(ignore(file) for ignore in ignores):
                            # makes image blurrier
                            image = Image.open(file)
                            new_image = image  # version of image after changes

                            if masks:
                                # only effects areas of image that are in the white parts of the mask image
                                for mask in masks:
                                    if chance_masks >= random.random():  # test if a file's mask will be edited
                                        mask = Image.open(mask).convert("L")  # the mask can only be black or white pixels
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


def resize(files: str | list[str], dimensions: tuple[int, int] | list[int], *, optimize: bool = False, resampling: int = 3, chance_files: float = 1, chance_total: float = 1,
           ignores: Ignore | list[Ignore] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes files always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.image.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if chance_files >= random.random():  # test if a file will be edited
                        # checks if the file is in any of the ignores
                        if ignores is None or not any(ignore(file) for ignore in ignores):
                            # changes resolution of the image
                            image = Image.open(file)
                            new_image = image.resize((dimensions[0], dimensions[1]), resampling)
                            new_image.save(file, optimize=optimize)

                            Massma.Display.image.result(file, "resize", image.size, new_image.size)

                except Exception as e:
                    Massma.Display.image.result_error(file, "resize", e)

    except Exception as e:
        Massma.Display.image.result_error(len(files), "resize", e)


def resolution(files: str | list[str], factor: float, *, optimize: bool = False, resampling: int = 3, chance_files: float = 1, chance_total: float = 1,
               ignores: Ignore | list[Ignore] | None = None):
    try:
        if chance_total >= random.random():  # test if method will happen
            # makes files always a list
            files = [files] if isinstance(files, str) else files
            ignores = ignores if isinstance(ignores, list) else ([ignores] if ignores else [])

            # gets size of the largest path for better result formatting
            file_paths = [os.path.abspath(file) for file in files]  # makes sures the full file path is given
            Massma.Display.image.set_source_length(max(file_paths, key=len))

            for file in files:
                try:
                    if chance_files >= random.random():  # test if a file will be edited
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