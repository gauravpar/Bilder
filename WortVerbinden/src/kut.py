'''
Created on Apr 4, 2014
Test module for cut and pasting images
DEPRECATED QT CAN DO IT FOR US
WE NEED TO CREATE OUR OWN QGRAPHICSSCENE AND QGRAPHICSVIEW AND CALL THE EVENT DOUBLECLICKVEVENT
AND THEN event.scene.pos
@author: phoenix
'''
import cv2,math
import numpy as np
#image is samos 0013
#opws ta vlepeis sto gimp
#17 noemvrioy 1900
LowY=1890
LowX=614

TopY=2231
TopX=663

doc=cv2.imread('/home/phoenix/samos_1900 - 1902/0013.jpg')
x,y,z=doc.shape

print 'dimensions ',x,y

bild=np.ones((math.fabs(LowX-TopX),math.fabs(TopY-LowY),3), np.uint8)
bild.fill(255)

r=-1

for i in range(LowX,TopX):
    r+=1
    #print 'r=',i
    c=-1
    for j in range(LowY,TopY):
        c+=1
        #print 'c=',j
        bild[r][c][0]=doc[i][j][0]
        bild[r][c][1]=doc[i][j][1]
        bild[r][c][2]=doc[i][j][2]
    
cv2.imshow('cut',bild)
cv2.waitKey()
cv2.destroyAllWindows()
print 'ok'

