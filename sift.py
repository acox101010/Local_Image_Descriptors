# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 22:02:56 2018

"""
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
from pylab import *

#create function process_image
def process_image(imagename,resultname,params="--edge-thresh 10 --peak-thresh 5"):
    """process the image then save in file"""
    
    if imagename[-3:] != 'pgm':
        #create pgm file
        im = Image.open(imagename).convert('L') #converts to greyscale
        im.save('tmp.pgm') #saves as .pgm file
        imagename = 'tmp.pgm'
        
    cmmd = str("sift "+imagename+" --output="+resultname+
               " "+params)
    os.system(cmmd)
    print('processed', imagename, 'to', resultname)
    
#create function to read features to NumPy arrays from output file
def read_features_from_file(filename):
    """Read feature properties and return in matrix form."""
    
    f = loadtxt(filename)
    return f[:,:4],f[:,4:] #feature locators, descriptors

#create function to write results back to features
def write_features_to_file(filename,locs,desc):
    """save feature location and descriptors to file"""
    savetxt(filename,hstack((locs,desc)))
    
#plot locations on image
def plot_features(im,locs,circle=False):
    
    def draw_circle(c,r):
        t = arange(0,1.01,.01)*2*pi
        x = r*cos(t) + c[0]
        y = r*sin(t) + c[1]
        plot(x,y,'b',linewidth=2)
    
    imshow(im)
    
    if circle:
        for p in locs:
            draw_circle(p[:2],p[2])
    else:
        plot(locs[:,0],locs[:,1],'ob')
    axis('off')
    