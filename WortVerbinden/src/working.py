# -*- coding: UTF-8 -*- 
#Build the word image  using a very naive approach
#we assume in this script that all characters  's gylphs are of roughly equal dimensions
#memory consuming....
import numpy as np
import cv2
#Space between words?????
BlackThreshold=6
Shift=12 #we can shift the baseline a few rows down
query=raw_input("")
BaseDir='/home/phoenix/Verbinden/'
tmp='/tmp/'
GlyphBook=[]
#those will be stored in a mysql database
GlyphBook.append(['Ο', BaseDir+'O.png'])
GlyphBook.append([' ', BaseDir+'space.png'])
GlyphBook.append(['α', BaseDir+'a.png'])
GlyphBook.append(['β', BaseDir+'b.png'])
GlyphBook.append(['γ', BaseDir+'g.png'])
GlyphBook.append(['δ', BaseDir+'d.png'])
GlyphBook.append(['ε', BaseDir+'e.png'])
GlyphBook.append(['ζ', BaseDir+'z.png'])
GlyphBook.append(['η', BaseDir+'h.png'])
GlyphBook.append(['θ', BaseDir+'th.png'])
GlyphBook.append(['ι', BaseDir+'i.png'])
GlyphBook.append(['κ', BaseDir+'k.png'])
GlyphBook.append(['λ', BaseDir+'l.png'])
GlyphBook.append(['μ', BaseDir+'m.png'])
GlyphBook.append(['ν', BaseDir+'n.png'])
GlyphBook.append(['ξ', BaseDir+'xx.png'])
GlyphBook.append(['ο', BaseDir+'o.png'])
GlyphBook.append(['π', BaseDir+'p.png'])
GlyphBook.append(['ρ', BaseDir+'r.png'])
GlyphBook.append(['ς', BaseDir+'s.png'])
GlyphBook.append(['σ', BaseDir+'sig.png'])
GlyphBook.append(['τ', BaseDir+'t.png'])
GlyphBook.append(['υ', BaseDir+'u.png'])
GlyphBook.append(['φ', BaseDir+'phi.png'])
GlyphBook.append(['χ', BaseDir+'x.png'])
GlyphBook.append(['ψ', BaseDir+'psi.png'])
GlyphBook.append(['ω', BaseDir+'w.png'])

glyphs=[]

QueryX=0
QueryY=0
XLines=[] #baseline for each glypl
YDims=[] #glyph dimensions
XDims=[]


#find the maximum  X dimension of all glyphs
#the final image should be 2*X and the sum of all Ys
#We know the first char is NOT a γ,ζ,η,μ,ξ,ρ
#get the baseline of the first glyph
#we should read all glyphs at the start 
#and store their baselines no need to recalculate them
for q in query:
    #find q in Glyphs
    print 'searching for char', q
    for n in range(0, GlyphBook.__len__()):
        if q in GlyphBook[n][0].decode('utf-8'):
            break
    else:
        continue
        
    print 'Reading Glyph', GlyphBook[n][1]
    glyphs.append(GlyphBook[n][1])
    tmp=cv2.imread(GlyphBook[n][1])
    
    x, y, z=tmp.shape
    QueryY+=y
    if x>QueryX:
        QueryX=x
    XDims.append(x)
    YDims.append(y)

    if 'ρ'.decode('utf-8') not in q:
       print 'character is not an ρ' 
       #read it from bottom to top
       #problem with glyph s bad print
       for i in reversed(range(0,x)):
           for j in range(0,y):
               if tmp[i][j][0]<BlackThreshold and tmp[i][j][1]<BlackThreshold and  tmp[i][j][2]<BlackThreshold:
                   print  i,j
                   #append the base line of each glyph
                   XLines.append(i)
                   
                   print 'Baseline for char ',q, 'is', i
                   break
           else:
                continue
           break
    else:
       
       print 'ρ is in query--------------------------------------------------'
       top=0
       low=0
       #get  the low line
       for i in reversed(range(0,x)):
           for j in range(0,y):
               if tmp[i][j][0]<BlackThreshold and tmp[i][j][1]<BlackThreshold and  tmp[i][j][2]<BlackThreshold:
                   print  i,j
                   
                   low=i
                   
                   break
           else:
                continue
           break
       #and the top line
       for i in range(0,x):
            for j in range(0,y):
                if tmp[i][j][0]<BlackThreshold and tmp[i][j][1]<BlackThreshold and  tmp[i][j][2]<BlackThreshold:
                    print  i,j
                    top=i
                    break
            else:
                continue
            break
       line=int(0.88*abs((top-low))) # the lower the value the higher the position of char  
       XLines.append(line)
       print 'Fixed Baseline for char ',q, 'is', line
       
       #output the naive baseline for r
       rbild= np.ones((x,y,3), np.uint8)
       rbild=tmp
       for i in range(0, y):
           rbild[line][i][0]=255
           rbild[line][i][1]=0
           rbild[line][i][2]=0
           
           rbild[top][i][2]=255
           rbild[top][i][0]=0
           rbild[top][i][1]=0
           
           rbild[low][i][0]=0
           rbild[low][i][1]=0
           rbild[low][i][2]=255
        #detected baseline for strange characters
       cv2.imwrite("/tmp/"+q.encode('utf-8')+".png", rbild)

            
       
       
#------------------------------------------------------------------------------------------------
#Begin synthesizing
print 'Synthesizing...'
#NAIVE ASSUMPTION
QueryX*=2
print 'Image Query lines',QueryX, 'columns', QueryY
#gemise tin me aspro
ImgQuery= np.ones((QueryX,QueryY,3), np.uint8)
ImgQuery.fill(255)
#maybe we must shfit a few rows  DOWN 
#append first char
StartColumn=0
diff=0

print 'Base is ', XLines[0]
for c in range(0, query.__len__()):
   
   
    tmp=cv2.imread(glyphs[c])
    
    XLines[c]+=Shift
    diff=abs(XLines[c]-XLines[0]) + Shift
        
    print 'Careful baseline ', glyphs[c], 'at', diff, 'base was', XLines[c]
    for i in range(0, XDims[c]):
        for j in range(0, YDims[c]):
            ImgQuery[i+diff][j+StartColumn][0]=tmp[i][j][0]
            ImgQuery[i+diff][j+StartColumn][1]=tmp[i][j][1]
            ImgQuery[i+diff][j+StartColumn][2]=tmp[i][j][2]
            
    StartColumn+=YDims[c]
    
 
    
#draw a red line one baseline
for j in range(0, QueryY):
    ImgQuery[XLines[0]][j][0]=0  #green
    ImgQuery[XLines[0]][j][1]=0  # blue
    ImgQuery[XLines[0]][j][2]=255 # red
    
    
cv2.imshow('Word Query', ImgQuery)
cv2.imwrite("/tmp/" + query.encode('utf-8') +".png", ImgQuery)

cv2.waitKey(0)
cv2.destroyAllWindows()   
