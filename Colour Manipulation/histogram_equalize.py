'''
Histogram Equalization for Coloured Pictures
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import
'''

import numpy as np
import sys
from PIL import Image

def main(*arg):
    imgName = input("Please enter image name: ")

    # import image and convert to grayscale numpy array
    img = np.asarray(Image.open(imgName).convert('RGB'), dtype='uint8')

    out = histogram_equalize(img).astype('uint8')
      
    final = Image.fromarray(out, mode='RGB')
    final.show()
    final.save("hist_eq_colour.png")

def histogram_equalize(img):
    '''
    Histogram equalization for RGB images
    '''

    # hist equal every colour separately
    red = histogram_equalize_colour(img[:,:,0])
    green = histogram_equalize_colour(img[:,:,1])
    blue = histogram_equalize_colour(img[:,:,2])

    # put final image together
    out_img = np.zeros(shape=img.shape)
    out_img[:,:,0] = red
    out_img[:,:,1] = green
    out_img[:,:,2] = blue

    return out_img

# Histogram equalization for 8-bit image (1 colour)
def histogram_equalize_colour(img):
    # num of pixels
    pixels = img.shape[0] * img.shape[1]

    # Initial histogram
    lut = np.zeros(256, dtype="float")

    # Get histogram
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            lut[img[row][col]] += 1

    # Get the PDF from the histogram
    lut = np.divide(lut, pixels)
    cdf = np.zeros(shape=lut.shape)

    # Get the CDF
    for i in range(cdf.shape[0]):
        if (i == 0):
            cdf[i] = lut[i]
        else:
            cdf[i] = lut[i] + cdf[i-1]

    # Multiply CDF by max intensity range to equalize
    cdf = np.multiply(cdf, 255)

    # Make final LUT and round the values
    lut_f = np.zeros(shape=lut.shape, dtype="uint8") 
    lut_f = np.rint(cdf)

    out_img = np.zeros(shape=img.shape)

    # Apply final LUT to the image
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            out_img[row][col] = lut_f[img[row][col]]

    return out_img

if __name__ == '__main__':
    main()