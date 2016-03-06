#!/usr/bin/env python
# coding: utf-8
#
# Author:   Kazuto Nakashima
# URL:      https://github.com/kazuto1011
# Created:  2016-03-07

import cv2
import numpy as np
import itertools

contrib_color = [
        [0.933, 0.933, 0.933],
        [0.521, 0.902, 0.839],
        [0.396, 0.776, 0.549],
        [0.251, 0.639, 0.267],
        [0.137, 0.408, 0.118]
]

contrib_thres = []

for i in range(5):
    mean = sum(contrib_color[i])/3.0
    contrib_thres.append(mean)

avatar = np.ones((223,223,3))

img = cv2.imread('./original.png', 0)
img = cv2.resize(img, (221,221))

square = 11
space  = 2

for i,j in itertools.product(range(17),range(17)):
    x = (i+1)*space + i*square
    y = (j+1)*space + j*square
    
    for k in range(5):
        if np.mean(img[x:x+square, y:y+square])/255 >= contrib_thres[k]:
            break
    
    avatar[x:x+square, y:y+square, :] = np.tile(contrib_color[k], [square, square, 1])

cv2.imwrite('./avatar.png', avatar*255)
