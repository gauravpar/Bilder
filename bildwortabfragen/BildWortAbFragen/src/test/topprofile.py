'''
Created on Jul 10, 2014

@author: phoenix
'''
#top profile
import cv2
import numpy as np
import matplotlib.pyplot as plt


gray=cv2.imread('/tmp/test.png',cv2.CV_LOAD_IMAGE_GRAYSCALE)
ret2,test = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)

Height,Width=test.shape #prota diavazei to ypsos kai meta to platos

print "Width",Width,"Height",Height




#for each column get the coordinates of the first black pixel (aka pixel with lowest x coord)


TopX=[] 
TopY=[] 


for col in xrange(0,Width):
    

    for row in xrange(0,Height):
        
        if test[row][col]==0: #count the BLACK
            TopY.append(Height-row) # Without the Height it is a mirror image of the top profile
            TopX.append(col)
            print 'a black pixel was found at',row,col
            break
    else:
        continue


print TopX
print TopY

#plot them
plt.plot(TopX,TopY)
plt.title("Top Profile")
plt.axis([0,Width,0,Height])
plt.show()
