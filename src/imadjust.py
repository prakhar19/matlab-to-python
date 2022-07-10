################################################################################
# Author: Prakhar Agarwal (https://github.com/prakhar19/)
################################################################################


import numpy as np

def imadjust(img):
    lower = np.percentile(img.flatten(), 1)
    upper = np.percentile(img.flatten(), 99)

    out = (img - lower) * (255 / (upper - lower))
    
    return np.clip(out, 0, 255).astype(np.uint8)