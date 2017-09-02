import sys
import os
from shutil import copyfile

count_words = dict()

def countWords():
	count_file = open('gene.count', 'r')
	line = count_file.readline()
	while line:
		tup = line.strip().split()
		if(tup[1] == 'WORDTAG'):
			tempcnt = int(tup[0])
			tag = tup[2]
			word = tup[3]
			if word in count_words:
				count_words[word] = count_words[word] + tempcnt
			else:
				count_words[word] = tempcnt
		line = count_file.readline()
	count_file.close()

def main():
	count_file = open('gene.count', 'r')
	count_file2 = open('gene2.count', 'w')
	line = count_file.readline()
	while line:
		tup = line.strip().split()
		if(tup[1] == 'WORDTAG'):
			word = tup[3]
			if(count_words[word] <= 5):
				tup[3] = '_RARE_'
		new_line = ' '.join(tup)
		line = count_file.readline()
		count_file2.write(new_line + '\n')
	count_file.close()
	count_file2.close()

countWords()
main()