'''
Created on May 7, 2014

@author: phoenix
'''
#baselineis 69
import cv2
import numpy as np

#ante pali apo tin arxi



def main():
    #no grid just horizontal lines
    #if whitespace more than a threshold 
    #shift
    qr=cv2.imread('/home/phoenix/Desktop/buchbilder/tog.jpg',cv2.CV_LOAD_IMAGE_GRAYSCALE)
    
    h,w=qr.shape
    bline=80
    
    print 'height is',h
    print 'width is',w
    
     
    
    #oi stopstiles periexoun ton aritho stilis opoy yparxei to provlima
    #px stin lexi thought  yparxei provlima metaxy tou u kai g 
        
    stopstiles=[150,326]  # to 150 einai ekei pou teleiwnei to u 
    #to teleytaio noumero einai i teleytaia stili tis eikonas
    noblank=[24,0] # ayto prepei na einai to paxos tis ouritsas toy descender
    
    
    charwidth=[48,0]
    
    

    
    
    winid=0
    cv2.imshow('original',qr)
    
    nospace=Shifter(qr, h, w, bline, stopstiles[0], stopstiles[1], noblank[0], charwidth[0],winid)
  
    
  
    
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
    
    cv2.imwrite('/tmp/desc' + str(picid)+".jpg" ,neo)
    
    picid+=1
    
    #progressive shifting
    #shift all pixel right from  stopcol+noblack  to stopcol[1] to the left by no blank
    
    print 'Copying mainbody from col',stopq+noblankq,'to',stopqnext

    #copy main body!!!
    for row in range(0,bline):
        for col in range(stopq,stopqnext-noblankq):
           
            neo[row][col]=arr_pic[row][col+noblankq]
    
    
    cv2.imshow('shift main body left' + str(picid),neo)
    cv2.imwrite('/tmp/desc' + str(picid)+".jpg" ,neo)

    picid+=1
    
    
    #copy descender!!!
    for row in reversed(range(bline,ypsos)):
        for col in range(stopq,stopq+charwidthq):
            neo[row][col-noblankq]=arr_pic[row][col]
    
    
    
    cv2.imshow('shift ascender' + str(picid),neo)
    cv2.imwrite('/tmp/desc' + str(picid)+".jpg" ,neo)

    
    picid+=1
    

    
    picid+=1
    return neo
    


if __name__ == '__main__':    
    main()
