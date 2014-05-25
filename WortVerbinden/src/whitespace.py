# -*- coding: UTF-8 -*- 
'''
Created on Apr 4, 2014
Test module to estimate white space
@author: phoenix
'''
#starting from left to right you found a column with no black elements


import cv2
for p in range(0,7):
    Spaces=[]
    print p
    test=cv2.imread("/home/phoenix/Verbinden/whitespace/space"+str(p)+".png",cv2.CV_LOAD_IMAGE_GRAYSCALE)
    ret2,test = cv2.threshold(test,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    copy=cv2.imread("/home/phoenix/Verbinden/whitespace/space"+str(p)+".png",cv2.CV_LOAD_IMAGE_COLOR)
    
    
    
    Height,Width=test.shape
    #xekina apo aristera 
    #diavase olo to column 
    #an einai ola aspra simeiosate x
    
   
    for col in range(0,Width):
        Schwartz=0
        
             
        for row in range(0,Height):
            
            if test[row][col]==0:
                Schwartz=1
                # print 'A black pixel was found at',i,j
                
                
          
               
        if Schwartz==0:
            #print 'All white in col',col
            
            Spaces.append(1)
            #draw a blue line
            for i in range(0,Height):
                copy[i][col][0]=0
                copy[i][col][1]=0
                copy[i][col][2]=255
        else:
            Spaces.append(0)
    
    #count the thickness of the red lines/spaces
    Mikos=[]
    m=0
    print '-------------------------'
    for s in Spaces:
        #print "s=",s
        if s==1:
            m+=1
        else:
            if m>0:
                Mikos.append(m)
            m=0
            
    for m in Mikos:
        print m
    #so find the length  sequence of ones in Spaces
    
    
    
    
    cv2.imshow('white space',copy)   
    #cv2.imwrite('/tmp/white' + str(p) + '.png',copy)         
    cv2.waitKey()
    cv2.destroyAllWindows()        
    
        
    
            



