'''
Created on Apr 4, 2014
Test module to estimate white space
@author: phoenix
'''
#staring from left to right you found a column with no black elements

import cv2

test=cv2.imread("/tmp/testbin.png",cv2.CV_LOAD_IMAGE_GRAYSCALE)

X,Y=test.shape
#xekina apo aristera 
#diavase olo to column 
#an einai ola aspra simeiosate x



for i in range(0,X):
    Scwarz=0
    for j in range(0,Y):
        if test[i][j]==0:
            Scwarz+=1
            # print 'A black pixel was found at',i,j
            break
    else:
        continue
    
    if Scwarz==0:
        print 'All white in col',j
        

    
    
        

Width,Height=test.shape

