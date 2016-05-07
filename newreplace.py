#!/usr/bin/python
import fileinput
for line in fileinput.input():
	for word in line.split():
		for letter in list(word):
			print letter;
