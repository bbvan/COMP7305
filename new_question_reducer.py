#!/usr/bin/python
import sys
import os
for line in sys.stdin:
    line = line.strip()
    row = line.split('\t')
    part1 = row[0].split('#')
    score = row[1]
    if score == "-1":
	print line
	continue
    tag = parseTag(row[1])
    accepted_answer_id = row[0]
    if accepted_answer_id=="" or accepted_answer_id=="None":                          
            continue
    score = similarity(user_tag,tag)
    if score>=max_similarity:
        max_similarity = score
        question_count+=1
        if question_count>max_count:
            break
	body = row[2]
        print "{0}\t{1}".format(accepted_answer_id,body)                            
    else:                                                                                  
        continue 
