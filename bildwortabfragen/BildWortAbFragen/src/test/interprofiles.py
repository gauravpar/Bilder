'''
Created on Jul 10, 2014

@author: phoenix
'''
#profiles at various heights of rows


import cv2
import numpy as np
import matplotlib.pyplot as plt



VertY=[] #for each row
VertX=[] # count the  black pixels


gray=cv2.imread('/tmp/test.jpeg',cv2.CV_LOAD_IMAGE_GRAYSCALE)
ret2,test = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)

Height,Width=test.shape #prota diavazei to ypsos kai meta to platos

print "Width",Width,"Height",Height


Limit=Height/2


#for each column get the coordinates of the last black pixel (aka pixel with higest x coord)


TopX=[] 
TopY=[] 


for col in xrange(0,Width):
    

    for row in reversed(range(0,Limit)):
        
        if test[row][col]==0: #count the BLACK
            TopY.append(Height-row) 
            TopX.append(col)
            #print 'a black pixel was found at',row,col
            break
    else:
        continue


print TopX
print TopY

#plot them
plt.plot(TopX,TopY)
plt.title("Low Profile")
plt.axis([0,Width,0,Height])
plt.show()