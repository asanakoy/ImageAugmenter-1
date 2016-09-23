"""Script to plot example augmentations generated by the ImageAugmenter."""
from __future__ import print_function

# make sure that ImageAugmenter can be imported from parent directory
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import numpy as np
from imageaugmenter import ImageAugmenter
from scipy import misc
from skimage import data


def main():
    """Plot example augmentations for Lena and an image loaded from a file."""

    # try on a lena image
    print('Plotting float lena, preserve range')
    image = data.lena().astype(float)
    augmenter = ImageAugmenter(image.shape[0], image.shape[1],
                               hflip=True, vflip=True,
                               scale_to_percent=1.3, scale_axis_equally=False,
                               rotation_deg=25, shear_deg=10,
                               translation_x_px=5, translation_y_px=5,
                               preserve_range=True)
    augmenter.plot_image(image, 10)

    print('Plotting chameleon')
    # check loading of images from file and augmenting them
    image = misc.imread("chameleon.png")
    augmenter = ImageAugmenter(image.shape[1], image.shape[0],
                               hflip=True, vflip=True,
                               scale_to_percent=1.3, scale_axis_equally=False,
                               rotation_deg=25, shear_deg=10,
                               translation_x_px=5, translation_y_px=5)

    augmenter.plot_image(image/255.0, 50)

    print('Plotting chameleon with channel_is_first_axis=True')
    # move the channel from index 2 (3rd position) to index 0 (1st position)
    # so (y, x, rgb) becomes (rgb, y, x)
    # try if it still works
    image = np.rollaxis(image, 2, 0)
    augmenter = ImageAugmenter(image.shape[2], image.shape[1],
                               hflip=True, vflip=True,
                               scale_to_percent=1.3, scale_axis_equally=False,
                               rotation_deg=25, shear_deg=10,
                               translation_x_px=5, translation_y_px=5,
                               channel_is_first_axis=True)
    augmenter.plot_image(image, 50)

if __name__ == "__main__":
    main()
