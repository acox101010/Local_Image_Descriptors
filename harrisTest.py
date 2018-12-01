# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 19:19:24 2018

@author: Reaper124
"""
from PIL import Image
from scipy.ndimage import filters
from matplotlib import pyplot as plt
from numpy import *
from pylab import *
import harris

image_1 = (r'C:\Users\Reaper124\castle.png')
image_open = Image.open(image_1)

im = array(Image.open(image_1).convert('L'))
harrisim = harris.compute_harris_response(im)
filtered_coords = harris.get_harris_points(harrisim,6)
harris.plot_harris_points(im, filtered_coords)