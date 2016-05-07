#!/usr/bin/python
import fileinput
for line in fileinput.input():
	word=line.split()
        	#if ''.join(sorted(list(word)))== word:
			#print ''.join(sorted(list(word))) + "\t" + word
	print word[1]+"\t"+word[0]
