'''
Created on Jul 9, 2014

@author: phoenix
'''
#read an image and crop white pixels
#aka create a bounding box around the image
import sys
import cv2,numpy as np
import glob



fakelos=glob.glob(sys.argv[1] + '*.*')

outFolder=sys.argv[2]


print 'in',sys.argv[1]
print 'out',outFolder



for pic in fakelos:
    

    print pic
    #get the word name along with the font
    inx=pic.rindex('synth') +6
    Word_Name=pic[inx:]    
    Word_Name=Word_Name.replace('.png','')
    Word_Name='synth_'+Word_Name
    print 'Word name is',Word_Name    
    
    

    img=cv2.imread(pic,cv2.CV_LOAD_IMAGE_GRAYSCALE)
    ret,img_bin=cv2.threshold(img,0,255,cv2.THRESH_OTSU)
    
    H,W=img_bin.shape
    
    print 'Ypsos',H,'platos',W
    TopRow=H
    BottomRow=0
    LeftCol=0
    RightCol=W
    
    
    #ahh these histograms again
    #compute vertical and horizontal histograms  almost
    
    
    
    
    #keep reading columns until you find one that has a black pixel
    found=0
    
    while LeftCol<W and found==0:
        
        r=0
        while r<H and found==0:
            
            #print r,LeftCol
            if img_bin[r][LeftCol]==0:
                found=1
            r+=1
        LeftCol+=1
           
    LeftCol-=1
    
    
    
    found=0
    
    while RightCol>0 and found==0:
        RightCol-=1
        r=0
        while r<H and found==0:
            
            #print r,RightCol
            if img_bin[r][RightCol]==0:
                found=1
            r+=1
        
           
    RightCol+=1
    
    
    
    found=0
    #you need to find the lowest black pixel
    
    for r in xrange(0,H):
        for c in xrange(0,W):
            if img_bin[r][c]==0 and r<TopRow:
                TopRow=r
    
    TopRow-=1
    
    found=0
    #you need to find the  black pixel with the highest row
    
    for r in xrange(0,H):
        for c in xrange(0,W):
            if img_bin[r][c]==0 and r>BottomRow:
                BottomRow=r
    
    BottomRow+=1
    print 'Bounding box is : LeftCol',LeftCol,'RightCol',RightCol,'TopRow',TopRow,'BottomRow',BottomRow
    
    
    #save the image to a new location
    Cropped=np.ones((BottomRow-TopRow,RightCol-LeftCol,1), np.uint8)
    Cropped.fill(255)
    
    i=-1
    for r in xrange(TopRow,BottomRow):
        i+=1
        j=-1
        for c in xrange(LeftCol,RightCol):
            j+=1
            Cropped[i][j]=img_bin[r][c]
            
            
    #cv2.imshow('cropped',Cropped)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    
    cv2.imwrite(outFolder + Word_Name + '.png',Cropped,[cv2.IMWRITE_PNG_COMPRESSION,95])
    
    
    