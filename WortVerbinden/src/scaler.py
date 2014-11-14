# -*- coding: UTF-8 -*- 
'''
Created on May 25, 2014
@author: phoenix
'''
import math,cv2

#OptikH
Caps=[1,0,0,0,0,0]
GlyphPaths=[]
GlyphPaths.append('/home/phoenix/Desktop/buchbilder/2014_04_21_20_01_51/Ὸ.png')
GlyphPaths.append('/home/phoenix/Desktop/buchbilder/2014_04_21_20_01_51/π.png')
GlyphPaths.append('/home/phoenix/Desktop/buchbilder/2014_04_21_20_01_51/τ.png')
GlyphPaths.append('/home/phoenix/Desktop/buchbilder/2014_04_21_20_01_51/ι.png')
GlyphPaths.append('/home/phoenix/Desktop/buchbilder/2014_04_21_20_01_51/κ.png')
GlyphPaths.append('/home/phoenix/Desktop/buchbilder/2014_04_21_20_01_51/ἡ.png')



ScaledPaths=[]
ScaledPaths.append('/home/phoenix/Desktop/buchbilder/new/O.png')
ScaledPaths.append('/home/phoenix/Desktop/buchbilder/new/p.png')
ScaledPaths.append('/home/phoenix/Desktop/buchbilder/new/t.png')
ScaledPaths.append('/home/phoenix/Desktop/buchbilder/new/i.png')
ScaledPaths.append('/home/phoenix/Desktop/buchbilder/new/k.png')
ScaledPaths.append('/home/phoenix/Desktop/buchbilder/new/h.png')


#main body should be the same
#as poyme oti exoyme to mikos toy mainbody (top most black pixel-lowest black pixel)
mainbody=[32.0,14.0,13.0,13.0,17.0,34.0]
scalefac=[]
#avg ?variance....

avg=0
var=0
m=0

#metra ayta poy DEN einai kefalaia
for i in xrange(0,len(Caps)):
    if Caps[i]==0:
        avg+=mainbody[i]
        m+=1

        
avg/=m
avg=int(avg)
print 'Average main body',avg

#variance 
for i in xrange(0,len(Caps)):
    if Caps[i]==0:
        var+=(mainbody[i]-avg)*(mainbody[i]-avg)
        m+=1
var/=m
var=math.sqrt(var)
print 'variance',var


for i in xrange(0,len(Caps)):
    #find how much we need to scale the main body
    if Caps[i]==1:
        scalefac.append(1)
    else:
        #either greater than one for scale up
        #or smaller than one for scaling down
        scalefac.append(avg/mainbody[i])

print scalefac
#scale each image ston katakoryfo axona ???
for p in xrange(0,len(GlyphPaths)):
    src=cv2.imread(GlyphPaths[p],cv2.CV_LOAD_IMAGE_GRAYSCALE)
    
    
    small = cv2.resize(src, (0,0), fx=1, fy=scalefac[p])   
    
    cv2.imshow('test',small)
    cv2.waitKey()
    cv2.imwrite(ScaledPaths[p],small)
    

cv2.destroyAllWindows()