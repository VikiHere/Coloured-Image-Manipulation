'''
edges preserved while larger regions are smoothed out
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import

        NOTE v2: as specified, PIL also used to provide Median Filter capability
'''

import numpy as np
import sys
from PIL import Image, ImageFilter

def main(*arg):
    imgName = input("Please enter image name: ")

    # import image 
    img = Image.open(imgName)   # note: NOT using numpy, keeping everything as a PIL object
    final = cartoonify_pt1(img)
      
    final.show()
    final.save('blurred.png')

# Smoothing out the picture to get cartoony effect
# note: img is a PIL object, not numpy array!
def cartoonify_pt1(img):
    # applying median filter with 3x3 kernel
    med3 = img.filter(ImageFilter.MedianFilter(3))

    # applying median filter with 5x5 kernel
    med5 = med3.filter(ImageFilter.MedianFilter(5))

    # applying median filter with 5x5 kernel
    med7 = med5.filter(ImageFilter.MedianFilter(5))

    # applying median filter with 7x7 kernel
    med3_2 = med7.filter(ImageFilter.MedianFilter(7))

    # applying median filter with 5x5 kernel
    medFinal = med3_2.filter(ImageFilter.MedianFilter(5))
    return medFinal

if __name__ == '__main__':
    main()