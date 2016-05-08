#!/usr/bin/python
from difflib import SequenceMatcher
import sys
MAX = 0
tag1 = sys.argv[1]
values_map = {}
with open('dict.txt') as source:
	for line in source:
		line = line.strip()
		similarity = SequenceMatcher(None, line, tag1).ratio()
		# try:
		values_map[line]=similarity
		# except Exception:
		# 	continue
values_map=sorted(values_map.iteritems(), key=lambda d:d[1], reverse=True)

for value in values_map[0:10]:
	print value[0],
