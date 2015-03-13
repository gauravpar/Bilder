#show results of local gradient histogram dynamic time warping from database
import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="seidman", # your username
                      passwd="seidman@localhost", # your password
                      db="Washington") # name of the data base




texnites=[]
        
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT Distinct(SynthFile) FROM Stiles ORDER BY SynthFile ASC")

# print all the first cell of all the rows
for row in cur.fetchall() :
    texnites.append(row[0])
    
avg=0
maxavg=0            
FirstResults=3
MaxPossibleScore=0
for i in xrange(1,FirstResults+1):
    MaxPossibleScore+=i

Score_per_KeyWord=[] # store the average score of each keyword here

for synth in texnites:
    print '********************************************************'
    skor=0.0
    maxavg+=MaxPossibleScore
    cur.execute("select * from Stiles Where SynthFile='"+ synth +"' order by Score ASC LIMIT "+ str(FirstResults))
    ScorePos=0
    for row in cur.fetchall() :
        ScorePos+=1
        #print row
        truth=row[2]
        #get only the word remove sytnh_font name
        keyword=''
        pos=0
        #get last index of _

        for c in xrange(len(synth)):
            if '_' == synth[c]:
                pos=c+1
        keyword=synth[pos:].replace('.png','')
        
        print synth,truth,ScorePos
        if keyword in truth:
            skor+=FirstResults+1-ScorePos
        

    print 'skor for',synth,'is',skor
    
    Score_per_KeyWord.append(skor)
    avg+=skor
    
avg/=len(texnites)
print '-------------------------'


print 'maximum average skor is',MaxPossibleScore
print 'final average  skor is',avg
print 'final average percentage skor is',(avg*100.0)/MaxPossibleScore


print '-------------------------'
#sort array Score_per_Keyword aascending
Score_per_KeyWord, texnites = (list(x) for x in zip(*sorted(zip(Score_per_KeyWord, texnites), key=lambda pair: pair[0])))


#for i in range(0,len(texnites)):
#    print texnites[i],Score_per_KeyWord[i]
