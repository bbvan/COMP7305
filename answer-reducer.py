#!/usr/bin/python
import sys
answer2owner = {}
answer_list = []
printed_users = []
answer_body_map = {}
answers = open('accepted_answer.txt','r')
for l in answers:
	l = l.strip().split('\t')
	if l[0] == None or l[0] == "":
		continue
	else:
#		print l
		answer_list.append(l[0])
		answer_body_map[l[0]]=l[1]
#print answer_list

answers.close()
for line in sys.stdin:
	data = line.strip().split("\t")
	length = len(data)
	if length==2:
		answer_id = data[0]
		owner_id = data[1]
		if owner_id == None or owner_id == "":
			continue
		if answer_id in answer_list and owner_id not in printed_users:
			printed_users.append(owner_id)
			print "{0},{1}".format(owner_id,answer_body_map[answer_id])
	else:
		continue
