#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 23:51:52 2019

@author: alex
"""

import matplotlib.pyplot as plt
from scipy import misc


green_img = misc.imread("/Users/alex/Documents/Documents/CS1109/GreenImage.jpg", )



print(green_img[0][0][1])

total = 0
for row in range(len(green_img)):
    total += green_img[row][0][1]

average = total/len(green_img)

print("The average is ")
print(average)

for row in range(len(green_img)):
    for col in range(len(green_img[0])):
        if green_img[row][col][1] >= 170 and green_img[row][col][1] <= 2000:
            green_img[row][col][1] = 0
    
green_img.shape

#f = f[:,:,1]


print(type(green_img))
print(green_img.shape)

plt.imshow(green_img)
plt.show()



