#background to ink transitions

import cv2

col=[0,1,0,0,1,1,0,1,0,1,1,0,1,0,1]

trans=0
#count transitions from 0 to 1

for i in range(0,len(col)-1):
    if col[i]==0 and col[i+1]==1:
        trans+=1


print trans


#read a real Image
im=cv2.imread('/home/phoenix/Markov/Test/test1.jpeg',cv2.CV_LOAD_IMAGE_GRAYSCALE)
ret,im=cv2.threshold(im,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#WHITE is 255!!!!
H,W=im.shape


cv2.imshow('test',im)
cv2.waitKey()
cv2.destroyAllWindows()


Ink=[]
for col in xrange (0,W):
    count=0
    for row in xrange(0,H-1):
       
        if im[row][col]==0 and im[row+1][col]==255:
            count+=1
    Ink.append(count)

print Ink