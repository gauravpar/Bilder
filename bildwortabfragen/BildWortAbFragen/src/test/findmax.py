'''
Created on Aug 19, 2014

@author: phoenix
'''
import glob,cv2
#find the maximum h and w from all images

maxW=0
maxH=0


HandSet=glob.glob('/home/phoenix/washingtondb-v1.0/data/word_images_normalized/*.png')

maxfile=''


for pic in HandSet:
    im=cv2.imread(pic,cv2.CV_LOAD_IMAGE_GRAYSCALE)
    ret,im=cv2.threshold(im,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    H,W=im.shape    
    print 'reading',pic,H,W


    if H>maxH:
        maxH=H
    if W>maxW:
        maxW=W
        maxfile=pic


print 'max h',maxH,'max w',maxW
print maxfile