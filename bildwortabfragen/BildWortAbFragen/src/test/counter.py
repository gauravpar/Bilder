'''
Created on Aug 12, 2014

@author: phoenix
'''
#count how many times the keyword appers in the truth file

KeyWordFile='/home/phoenix/Desktop/handcraft/lexeis.txt'
TruthFile='/home/phoenix/washingtondb-v1.0/ground_truth/word_labels.txt'


with open(KeyWordFile) as keyfile:
    for line in keyfile:
        key=line.replace('\n','')
        
        occurs=0
        with open(TruthFile) as truthfile:
            for grammi in truthfile:
                if key in grammi:
                    occurs+=1
        
        
        print key,occurs