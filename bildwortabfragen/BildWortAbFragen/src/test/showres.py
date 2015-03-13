#show results from database be it LGH DTW of profile DTW
import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="seidman", # your username
                      passwd="seidman@localhost", # your password
                      db="Regina") # name of the data base




texnites=[]
        
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT Distinct(query) FROM Results")

# print all the first cell of all the rows
for row in cur.fetchall() :
    texnites.append(row[0])
    
            

for t in texnites:
    print '********************************************************'
    cur.execute("select * from Results Where query='"+ t+"' order by Skor ASC LIMIT 10")
    for row in cur.fetchall() :
        print row
    
    