# imports
import cv2 as cv
import numpy as np
import os
import face_recognition

# read data
img = cv.imread('out.jpg')

# play with data
img = cv.resize(img, (500, 400))
#img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(img_gray, 10, 255, cv.THRESH_BINARY)

# represent the data
cv.imshow('normal_image', img)
cv.imshow('gray_image', img_gray)
cv.imshow('binary_image', thresh)





# cv.imshow('CHANGED_image', img_rgb)
cv.waitKey(0)