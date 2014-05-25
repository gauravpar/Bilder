'''
Created on May 7, 2014

@author: phoenix
'''
#baselineis 69

import cv2
import numpy as np


def main():
    #no grid just horizontal lines
    #if whitespace more than a threshold 
    #shift
    qr=cv2.imread('/home/phoenix/Desktop/faq.png',cv2.CV_LOAD_IMAGE_GRAYSCALE)
    
    h,w=qr.shape
    bline=68
    
    print 'height is',h
    print 'width is',w
    
     
    #calc white space above the red line
    
    #many stop cols #last element of stopfiles is the end of the char
    stopstiles=[139,256,374,495,410] 
    noblank=[24,24,24,24,0]
    charwidth=[48,48,48,48,0]
    
    
    #stopcol=1
    #while stopcol>0:
    #    stopcol=int(raw_input("enter stop col"))
    #    nowhite=int(raw_input("no white space"))
    #    stopstiles.append(stopcol)
    #    noblank.append(nowhite)
    
    
    #user help
   

    
    
    winid=0
    cv2.imshow('original',qr)
    
    nospace=Shifter(qr, h, w, bline, stopstiles[0], stopstiles[1], noblank[0], charwidth[0],winid)
    winid+=4
    nospace=Shifter(nospace, h, w, bline, stopstiles[1]-noblank[0], stopstiles[2], noblank[1], charwidth[1],winid)
    
    winid+=4
    nospace=Shifter(nospace, h, w, bline, stopstiles[2]-noblank[0], stopstiles[3], noblank[1], charwidth[1],winid)
    
  
    
    cv2.imshow('final',nospace)


    cv2.waitKey()
    cv2.destroyAllWindows()   

    



    
def Shifter(arr_pic,ypsos,platos,bline,stopq,stopqnext,noblankq,charwidthq,picid):    
    print 'new loop'
    neo= np.ones((ypsos,platos,1), np.uint8)
    neo.fill(255)
    
  
    print 'Copying from zero to',stopq
    #copy all the pixels up to the first stop col before the limit of the descender
    for row in range(0,ypsos):
        for col in range(0,stopq):
            neo[row][col]=arr_pic[row][col]
    
    cv2.imshow('copy pixels'+ str(picid),neo)
    
    
    picid+=1
    
    #progressive shifting
    #shift all pixel right from  stopcol+noblack  to stopcol[1] to the left by no blank
    
    print 'Copying mainbody from col',stopq+noblankq,'to',stopqnext

    #copy main body!!!
    for row in range(0,bline):
        for col in range(stopq,stopqnext-noblankq):
           
            neo[row][col]=arr_pic[row][col+noblankq]
    
    
    cv2.imshow('shift main body left' + str(picid),neo)
    picid+=1
    
    
    #copy descender!!!
    for row in reversed(range(bline,ypsos)):
        for col in range(stopq,stopq+charwidthq):
            neo[row][col-noblankq]=arr_pic[row][col]
    
    
    
    cv2.imshow('shift ascender' + str(picid),neo)
    
    picid+=1
    

    
    shiftrem=noblankq
    #copy the remainder of the unshifted image
    for row in range(0,ypsos):
        for col in range(stopqnext,platos):
            neo[row][col-shiftrem]=arr_pic[row][col]   #SHIFT what will be shifted in the next loop by shiftrem
            
            
            
    cv2.imshow('shift remaining unshifted' + str(picid),neo)
    
    picid+=1
    return neo
    


if __name__ == '__main__':    
    main()
