'''
Created on Aug 12, 2014

@author: phoenix
'''
#a measure of success
#10 points for first place
#9 for second
#8 for third...
#1 for 10th place
#if the word appears less than 10 times count up to the word occurrence????
def Score(sc):
    sum=0
    for i in range(0,len(sc)):
        if sc[i]==1:
            sum+=10-i
    return sum



occurs=10

Ergebins=[]
results=[1,0,0,0,0,0,0,0,0,0]
Ergebins.append(results)
results=[0,0,1,1,0,0,1,1,0,0]
Ergebins.append(results)
results=[1,1,1,1,0,0,1,1,0,0]
Ergebins.append(results)
results=[1,0,0,0,0,0,0,1,0,0]
Ergebins.append(results)
results=[0,0,1,0,0,0,0,1,0,0]
Ergebins.append(results)
results=[1,0,0,0,0,1,0,1,0,0]
Ergebins.append(results)
results=[0,0,1,0,0,0,0,0,0,0]
Ergebins.append(results)
results=[0,0,0,0,0,0,0,0,0,0]
Ergebins.append(results)
results=[0,0,0,0,0,0,0,0,0,1]
Ergebins.append(results)
results=[0,0,0,0,0,0,0,0,1,1]
Ergebins.append(results)
results=[1,0,0,0,0,0,0,1,1,0]
Ergebins.append(results)
results=[1,0,0,0,0,0,1,0,0,1]
Ergebins.append(results)

avg=0.0

for res in Ergebins:
    print '-------------'
    print res
    #divide by the best score possible
    #occurence should go here
    best=0.0
    for i in xrange(1,11):
        best+=i
    print 'best',best
    skor=Score(res)/best
    avg+=skor
    
print 'average',avg/len(Ergebins)
    


        