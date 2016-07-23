#!/usr/bin/python
import fileinput
for line in fileinput.input():
	for word in line.split():
        	#if ''.join(sorted(list(word)))== word:
			print ''.join(sorted(list(word))) + "\t" + word
