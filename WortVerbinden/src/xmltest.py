# -*- coding: UTF-8 -*- 
'''
Created on Apr 4, 2014
This is just a test module to store and load xml
In the xml you will store the char  the path to its glyph ,if it is a special char its dimensions the top , low line and baseline
The xml works as a backup in case everything is lost
The xml contains all the chars contains the the listwidget
@author: phoenix
'''
from xml.etree.ElementTree import ElementTree 
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree

chars=['α','ρ']
Lang=["GR","GR"]
Path=["/tmp/a.png","/tmp/r.png"]
Spec=["No","Yes"]
Top=["8","12"]
Low=["28","32"]
Base=["28","24"]
X=["35","40"]
Y=["45","49"]

root=Element("GlyphBook")
tree=ElementTree(root)
i=0
for ch in chars:
    glyph=Element("Glyph")
    root.append(glyph)
    c=Element("Char")

    glyph.append(c)
    c.text= ch
    
    
    spec=Element("Special")
    spec.text=Spec[i]
    glyph.append(spec)
    
    
    p=Element("Path")
    p.text=Path[i]
    glyph.append(p)

    l=Element("Lang")
    l.text=Lang[0]
    glyph.append(l)
    
    top=Element("Top")

   
    top.text=Top[i]
    glyph.append(top)
    
    low=Element("Low")

   
    low.text=Low[i]
    glyph.append(low)
    
    b=Element("Base")
    b.text=Base[i]
    glyph.append(b)
    
   
    x=Element("X")
    x.text=X[i]
    glyph.append(x)
    
   
   
   
   
    y=Element("Y")
    y.text=Y[i]
    glyph.append(y)
    
    
    
    
   
   
    
    i+=1


print etree.tostring(root, encoding='utf-8')

tree.write("/tmp/filename.xml", xml_declaration=True,encoding='utf-8' )    
print 'ok'

