#!/usr/bin/python
import sys
for line in sys.stdin:
    line = line.strip()
    row = line.split('"')
    post_type = row[1]
    #print "post_type: "+post_type
    if post_type=="2":
        answer_id = row[0]
        owner_id = row[4]
        print "{0}\t{1}".format(answer_id,owner_id)
    else:
        continue
