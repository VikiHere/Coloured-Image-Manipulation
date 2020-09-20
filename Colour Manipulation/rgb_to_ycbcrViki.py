'''
Colours: Part 3.1.3 - converting rgb to YCbCr
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import
'''

import numpy as np
import sys
#import cv2
from PIL import Image, ImageFilter

def main(*arg):
    imgName = input("Please enter image name: ")


    # import image 
    img = Image.open(imgName) 

     # Save image as np array of type float
    img = np.asarray(Image.open(imgName).convert('RGB'), dtype='float')

    out = rgb_to_ycbcr(img)

    final = Image.fromarray(out, mode='YCbCr')
    final.show()
    #final.save('testing.png')

def rgb_to_ycbcr(img):
#Checking if image passed is of type float, if not it will convert it
    if(img.dtype == 'uint8' or img.dtype == 'uint32'):
        img = np.asarray(img, dtype='float')

#normalize the image, therefore will only be working with
    #the simplified transform - yay no unsigned chars!!
    #img = np.divide(img, 255)
    #print(img)

#creating the output image empty size
    out_img = np.zeros(shape=img.shape, dtype='float')

    #print(img.shape[0], img.shape[1], img.shape[2])

#
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            out_img[row][col][0] = (0.299*img[row][col][0] + 0.587*img[row][col][1] + 0.114*img[row][col][2]) 
            #print(out_img[row][col][0])
            out_img[row][col][1] = (-0.1687*img[row][col][0] - 0.3313*img[row][col][1] + 0.5*img[row][col][2])
            out_img[row][col][2] = (0.5*img[row][col][0] - 0.4187*img[row][col][1] - 0.0813*img[row][col][2])

#Seperating the 3 colour channels
    #r = img[:, :, 0]
    #g = img[:, :, 1]
    #b = img[:, :, 2]


#linear operations - 
    #Applying the affine transformation to each pixel
    #for row in range(img.shape[0]):
    #    for col in range(img.shape[1]):
    #        r[row][col] = (0.299*r[row][col] + 0.587*g[row][col] + 0.114*b[row][col])    
    #        g[row][col] = (-0.1687*r[row][col] + -0.3313*g[row][col] + 0.5*b[row][col])
    #        b[row][col] = (0.5*r[row][col] + -0.4187*g[row][col] + -0.0813*b[row][col])

#de-normalize the image
    out_img = np.multiply(out_img, 255)

    #print(out_img)

    #return out_img 

if __name__ == '__main__':
    main()