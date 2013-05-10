#!/usr/bin/env python

import os
import mapnik as mapnik

m = mapnik.Map(1200,600) # create a map with a given width and height in pixels
# note: m.srs will default to '+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs'
# the 'map.srs' is the target projection of the map and can be whatever you wish
ocean = '#a2ecf7'
m.background = mapnik.Color('#CCD8FF') 

outline = '#666666' #lighter grey 2
# Greens:
greens = '''
66C2A5
A6D854
8DA0CB
CD9DBB
FC8D62
E5C494
859900
'''.split()

for i,color in enumerate(greens):
    s = mapnik.Style() # style object to hold rules
    r = mapnik.Rule() # rule object to hold symbolizers
# to fill a polygon we create a PolygonSymbolizer
    polygon_symbolizer = mapnik.PolygonSymbolizer(mapnik.Color('#%s'%color))
    r.symbols.append(polygon_symbolizer) # add the symbolizer to the rule object
# to add outlines to a polygon we create a LineSymbolizer
    line_symbolizer = mapnik.LineSymbolizer(mapnik.Color(outline),0.4)
    r.symbols.append(line_symbolizer) # add the symbolizer to the rule object
    s.rules.append(r) # now add the rule to the style and we're done

    m.append_style('My Style %i'%(i+1),s) # Styles are given names only as they are applied to the map

    
def addLayerSimple(name, fileName):
    
    ds = mapnik.Shapefile(file=fileName)
    layer = mapnik.Layer(name)
    layer.datasource = ds
    layer.styles.append('My Style 1')
    m.layers.append(layer)

def addLayer(name, fileName):
    for i in range(1,8):
        newName = '%s_%i.shp'%(fileName,i)
        if os.path.isfile(newName):
            ds = mapnik.Shapefile(file=newName)
            layer = mapnik.Layer('%s_%i'%(name,i))
            layer.datasource = ds
            layer.styles.append('My Style %i'%i)
            m.layers.append(layer)