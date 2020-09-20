'''
Change Hue
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
    rad = (float)(input("Please enter hue angle offset (rad): "))

    img = cv2.imread(imgName, 1)

    out = change_hue(img, rad)
    
    cv2.imshow('out', out)
    cv2.waitKey(0) 

def change_hue(img, hue_angle):
    ''' 
    Changes Hue based on provided hue offset; Hue Angle must be provided in *radians* !
    '''
    # convert to HSI
    out_img = rgb_to_hsi(img)

    # get Hue angle displacement in radians; only change 0 <= x <= 2pi
    if (hue_angle != 0):
        change = abs(hue_angle) % (2*math.pi)
    else:
        change = 0
    
    # adjust hue for every pixel
    for row in range(out_img.shape[0]):
        for col in range(out_img.shape[1]):
            
            # making sure 0 <= hue <= 2pi
            if (out_img[row,col,0] + change > 2*math.pi):
                 out_img[row,col,0] = out_img[row,col,0] + change - 2*math.pi
            elif (out_img[row,col,0] + change < 0):
                 out_img[row,col,0] = out_img[row,col,0] + change + 2*math.pi
            else:
                 out_img[row,col,0] = out_img[row,col,0] + change

    # convert to RGB
    out_img = hsi_to_rgb(out_img)

    return out_img

if __name__ == '__main__':
    main()