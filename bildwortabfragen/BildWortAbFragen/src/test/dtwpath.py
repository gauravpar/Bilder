'''
Created on Jul 11, 2014

@author: phoenix
'''
from  random  import randrange
import math



S=[]
T=[]

for j in range(0,96):
    S.append(randrange(100))

for j in range(0,120):
    T.append(randrange(100))



M=[]
for i in range(0,len(S)):
    tmp=[]
    for j in xrange(0,len(T)):
        tmp.append(0)
    M.append(tmp)


for i in xrange(0,len(S)):
    M[i][0]=float("inf")

for i in xrange(0,len(T)):
    M[0][i]=float("inf")
    
M[0][0]=0



    
#DTW   
    
for i in xrange(1,len(S)):
    for j in xrange(1,len(T)):
    
        M[i][j]=(S[i]-T[j])**2 +min(M[i-1][j],M[i][j-1],M[i-1][j-1])
   


#wrap path
#find at each step the lowest cost of the nearby cell

    
#put infinity in a band..... R=3
R=3*len(T)/4


for i in xrange(0,len(S)):
    for j in xrange(0,len(T)):
        if abs(j-i)>=R: 
            M[i][j]=float("inf")





for tmp in M:
    print tmp
        

i=i_prev=len(S)-1
j=j_prev=len(T)-1
        
mikos=0    
while i>0 and j>0:

    
    print i,j
    if M[i-1][j]<=M[i-1][j-1] and M[i-1][j]<=M[i][j-1]:
        i_prev=i-1
        j_prev=j
        
    elif M[i-1][j-1]<=M[i-1][j] and M[i-1][j-1]<=M[i][j-1]:
        i_prev=i-1
        j_prev=j-1
        
        
    elif M[i][j-1]<=M[i-1][j-1] and M[i][j-1]<=M[i-1][j]:
        i_prev=i
        j_prev=j-1
        
    
    i=i_prev
    j=j_prev
    mikos+=1
    
print 'mikos',mikos
print 'kostos',M[len(S)-1][len(T)-1]
print 'match',float(M[len(S)-1][len(T)-1]/mikos)

    
    