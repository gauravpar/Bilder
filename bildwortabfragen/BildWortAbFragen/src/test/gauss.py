'''
Created on Jul 19, 2014

@author: phoenix
'''
#read the hand written features preform a Expectation maximization
#add zeroes when needed
import pickle


Hand_Feats=[]

max=0
for hf in Hand_Feats:
    print hf
    if len(hf)>max:
        max=len(hf)

#add zeroes
for hf in Hand_Feats:
    if len(hf)<max:
        for i in xrange(0,max-len(hf)):
            hf.append(0)
            
            
#EM
