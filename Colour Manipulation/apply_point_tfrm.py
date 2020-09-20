'''
Apply Point Transfer for Coloured Pictures
Vic S.
 NOTE: Scipy and Numpy are only used for matrix manipulation and
        image import
'''

import numpy as np
import sys
from PIL import Image

def main():
    imgName = input("Please enter image name: ")
    c = (float)(input("Enter 'c' value: "))
    b = (int)(input("Enter 'b' value: "))
    
    # import image
    img = np.asarray(Image.open(imgName).convert('RGB'), dtype='uint8')

    out = apply_point_tfrm(img, c, b).astype('uint8')
      
    final = Image.fromarray(out, mode='RGB')
    final.show()
    final.save("color_pt_trfm.png")

def apply_point_tfrm(img, c, b):
    '''
    Histogram equalization for RGB images
    '''
    red = np.copy(img[:,:,0])
    green = np.copy(img[:,:,1])
    blue = np.copy(img[:,:,2])

    # point operation on each colour individually
    red = apply_point_tfrm_colour(img[:,:,0], c, b)
    green = apply_point_tfrm_colour(img[:,:,1], c, b)
    blue = apply_point_tfrm_colour(img[:,:,2], c, b)

    out_img = np.zeros(shape=img.shape)
    out_img[:,:,0] = red
    out_img[:,:,1] = green
    out_img[:,:,2] = blue

    return out_img

# Apply point transform for 8 bit image (1 colour)
def apply_point_tfrm_colour(in_img, C, B):
    img = np.copy(in_img)

    # bounding B value to 0 <= B <= 255
    if (B > 255 or B < 0):
        print("Error: B must be between 0 and 255! ")
        exit()

    for i in range(in_img.shape[0]):
        for j in range(in_img.shape[1]):
            img[i][j] = img[i][j]*C+B
            if (img[i][j] > 255):
                img[i][j] = 255
            elif img[i][j] < 0:
                img[i][j] = 0
    return img

if __name__ == '__main__':
    main()
