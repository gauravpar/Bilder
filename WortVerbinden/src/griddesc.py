'''
Created on May 7, 2014

@author: phoenix
'''
#baselineis 69
import cv2
import numpy as np


qr=cv2.imread('/home/phoenix/Desktop/faq.png',cv2.CV_LOAD_IMAGE_COLOR)
h,w,z=qr.shape
step=8
bline=73


 


colstep=8
#draw red lines 
for row in range(0,bline,step):
    for col in range(0,w):
        qr[row][col][0]=0
        qr[row][col][1]=0
        qr[row][col][2]=255
        

for col in range(0,w,colstep):
    for row in range(0,bline):
        qr[row][col][0]=0
        qr[row][col][1]=0
        qr[row][col][2]=255
        


cv2.imshow('red',qr)
cv2.waitKey()
cv2.destroyAllWindows()        