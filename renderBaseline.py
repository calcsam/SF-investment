#!/usr/bin/env python

import os
import mapnik as mapnik
import renderCommon as rend
import split_mapColors as splitColors


for color in range(1,8):
    splitColors.cropMapColor('2013_transformation', color)


rend.addLayer("World", '2013_transformation')

rend.m.zoom_all()

mapnik.render_to_file(rend.m, 'New__Map_2013.png', 'png')
