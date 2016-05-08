#!/usr/bin/python
from difflib import SequenceMatcher
import sys
words=set(open('dict.txt').read().split())
tag1 = sys.argv[1]
values_map = {}
for word in words:
	values_map[word]=SequenceMatcher(None,word,tag1).ratio()
values_map=sorted(values_map.iteritems(), key=lambda d:d[1], reverse=True)

for value in values_map[0:5]:
	print value[0],
