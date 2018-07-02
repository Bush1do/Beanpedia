from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import random

for x in range(1):
	x=random.randint(1,101)
	print(x)

myUrl='https://www4.bing.com/search?q=beans='+str(x)
print(myUrl)

#Opening connection
uClient=uReq(myUrl)
pageHtml=uClient.read()
uClient.close()

#Parsing part
pageSoup=soup(pageHtml, "html.parser")

# Grab products
boop=pageSoup.findAll("li",{"class":"b_algo"})

filename="Fact Spreadsheet.csv"
f=open(filename,"w")

headers="title, desc, link\n"

f.write("")

# Get Data
beep=boop[0]

for beep in boop:
	title= beep.a.text.strip()+"\n"
	desc= beep.p.text.strip()+"\n"
	link=beep.cite.text.strip()+"\n"

	#print(title,desc,link)
	f.write(title.replace(",","|")+","+desc.replace(",","|")+","+link+"\n")

f.close()
