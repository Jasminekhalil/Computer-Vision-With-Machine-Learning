# -*- coding: utf-8 -*-
# Course Project 1 - Image Manipulation.ipynb

# Imported libraries
import os
import PIL
import matplotlib.pyplot as plt

directory = "/content" # Identfying the location of the image
name = "0.png" # Identfying the name of the image

filepath = os.path.join(directory, name) # Using the os library to create a path to the image regardless of the operating system used

img = PIL.Image.open(filepath) # Use PIL to open the image

img = img.convert('L') # Converting the image to grayscale

plt.imshow(img, cmap='gray', vmin=0, vmax=255) # Using matplot to plot the grayscale image

# Importing numpy to convert the image into a numerical array
import numpy as np

# Converting the image to a Numpy array
img_array = np.asarray(img)

# Viewing the array as an image
plt.imshow(img_array, cmap='gray', vmin=0, vmax=255)

# Viewing the shape and dimensions of the array
shape = img_array.shape
array = img_array
first_row = img_array[0,:]
first_column = img_array[:,0]

print('Shape:', shape)
print('Array:', array)
print('First Row:', first_row)
print('First Column:', first_column)

# Using the Scikit-Image Transform module to help resize the image
from skimage.transform import resize

# Resizing to 28X28 pixels 

height = 28
width = 28

img_resized =  resize(img_array, (height, width), anti_aliasing = True)

print('New array shape:', img_resized.shape)

plt.imshow(img_resized, cmap='gray', vmin=0, vmax=255)

img_resized = img_resized*255 # Normalizing values in the image to values between 0 and 255
img_resized = np.rint(img_resized) # Rounding all elements
img_resized = img_resized.astype(int) # Converting all elements to integers
img_resized = np.clip(img_resized, 0, 255) # Clamping values to 0 and 255

plt.imshow(img_resized, cmap='gray', vmin=0, vmax=255) # Will result in a more pixelated image as it is smaller now

img_with_box = np.copy(img_resized) # Copying the resized image

# Shape of the box to be placed in the center of the image
box_h = 10
box_w = 10

# Get the height and width of the image
img_h = img_with_box.shape[0]
img_w = img_with_box.shape[1]

# Find coordinates of first line
x0 = int((img_w / 2) - (box_w / 2))
x1 = int((img_w / 2) + (box_w / 2))
y0 = int((img_h / 2) - (box_h / 2))

# Change slice of image array elements to 255
img_with_box[y0, x0:x1] = 255

# Find coordinates of the second line
x0 = int((img_w / 2) - (box_w / 2))
x1 = int((img_w / 2) + (box_w / 2))
y0 = int((img_h / 2) + (box_h / 2))

# Change slice of image array elements to 255
img_with_box[y0, x0:x1] = 255

# Find coordinates of third line
x0 = int((img_w / 2) - (box_w / 2))
y0 = int((img_h / 2) - (box_h / 2))
y1 = int((img_h / 2) + (box_h / 2))

# Change slice of image array elements to 255
img_with_box[y0:y1, x0] = 255

# Find coordinates of the fourth line
x0 = int((img_w / 2) + (box_w / 2))
y0 = int((img_h / 2) - (box_h / 2))
y1 = int((img_h / 2) + (box_h / 2) + 1) # The last index is non-inclusive so we add 1

# Change slice of image array elements to 255
img_with_box[y0:y1, x0] = 255

plt.imshow(img_with_box, cmap='gray', vmin=0, vmax=255) # Displaying teh same resized image with a white box in the middle