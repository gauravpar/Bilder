# -*- coding: UTF-8 -*- 
'''
Created on Apr 4, 2014
Test module to estimate white space
@author: phoenix
'''
#staring from left to right you found a column with no black elements

import cv2
for p in range(1,7):
    test=cv2.imread("/home/phoenix/Verbinden/Weißraum/testwhite"+str(p)+".png",cv2.CV_LOAD_IMAGE_GRAYSCALE)
    ret2,test = cv2.threshold(test,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    copy=cv2.imread("/home/phoenix/Verbinden/Weißraum/testwhite"+str(p)+".png",cv2.CV_LOAD_IMAGE_COLOR)
    
    
    
    Width,Height=test.shape
    #xekina apo aristera 
    #diavase olo to column 
    #an einai ola aspra simeiosate x
    
    Spaces=[]
    
    for col in range(0,Height):
        Scwarz=0
        
        for row in range(0,Width):
            
            if test[row][col]==0:
                Scwarz=1
                # print 'A black pixel was found at',i,j
               
        if Scwarz==0:
            #print 'All white in col',col
            
            
            #draw a blue line
            for i in range(0,Width):
                copy[i][col][0]=255
                copy[i][col][1]=0
                copy[i][col][2]=0
    
    #count the thickness of the red lines
    
    
    cv2.imshow('white space',copy)   
    cv2.imwrite('/tmp/white' + str(p) + '.png',copy)         
    cv2.waitKey()
    cv2.destroyAllWindows()        
    
        
        
            



