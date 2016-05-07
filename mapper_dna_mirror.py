#!/usr/bin/python
import fileinput
for line in fileinput.input():
	word=line.split()
	#print ''.join(reversed(word[0]))
	print min(word[1],''.join(reversed(word[1])))+"\t"+word[0]
        	#if ''.join(sorted(list(word)))== word:
			#print ''.join(sorted(list(word))) + "\t" + word
	#print word[1]+"\t"+word[0]
