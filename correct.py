#!/usr/bin/python
import re, collections
import sys

def lev(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

keyword = sys.argv[1]
with open('dict.txt') as f:
	content = f.readlines()
d = {}
for row in content:
	d[row] = lev(row,keyword)
ret = sorted(d.items(),key=lambda x:x[1])
print ret[:5]
#print '\n'.join(correct(sys.argv[1]))
