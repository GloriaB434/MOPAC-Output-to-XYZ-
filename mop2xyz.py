'''
Takes a mopac output file and writes the optimized coordinates to an xyz file. You will need to set the appropriate input &
output file names as well as the correct number of atoms for your system.
by Gloria Bazargan
April 7, 2017
'''
#!/usr/bin/env python
#import necessary packages
import string,sys
import numpy as np
from numpy import *

#read in the mopac output file
with open("ouput.out", "r") as f:
    content = []
    cartesian = 0
#find the second occurance of 'CARTESIAN COORDINATES' the optimized coordinates are printed here
    for line in f:
        if cartesian >= 2:
            content.append(line)
        if 'CARTESIAN COORDINATES' in line:
            cartesian += 1
#convert the content to an area for iterating over
coords = np.array(content)

#open an intermediate file to write to this is not used for anything except plucking out the necessary information
with open('data.txt', 'w') as f:
        for i in range (213):    #Set the range to be No. atoms + 1
                f.write(coords[i])
f.close()

#open the xyz file that the optimized coordinates will be written to
g = open("data.txt", "r")
h = open("output.xyz", "w")

#Write the number of atoms to the first line of the xyz file
h.write('212\n')
h.write('made with mop2xyz by GB\n')

#Eliminate the first column that countains the atom numbers 1-X these cannot be read by most visualizers
for line in g:
    if line.strip():
        h.write("\t".join(line.split()[1:]) + "\n")

g.close()
h.close()
