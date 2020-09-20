'''
RGB to HSI
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import

 ** NEW NOTE ** : MUST have OpenCV (cv2) installed; used to display
                    images in HSI format; HSI *not* supported by PIL
'''

import numpy as np
import math
import sys
import cv2
from PIL import Image

def main(*arg):
    imgName = input("Please enter image name: ")
    img = cv2.imread(imgName, 1)

    out = rgb_to_hsi(img)      
    cv2.imshow('HSI', out)
    cv2.waitKey(0)

def rgb_to_hsi(img):
    # making sure input is always a float
    img = np.asarray(img, dtype='float64')
    img = np.divide(img, 255)  #normalization of RGB
    out_img = img
    
    # breaking into separate colours (cv2 returns numpy array in BGR)
    b = img[:,:,0]
    g = img[:,:,1]
    r = img[:,:,2]

    H = np.zeros(shape=g.shape)
    for row in range(H.shape[0]):       # point transform operation; per pixel
        for col in range(H.shape[1]):
            red = r[row][col]
            green = g[row][col]
            blue = b[row][col]
            
            # HUE Calculation
            num = 0.5*((red - green) + (red - blue))    
            denom = math.sqrt( (red-green)**2 + (red-blue)*(green-blue))
            theta = math.acos(num/(denom + 0.00001)) # added small number to avoid div by 0

            if (blue <= green):
                out_img[row][col][0] = theta
            elif (blue > green):
                out_img[row][col][0] = 2*math.pi - theta

            # SATURATION Calculation
            c_min = np.amin([red, green, blue])
            out_img[row][col][1] = 1 - (3*c_min/(red+green+blue+0.0001))    # added small number to avoid div by 0
            
            # INTENSITY Calculation
            out_img[row][col][2] = (red+green+blue)/3

    return out_img

if __name__ == '__main__':
    main()