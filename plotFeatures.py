# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 22:30:10 2018

@author: Reaper124
"""
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pylab import *
import sift
import os

imname =(r'C:\Users\Reaper124\.spyder-py3\Scripts\sift\castle.png')
im1 = array(Image.open(imname).convert('L'))
sift.process_image(imname,'castle.sift')
l1,d1 = sift.read_features_from_file('castle.sift')

figure()
gray()
sift.plot_features(im1,l1,circle=True)
show()
