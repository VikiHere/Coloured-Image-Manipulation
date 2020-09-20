'''
HSI to RGB
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

def main(*arg):
    imgName = input("Please enter image name: ")
    img = cv2.imread(imgName, 1)
    
    # to run independently (from main() ), needs to have rgb_to_hsi.py to be in the same directory!
    img1 = rgb_to_hsi(img)
    out = hsi_to_rgb(img1)
    
    cv2.imshow('out', out)
    cv2.waitKey(0) 

def hsi_to_rgb(img):
    ''' 
    Converts HSI to RGB; input image MUST be a float!
    '''
    # output image
    out_img = img

    # point transform operation; per pixel
    for row in range(img.shape[0]):
        for col in range(img.shape[1]): 
            H = img[row,col,0]    # getting HSI vals
            S = img[row,col,1]
            I = img[row,col,2]

            r = 0                # init RGB vals
            g = 0
            b = 0

            if (H >= 0 and H < (math.pi * 2/3)):                    # red-green region
                b = I*(1-S)
                r = I*(1 + (S*math.cos(H)) / math.cos(math.pi/3 - H))
                g = 3*I - (r+b)

            elif (H >=(math.pi * 2/3)  and H < (math.pi * 4/3)):    #green-blue region
               
                H_1 = H - (math.pi * 2/3)
                r = I*(1-S)
                g = I*(1 + (S*math.cos(H_1)) / math.cos(math.pi/3 - H_1))
                b = 3*I - (r+g)

            elif (H >= (math.pi * 4/3) and H < 2*math.pi):          #blue-red region

                H_2 = H - math.pi * 4/3
                g = I*(1-S)
                b = I*(1 + (S*math.cos(H_2)) / math.cos(math.pi/3 - H_2))
                r = 3*I - (g+b)
            
            # assign BGR values to output image
            out_img[row,col,0] = b
            out_img[row,col,1] = g
            out_img[row,col,2] = r

    return out_img

if __name__ == '__main__':
    main()