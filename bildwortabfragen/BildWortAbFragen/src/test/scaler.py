'''
Created on Jul 9, 2014

@author: phoenix
'''
#read all the images in the query folder and make them have the same scale
#read the height of the biggest word

import sys
import cv2,glob



pics=glob.glob(sys.argv[1] +'*.*')

outFolder=sys.argv[2]


maxH=120


print sys.argv[1]
print sys.argv[2]


for p in pics:

 
    print '-------------------------------'
    print p
    #get the word name along with the font
    inx=p.rindex('synth') +6
    Word_Name=p[inx:]    
    Word_Name=Word_Name.replace('.png','')
    Word_Name='synth_'+Word_Name
    print 'Word name is',Word_Name    
    
    
 
    
    img=cv2.imread(p,cv2.CV_LOAD_IMAGE_GRAYSCALE)
    ret,im_bin=cv2.threshold(img,0,255,cv2.THRESH_OTSU)
    H,platos=im_bin.shape
    
    scale_fact_y=maxH/float(H)
    print 'new width',platos*scale_fact_y # this is the new width!!!
    
    newpic=cv2.resize(im_bin,None,fx=scale_fact_y,fy=scale_fact_y,interpolation=cv2.INTER_CUBIC) 
    #cv2.imshow('scaled',newpic)
    #cv2.waitKey() 
    #cv2.destroyAllWindows()   
    #save new pics

    #pics are now normalized
    
    #sharpen ????
    cv2.imwrite(outFolder+ Word_Name + '_norm.png',newpic,[cv2.IMWRITE_PNG_COMPRESSION,95])

        