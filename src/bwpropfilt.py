################################################################################
# Author: Prakhar Agarwal (https://github.com/prakhar19/)
################################################################################


import numpy as np
from skimage.measure import label, regionprops

def bwpropfilt(img, prop, range):
    labels = label(img)
    stats_full = regionprops(labels)
    
    propValues = np.array([each[prop] for each in stats_full])
    
    filteredIndecies = np.argwhere(np.logical_and(propValues >= range[0], propValues <= range[1]))

    mask = np.zeros(img.shape, dtype = bool)
    for index in filteredIndecies:
        mask = np.logical_or(mask, labels == stats_full[index[0]]['label'])
    
    out_img = cv2.bitwise_and(img, (mask * 255).astype(np.uint8))

    return out_img