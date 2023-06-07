#!/usr/bin/env python3
#
#--------------------------------------------------------------------
# Parse the SPICE model files from sky130 and use the (commented out)
# statistics block to generate the correct monte carlo expressions
# in the device models for mismatch.
#--------------------------------------------------------------------

import os
import re
import sys

mm_switch_param = 'MC_MM_SWITCH'

options = []
arguments = []
for item in sys.argv[1:]:
    if item.find('-', 0) == 0:
        options.append(item[1:])
    else:
        arguments.append(item)

variant = '/home/krzysztof/'
walkpath = variant + 'books'

filelist = []

print(walkpath)

for dirpath, dirnames, filenames in os.walk(walkpath):
	for filename in filenames:
		print(filename)
		
	
	
print('end')       

