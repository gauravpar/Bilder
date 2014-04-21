'''
Created on Apr 21, 2014

@author: phoenix
'''
#vertical and horizontal istograms
import cv2
import numpy as np
import matplotlib.pyplot as plt

VertY=[] #for each row
VertX=[] # count the  black pixels


test=cv2.imread('/home/phoenix/Verbinden/testhist.png',cv2.CV_LOAD_IMAGE_GRAYSCALE)
Height,Width=test.shape #prota diavazei to ypsos kai meta to platos

print "Width",Width,"Heigth",Height

max=0 #for matplob figure
for row in range(0,Height):
    sum=0

    for col in range(0,Width):
        if test[row][col]==0: #count the BLACK
            sum+=1
    if sum>max:
        max=sum
    VertY.append(row)
    VertX.append(sum)



    
max+=10
#plot them
plt.plot(VertX,VertY)
plt.title("Vertical Histogram")
plt.axis([0,max,0,Height]) # max(sum in x)
plt.show()


#Horizontal histogram


HorX=[] #for each column
HorY=[] # count the  black pixels

max=0 #for matplob figure
for col in range(0,Width):
    sum=0

    for row in range(0,Height):
        
        if test[row][col]==0: #count the BLACK
            sum+=1
    if sum>max:
        max=sum
        
    HorX.append(col)
    HorY.append(sum)




#plot them
plt.plot(HorX,HorY)
plt.title("Horizontal Histogram")
plt.axis([0,Width,0,max])
plt.show()

