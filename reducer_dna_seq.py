#!/usr/bin/python
import fileinput
key=''
value=''
data = ''
#lines=fileinput.input()
#print lines
for line in fileinput.input():
	words = line.split()
	#print words[0]+"  "+words[1]
	if(key==''):
		key=words[0].rstrip()
		data=data+words[0]+"="+words[1]
	elif(key==words[0]):
		data=data+","+words[1]
	else:
		key=words[0]
		#anagram=data.split(",");
		#if(len(anagram)>1):
		print data
		data="";
		data=data+words[0]+"="+words[1]
		#print anagram[0]+"  "+anagram[1]
print data
#print "Yogesh"
#print key
#print data

	#words = line.split()
	#data[words[0]].append(words[1])
	#if(words[0] == key or key == ''):
	#	key=words[0]
	#	value=value+","+words[1]
	#	print key , value 
	#print words
	#for word in line.split():
		#print ''.join(sorted(list(word))) + ":" + word
	#print line
	#word = line.split:
#print word
	
	#for word in line.split():
		#prev_value=
       		#if ''.join(sorted(list(word)))== word:
			#print ''.join(sorted(list(word))) + "\t" + word
			#print word
