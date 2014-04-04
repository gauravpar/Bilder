# -*- coding: UTF-8 -*- 
'''
Created on Apr 4, 2014
This is just a test module to store and load xml
In the xml you will store the char  the path to its glyph ,if it is a special char its dimensions the top , low line and baseline
The xml works as a backup in case everything is lost
@author: phoenix
'''
 
chars=['a','b']
Lang=["GR","GR"]
path=["/tmp/a.png","/tmp/r.png"]
spec=["No","Yes"]
Top=["8","12"]
Low=["28","32"]
Base=["28","24"]
X=["35","40"]
Y=["45","49"]


root=et.Element("root")

for c in chars:
    glyph=et.SubElement(root,"Glyph")
    glyph.set("name", "α")
    glyph.text = "some value1"
    
tree = et.ElementTree(root)
   
tree.write("filename.xml", xml_declaration=True, encoding='utf-8')    
tree.write("/tmp/filename.xml")
print 'ok'

