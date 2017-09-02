import sys
from shutil import copyfile
import pickle

count_words = dict()
count_wordtags = dict()
count_unigrams = dict()
count_bigrams = dict()
count_trigrams = dict()

def count():
	count_file = open('gene2.count', 'r')
	line = count_file.readline()
	while line:
		tup = line.strip().split()
		if(tup[1] == 'WORDTAG'):
			tempcnt = int(tup[0])
			tag = tup[2]
			word = tup[3].lower()
			if word+' '+tag in count_wordtags: 
				count_wordtags[word+' '+tag] = count_wordtags[word+' '+tag] + tempcnt
			else:
				count_wordtags[word+' '+tag] = tempcnt
			if word in count_words:
				count_words[word] = count_words[word] + tempcnt
			else:
				count_words[word] = tempcnt
		elif(tup[1] == '1-GRAM'):
			tempcnt = int(tup[0])
			tag = tup[2]
			if tag in count_unigrams:
				count_unigrams[tag] = count_unigrams[tag] + tempcnt
			else:
				count_unigrams[tag] = tempcnt
		elif(tup[1] == '2-GRAM'):
			tempcnt = int(tup[0])
			tag1 = tup[2]
			tag2 = tup[3]
			if tag1+' '+tag2 in count_bigrams:
				count_bigrams[tag1+' '+tag2] = count_bigrams[tag1+' '+tag2] + tempcnt
			else:
				count_bigrams[tag1+' '+tag2] = tempcnt
		elif(tup[1] == '3-GRAM'):
			tempcnt = int(tup[0])
			tag1 = tup[2]
			tag2 = tup[3]
			tag3 = tup[4]
			if tag1+' '+tag2+' '+tag3 in count_trigrams:
				count_trigrams[tag1+' '+tag2+' '+tag3] = count_trigrams[tag1+' '+tag2+' '+tag3] + tempcnt
			else:
				count_trigrams[tag1+' '+tag2+' '+tag3] = tempcnt
		line = count_file.readline()

count()
pickle.dump([count_words, count_wordtags, count_unigrams, count_bigrams, count_trigrams], open('counts.p', 'wb'))