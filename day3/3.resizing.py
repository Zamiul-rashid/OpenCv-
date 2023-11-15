import cv2 as cv 
import numpy as np 

img = cv.imread("E:\OpenCv\Assets\pic1.jpg")


#resize 
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) 
"""Interpolation notes 
Inter cubic = takes time but the highest quality 
inter area = tend to use most regularly
"""
cv.imshow('Resized', resized)