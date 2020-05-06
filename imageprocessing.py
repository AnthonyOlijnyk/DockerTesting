from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


print("first check")
#reading in the original image
original = cv.imread('airplanes.jpg')

#converting the original image into grayscale
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)

#making the grayscale have 3 channelsl
grayThree = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

#threshold for black and white
ret,thresh = cv.threshold(grayThree, 127, 255, cv.THRESH_BINARY_INV)

print("second check")

#instantiating the figure and axes objects
fig, (ax1, ax2, ax3) = plt.subplots(nrows = 1, ncols = 3)
ax1.set_title('Original')
ax1.set_axis_off()

ax2.set_title('Gray Scale')
ax2.set_axis_off()

ax3.set_title('Black and White')
ax3.set_axis_off()

ax1.imshow(original)
ax2.imshow(grayThree)
ax3.imshow(thresh)

print("third check")

plt.savefig('threeplanes.png')

print("fourth check")
