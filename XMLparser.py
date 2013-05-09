import xml.sax
import csv
import urllib2
import time

global gateGlobalVariable0001
global gateGlobalVariable0002
global gateGlobalVariable0003
global currentElement 
currentElement = "placeholderElement"
global currentIssuer 
global fileURL
currentIssuer = "placeholderIssuer"
gateGlobalVariable0001 = "closed";
gateGlobalVariable0002 = "closed";
gateGlobalVariable0003 = "open";

class ABContentHandler(xml.sax.ContentHandler):
	def __init__(self):
		xml.sax.ContentHandler.__init__(self)
 
	def startElement(self, name, attrs):
		global gateGlobalVariable0001
		global gateGlobalVariable0002
		global gateGlobalVariable0003
		global currentIssuer
		global currentElement
		if name == "city" and gateGlobalVariable0003 == "open":
			currentElement = name
			gateGlobalVariable0001 = "open"
		if name == "entityName" or name == "entityType" or name == "totalOfferingAmount" or name == "totalAmountSold" or name == "totalOfferingAmount" or name == "industryGroupType" or name == "signatureDate":
			gateGlobalVariable0001 = "open"
			currentElement = name
		if name == "entityName":
			gateGlobalVariable0002 = "open"
		#print("startElement '" + name + "'" + " gate1:" + gateGlobalVariable0001 + " gate2:" + gateGlobalVariable0002)
		return ("Element", name)
 
	def endElement(self, name):
		# print("endElement '" + name + "'")
		myCool = 0
		
	def characters(self, content):
		global fileURL
		global gateGlobalVariable0001
		global gateGlobalVariable0002
		global gateGlobalVariable0003
		global currentIssuer
		global currentElement
		if gateGlobalVariable0002 == "open":
			currentIssuer = content
			gateGlobalVariable0002 = "closed"
		if gateGlobalVariable0001 == "open":
			gateGlobalVariable0001 = "closed"		
			csv_file.writerow([currentIssuer, currentElement, content, fileURL])
			if 	currentElement == "city":
				gateGlobalVariable0003 = "closed"
		#print("characters '" + content + "'" + " gate1:" + gateGlobalVariable0001 + " gate2:" + gateGlobalVariable0002)
	
def main(sourceFileName):
	global fileURL
	print sourceFileName
	fileURL = sourceFileName
	try: 
		source = urllib2.urlopen(sourceFileName)
	except urllib2.URLError:
		time.sleep(0.1)
		source = urllib2.urlopen(sourceFileName)
	xml.sax.parse(source, ABContentHandler())
	
index = 0
f = open("filelist.txt")
locationArray = {}
for line in f:
	locationArray[index] = str(line)
	#print locationArray[index]
	index += 1
#print locationArray;
with open("xmltest.csv", "wb") as file:
	csv_file = csv.writer(file)
#	print "break dance!"
#	print locationArray;
	for i in range(len(locationArray)):
		myStr = locationArray[i]
		realLength = len(myStr)-1
		main(myStr[:realLength])
		gateGlobalVariable0001 = "closed";
		gateGlobalVariable0002 = "closed";
		gateGlobalVariable0003 = "open";


