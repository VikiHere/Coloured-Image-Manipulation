'''
 Histogram Equalization for Coloured Pictures
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import
'''

import numpy as np
import sys
from PIL import Image
from rgb_to_ycbcr import rbg_to_ycbcr
from ycbcr_to_rgb import ycbcr_to_rgb

def main(*arg):
    imgName = input("Please enter image name: ")

    # import image and convert to grayscale numpy array
    img = np.asarray(Image.open(imgName).convert('RGB'), dtype='float')

    out = histogram_equalize(img).astype('uint8')
      
    final = Image.fromarray(out, mode='RGB')
    final.show()
    final.save("hist_eq_colour_ycbcr.png")

# Histogram equalization for RGB images
def histogram_equalize(img):

    temp = rbg_to_ycbcr(img)
    #print(temp)

    #y_hist = histogram_equalize_colour(img[:,:,0].astype('uint8'))
    y_hist = histogram_equalize_colour(temp[:,:,0].astype('uint8'))
    print(np.amax(y_hist))
    print(np.amin(y_hist))
    #y_hist = temp[:,:,0]
    
    #y_hist = temp[:,:,0]

    #for row in range(img.shape[0]):
    #    for col in range(img.shape[1]):
    #        y_hist[row,col] = y_hist[row,col] + 128
            
    #y_hist = (y_hist*255).astype('uint8')


    #out_img = np.zeros(shape=img.shape)
    out_img = np.zeros(shape=temp.shape)
    out_img[:,:,0] = y_hist

    out_img = ycbcr_to_rgb(out_img)

    return out_img

# Histogram equalization for 8-bit image (1 colour)
def histogram_equalize_colour(img):
    # num of pixels
    pixels = img.shape[0] * img.shape[1]

    # num of levels
    levels = np.unique(img).size

    # max value found
    maxVal = np.amax(img)

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