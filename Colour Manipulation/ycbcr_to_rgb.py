'''
 Y'CbCr to RGB
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import
'''

import numpy as np
import sys
from PIL import Image
from rgb_to_ycbcr import rbg_to_ycbcr

def main(*arg):
    imgName = input("Please enter image name: ")

    # import image
    img = np.asarray(Image.open(imgName).convert('RGB'), dtype='float')
    temp = rbg_to_ycbcr(img)
    out = ycbcr_to_rgb(temp)
    
    # converting to 8-bit before viewing (avoided when more operations planned)
    #out[:,:,0] = chkOv(out[:,:,0])
    #out[:,:,1] = chkOv(out[:,:,1])
    #out[:,:,2] = chkOv(out[:,:,2])

    final = Image.fromarray(out.astype('uint8'), mode='RGB')
    final.show()
    final.save("ycbcrtorgb.png")

# Y'CbCr to RGB Converter, using JPEG variant
def ycbcr_to_rgb(img):
    '''
    Assuming Y/Cb/Cr format of 'img'!
    '''

    temp1 = img.astype('float')
    out_img = img.astype('float')

    subMat = np.array([0,128,128], dtype='float')

    inv_mat = np.array([[1, 0, 1.402 ],
                        [1, -0.34414, -0.71414],
                        [1, 1.772, 0]  ], dtype='float')

    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            out_img[row,col] = np.subtract(out_img[row,col], subMat)
            out_img[row,col] = np.dot(out_img[row,col], inv_mat)

    return out_img

# Helper function to check for overflow over 255 or below 0
def chkOv(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (img[i][j] > 255):
                img[i][j] = 255
            elif (img[i][j] < 0):
                img[i][j] = 0
    return img

if __name__ == '__main__':
    main()