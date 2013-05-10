#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shapefile
import csv

mapColor_index = 30 #mapcolor7 in natural earth shapefile

#ifile  = open('city_classifier.csv', "rb")
#reader = csv.reader(ifile)
#rownum = 0
#cityDictionary = {}
#for row in reader:
#    cityDictionary[row[0]] = row[1]
#ifile.close()

def cropMapColor(sfOrigin, color_index):
    sf = shapefile.Editor(sfOrigin)

    def deleteShape(n):
        del sf._shapes[n]
        del sf.records[n]
        return
   # for r in sf.records:
    #    for i,f in enumerate(r):
     #       if isinstance(f, str):
      #          r[i] = unicode(f,'cp1252')

    print  'deleteing ', 
    for i,r in reversed(list(enumerate(sf.records))):
        print r[2],
        if r[2] != color_index:
            print i,
            print r[2],
            #print color_index,
            #print cityDictionary[r[1]] == color_index,
            deleteShape(i)

    #for r in sf.records:
     #   for i,f in enumerate(r):
      #      if isinstance(f, unicode):
       #         r[i] = f.encode('cp1252')

    foutname = '%s_%i'%(sfOrigin, color_index)
    if len(sf.records) == 0:
        print "This file %s doesn't have any data and is not rendered"%foutname
    else:
        print 'Outputting: ',foutname
        sf.save(foutname)

