'''
Created on Jul 10, 2014

@author: phoenix
'''
#vertical projection of a word

import cv2
import numpy as np
import matplotlib.pyplot as plt


VertY=[] #for each row
VertX=[] # count the  black pixels


gray=cv2.imread('/tmp/test.png',cv2.CV_LOAD_IMAGE_GRAYSCALE)
ret2,test = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)

Height,Width=test.shape #prota diavazei to ypsos kai meta to platos

print "Width",Width,"Height",Height




#Horizontal histogram


HorX=[] #for each column
HorY=[] # count the  black pixels

max=0 #for matplob figure
for col in xrange(0,Width):
    sum=0

    for row in xrange(0,Height):
        
        if test[row][col]==0: #count the BLACK
            sum+=1
    if sum>max:
        max=sum
        
    HorX.append(col)
    HorY.append(sum)




#plot them
plt.plot(HorX,HorY)
plt.title("Vertical Histogram")
plt.axis([0,Width,0,max])
plt.show()
