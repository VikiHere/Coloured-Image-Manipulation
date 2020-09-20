'''
Spatial Filter for Coloured Pictures
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
    img = np.asarray(Image.open(imgName).convert('RGB'), dtype='float')

    # Gaussian kernel with sigma = 1
    h = (1/331)*np.array([  [1, 4, 7, 4, 1],
                            [4, 20, 33, 20, 4],
                            [7, 33, 55, 33, 7],
                            [4, 20, 33, 20, 4],
                            [1, 4, 7, 4, 1]
                            ])

    out = spatial_filter(img, h).astype('uint8')
      
    final = Image.fromarray(out, mode='RGB')
    final.show()
    final.save("spatial_filter_blur.png")


def spatial_filter(img,h):
    '''
    Spatial Filtering for RGB images; default operation: Gaussian blur
    '''

    red = np.copy(img[:,:,0])
    green = np.copy(img[:,:,1])
    blue = np.copy(img[:,:,2])

    # filter every colour separately
    red = spatial_filter_colour(img[:,:,0], h)
    green = spatial_filter_colour(img[:,:,1], h)
    blue = spatial_filter_colour(img[:,:,2], h)

    # bring the final image together
    out_img = np.zeros(shape=img.shape)
    out_img[:,:,0] = red
    out_img[:,:,1] = green
    out_img[:,:,2] = blue

    return out_img

# Spatial Filter for 1 colour only (8-bit image)
def spatial_filter_colour(img, h):
    padX = (int)(h.shape[0]/2)
    padY = (int)(h.shape[1]/2)

    # creating padded Image
    temp = np.zeros(shape=(2*padX + img.shape[0], 2*padY + img.shape[1]))
    temp[padX : img.shape[0]+padX , padY : img.shape[1]+padY] = img

    #final image
    out_img = np.zeros(shape=img.shape)

    # filter convolution
    for row in range(padX, img.shape[0]+padX):       # row
       for col in range(padY, img.shape[1]+padY):   # column

            startX = row - padX
            startY = col - padY
            endX = startX + h.shape[0]
            endY = startY + h.shape[1]
            window = temp[startX : endX, startY : endY] 

            out_img[row - padX][col - padY] = (int)(np.sum(np.multiply(window, h)))
    
    return out_img

if __name__ == '__main__':
    main()