import shapefile
import csv

# Read in our existing shapefile
r = shapefile.Reader("zt06_d00")
w = shapefile.Writer()
print "are we getting here?"
print r

# Copy over the existing fields
w.fields = list(r.fields)

def deleteShape(n):
	del r.records[n]
	del r._shapes[n]
	return

def InBayArea(myRec):
	with open('Bay_Area_New_ZIP_List.csv', 'rb') as f:
		reader = csv.reader(f)
		#print "not there"
		for row in reader:
			#print myRec[1] + " " + row[0]
			if myRec[4] == row[0]:
				return True
	return False
	
w.shapeType = 5	
i = 1
for sr in r.shapeRecords():
	#print ",ome"
	sr_test = sr.record
	# print sr_test
	if InBayArea(sr_test):
		w.records.append(sr_test)
		w._shapes.append(sr.shape)
	#w._shapes[0] = sr.shape
	#w.records[0] = sr_test
	i+=1
print w._shapes[0]
# Save as a new shapefile (or write over the old one)
print w
w.save("BayArea_new_zipcodes") 

