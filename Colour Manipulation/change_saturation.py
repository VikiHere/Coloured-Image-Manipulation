'''
Change Saturation
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import

** NEW NOTE ** : MUST have OpenCV (cv2) installed; used to display
                    images in HSI format; HSI *not* supported by PIL
'''

import numpy as np
import math
import sys
from PIL import Image
import cv2
from rgb_to_hsi import rgb_to_hsi
from hsi_to_rgb import hsi_to_rgb

def main(*arg):
    imgName = input("Please enter image name: ")
    sat = (float)(input("Please enter saturation offset: "))

    img = cv2.imread(imgName, 1)

    out = change_saturation(img, sat)
    
    cv2.imshow('out', out)
    cv2.waitKey(0) 

def change_saturation(img, sat):
    ''' 
    Changes saturation level of HSI image
    '''
    # convert to HSI
    out_img = rgb_to_hsi(img)

    # Perform operation only if change isn't 0
    if (sat != 0):
        # adjust saturation for every pixel
        for row in range(out_img.shape[0]):
            for col in range(out_img.shape[1]):
                result = out_img[row,col,1] + sat
                
                # make sure that the final result stays 0 <= S <= 1
                if (result > 1):
                    out_img[row,col,1] = 1
                elif (result < 0):
                    out_img[row,col,1] = 0
                else:
                    out_img[row,col,1] = result

    # convert to RGB
    out_img = hsi_to_rgb(out_img)

    return out_img

if __name__ == '__main__':
    main()