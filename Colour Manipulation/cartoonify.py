'''
Complete Cartoonify effect (using Sobel Kernel)
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import

        NOTE v2: as specified, PIL also used to provide Median Filter capability
'''

import numpy as np
import sys
from PIL import Image
from cartoonify_pt1 import cartoonify_pt1
from cartoonify_pt2 import cartoonify_pt2

def main(*arg):
    imgName = input("Please enter image name: ")
    print("\nATTENTION: folder 'edge_det_res' with .py files:\n\t 'automatic_threshold.py',\n\t 'spatial_filter.py',\n\t 'image_threshold.py'\n\t__init__.py\nmust be present (do not change the given file/directory structure; use as given)\n")
    print("...working...")
    
    # import image as RGB
    img = Image.open(imgName).convert('RGB')   # note: NOT using numpy, keeping as a PIL object
    
    out = cartoonify(img)

    final = Image.fromarray(out, mode='RGB')
    final.show()
    #final.save("cartoonify_sobel.png")

# Main cartoonify function
def cartoonify(img):
    # blurring
    blur = cartoonify_pt1(img)
    
    # Edge map (using Sobel, threshold at 30%)
    gray = img.convert('L')
    edge = cartoonify_pt2(gray, "s", 0.30)    # return numpy object
    
    # combining the blurred image and edge map
    out = np.asarray(blur, dtype='float')   

    for row in range(out.shape[0]):      # for all 3 colours
        for col in range(out.shape[1]):
            if (edge[row][col] > 0):
                # taking 30% of original intensity, rather than setting to black
                out[row][col][0] = out[row][col][0]*0.3
                out[row][col][1] = out[row][col][1]*0.3
                out[row][col][2] = out[row][col][2]*0.3
 
    return out.astype('uint8')

if __name__ == '__main__':
    main()