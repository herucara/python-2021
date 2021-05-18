# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:14:09 2021

@author: carlb
"""

from PIL import Image 
import numpy as np   #Use numpy to convert images to arrays

# Read image 
img = Image.open("images/test_image.jpg") #Not a numpy array
print(type(img))

# Output Images 
img.show() 

# prints format of image 
print(img.format) 
  
# prints mode of image 
print(img.mode) 

#PIL is not by default numpy array but can convert PIL image to numpy array. 
img1 = np.asarray(img)
print(type(img1))