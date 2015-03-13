'''
Created on Aug 19, 2014

@author: phoenix
'''
import glob,cv2,os,numpy as np
#all hands should have a height of 120 and width 1150 
#1150 is the maximum width of the scaled synthetic...


#the class is the synthetic query




#white cols

maxW=0
maxH=0


HandSet=glob.glob('/home/phoenix/washingtondb-v1.0/data/word_images_normalized/*.png')


for pic in HandSet:
    img=cv2.imread(pic,cv2.CV_LOAD_IMAGE_GRAYSCALE)
    ret,img=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    H,W=img.shape   
    extra_cols=0
    while W<650:
        W+=1
        extra_cols+=1
    
     
    ext_img= np.ones((H,W,1), np.uint8)
    ext_img.fill(255)
    
    for i in xrange(0,H):
        #copy old image
        for j in xrange(0,W-extra_cols):
            ext_img[i][j]=img[i][j]
 
        #save image
    
    filename='/home/phoenix/Desktop/ext_hand/' + os.path.basename(pic)
    print filename
    cv2.imwrite(filename,ext_img,[cv2.IMWRITE_PNG_COMPRESSION,95])


