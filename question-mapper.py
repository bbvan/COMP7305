#!/usr/bin/python
import sys
import os
tag1 = str(os.environ.get('tag1'))
tag2 = str(os.environ.get('tag2'))
tag3 = str(os.environ.get('tag3'))
tag4 = str(os.environ.get('tag4'))
user_tag = [tag1,tag2,tag3,tag4]

def similarity(tags1, tags2):
    score = 0
    for tag1 in tags1:
	if tag1=="None" or tag1=="":
		continue
	for tag2 in tags2:
		if tag2==tag1:
			score+=1
    return score

def parseTag(tag):
    strings = str(tag).split("&gt;&lt;")
    for x in range(len(strings)):
        strings[x] = strings[x].strip('&gt;').strip('&lt;')
    return strings

for line in sys.stdin:
    line = line.strip()
    row = line.split('"')
    post_type = row[1]
    #print "post_type: "+post_type
    #1->question,2->answer,row[0]->post_id,row[4]->owner_id
    if post_type=="2":
	if row[4]=="None" or row[4]=="":
		continue
	print "{0},{1},{2}".format(9,row[0],row[4])
    elif post_type=="1":
	tags = parseTag(row[2])
	accepted_answer_id = row[3]
	if accepted_answer_id=="" or accepted_answer_id=="None" or tags=="" or tags=="None":
                continue
	score = similarity(user_tag,tags)
	if score == 0:
		continue
	print "{0},{1},{2}".format(0,accepted_answer_id,score)
    else:
	continue 
