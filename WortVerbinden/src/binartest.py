'''
Created on Apr 2, 2014

@author: phoenix
'''
#This is just a test module . It is not  part of the main program
import cv2
import numpy as np

#Read an image
col=cv2.imread('/home/phoenix/Verbinden/imageproc.png')
x,y,z=col.shape


#Create the binary image
#Fill it with blank
bin= np.ones((x,y,z), np.uint8)
bin.fill(255)

for i in range(0,x):
    for j in range(0,y):
        if col[i][j][0]<120 and col[i][j][1]<120 and col[i][j][2]<120:
            bin[i][j]=col[i][j]
#show the image
cv2.imshow('binarized',bin)
cv2.waitKey() 
cv2.destroyAllWindows()