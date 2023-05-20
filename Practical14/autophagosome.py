import xml.dom.minidom
import re
import pandas
DOMTree=xml.dom.minidom.parse("go_obo.xml")
element=DOMTree.documentElement
terms=element.getElementsByTagName("term")
def childnodes(ID):
    node = 0
    for i in terms:
        is_a = i.getElementsByTagName('is_a')
        for j in is_a:
            if j.childNodes[0].nodeValue == ID:
                node += childnodes(i.getElementsByTagName('id')[0].childNodes[0].nodeValue)+1
    return node
data=[]
for i in terms:
	definition=i.getElementsByTagName("defstr")[0].childNodes[0].nodeValue
	if re.search("autophagosome",definition):
		id=i.getElementsByTagName("id")[0].childNodes[0].nodeValue
		name=i.getElementsByTagName("name")[0].childNodes[0].nodeValue
		number=childnodes(i.getElementsByTagName("id")[0].childNodes[0].nodeValue)
		data.append([id,name,definition,number])
df=pandas.DataFrame(data,columns=["id","name","definition","childnodes"])
df.to_excel("autophagosome.xlsx",index=False)