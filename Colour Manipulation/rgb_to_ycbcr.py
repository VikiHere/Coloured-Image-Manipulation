'''
RGB to Y'CbCr
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import
'''

import numpy as np
import sys
from PIL import Image

def main(*arg):
    imgName = input("Please enter image name: ")

    # import image
    img = np.asarray(Image.open(imgName).convert('RGB'), dtype='float')
    img2 = Image.open(imgName).convert('HSV')
    img2.show()
    out = rbg_to_ycbcr(img)
    
    # converting to 8-bit before viewing (avoided when more operations planned)
    #out[:,:,0] = chkOv(out[:,:,0])
    #out[:,:,1] = chkOv(out[:,:,1])
    #out[:,:,2] = chkOv(out[:,:,2])
    #out = out.astype('uint8')

    final = Image.fromarray(out.astype('uint8'), mode='RGB')
    final.show()
    final.save("rgbtoycbcr.png")

# RGB to Y'CbCr Converter, using JPEG variant
def rbg_to_ycbcr(img):
    '''
    Assuming RGB format of 'img'
    '''
    out_img = img.astype('float')

    inv_mat = np.array([[0.299, 0.587, 0.114 ],
                        [-0.1687, -0.3313, 0.5],
                        [0.5, -0.4187, -0.0813]  ], dtype='float')

    # if output image is 8-bit
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            
            out_img[row,col] = np.matmul(out_img[row,col], inv_mat)

           # if (maxVal == 'uint8' or maxVal == 'uint32'):  # if input image isn't normalized/float
            out_img[row,col] = np.add(out_img[row,col], [0, 128, 128])

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