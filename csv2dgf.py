import csv
import sys
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('infile', type=argparse.FileType('r'))
ap.add_argument('outfile', type=argparse.FileType('w'))

args = ap.parse_args()

edges = []
vertices = -1
vert_names = [ "" ]
j = 0
with args.infile as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if vertices == -1:
            vertices = len(row)-1
            for i in range(1, vertices +1):
                vert_names.append("%d_%s"%(i,row[i]))
        else:
            j += 1
            for i in range(j, vertices +1):
                if int(row[i]) == 1:
                    edges.append([ vert_names[i],vert_names[j] ])

args.infile.close()

with args.outfile as dgffile:
    print >>dgffile, "c Created with csv2dgf"
    print >>dgffile, "p edge %d %d"%(vertices, len(edges))
    for e in edges:
        print >>dgffile, "e %s %s"%(e[0],e[1])


args.outfile.close()
