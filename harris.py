# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 19:17:26 2018

@author: Reaper124
"""
from PIL import Image
from scipy.ndimage import filters
from matplotlib import pyplot as plt
from numpy import *
from pylab import *

def compute_harris_response(im,sigma=3):
    imx = zeros(im.shape)
    filters.gaussian_filter(im, (sigma,sigma), (0,1), imx)
    imy = zeros(im.shape)
    filters.gaussian_filter(im, (sigma,sigma), (1,0), imy)
    
    Wxx = filters.gaussian_filter(imx*imx,sigma)
    Wxy = filters.gaussian_filter(imx*imy,sigma)
    Wyy = filters.gaussian_filter(imy*imy,sigma)
    
    Wdet = Wxx*Wyy - Wxy**2
    Wtr = Wxx + Wyy
    
    return Wdet/Wtr  

def get_harris_points(harrisim,min_dist=10,threshold=0.1):
    
    corner_threshold = harrisim.max() * threshold
    harrisim_t = (harrisim > corner_threshold) * 1
    
    coords = array(harrisim_t.nonzero()).T
    
    candidate_values = [harrisim[c[0],c[1]] for c in coords]
    
    index = argsort(candidate_values)
    
    allowed_locations = zeros(harrisim.shape)
    allowed_locations[min_dist:-min_dist,min_dist:-min_dist] = 1
    
    filtered_coords = []
    for i in index:
        if allowed_locations[coords[i,0],coords[i,1]] == 1:
            filtered_coords.append(coords[i])
            allowed_locations[(coords[i,0]-min_dist):(coords[i,0]+min_dist),
                              (coords[i,1]-min_dist):(coords[i,1]+min_dist)] = 0
    return filtered_coords
    
def plot_harris_points(image,filtered_coords):
    
    figure()
    gray()
    imshow(image)
    plot([p[1] for p in filtered_coords],[p[0] for p in filtered_coords],'*')
    axis('off')
    show()
