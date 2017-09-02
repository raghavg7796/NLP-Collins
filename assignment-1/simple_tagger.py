import sys
import os
import pickle

[count_words, count_wordtags, count_unigrams, count_bigrams, count_trigrams] = pickle.load(open('counts.p', 'rb'))
tags = list(count_unigrams.keys())

def emission_prob(x, y):
	key = x+' '+y
	if key in count_wordtags:
		return count_wordtags[x+' '+y]/count_unigrams[y]
	else:
		return 0 

def find_tag(x):
	if(x not in count_words or count_words[x] <= 5):
		x = '_RARE_'
	ans_tag = tags[0]
	ans_prob = emission_prob(x, ans_tag)
	for tag in tags:
		prob = emission_prob(x, tag)
		if(prob >= ans_prob):
			ans_prob = prob
			ans_tag = tag
	return ans_tag

def main():
	inp = open('gene.dev', 'r')
	out = open('gene_dev.p1.out', 'w')
	line = inp.readline()
	while line:
		word = line.strip()
		if not word:
			out.write('\n')
		else:
			tag = find_tag(word.lower())
			out.write(word+' '+tag+'\n')
		line = inp.readline()
	inp.close()
	out.close()

main()
