'''
Created on Apr 4, 2014
Test module for cut and pasting images
@author: phoenix
'''
import cv2,math
import numpy as np
#image is samos 0013
LowY=471
LowX=457

TopX=424
TopY=771

doc=cv2.imread('/home/phoenix/samos_1900 - 1902/0013.jpg')
x,y,z=doc.shape

print 'dimensions ',x,y

bild=np.ones((math.fabs(LowX-TopX),math.fabs(TopY-LowY),3), np.uint8)
