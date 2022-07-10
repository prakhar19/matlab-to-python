################################################################################
# Author: Prakhar Agarwal (https://github.com/prakhar19/)
################################################################################


import numpy as np

def isvector(inp):
    return (np.array(np.array(inp).shape) > 1).sum() <= 1