import os
import sys
import pickle

[count_words, count_wordtags, count_unigrams, count_bigrams, count_trigrams] = pickle.load(open('counts.p', 'rb'))
tags = list(count_unigrams.keys())
sentence = input().strip().split()
dp = dict()
bt = dict()
ans_tags = []

def qparam(tag1, tag2, tag3):
	return count_trigrams[tag1+' '+tag2+' '+tag3]/count_bigrams[tag1+' '+tag2]

def emiss(x, y):
	if(x not in count_words or count_words[x] <= 5):
		x = '_RARE_'
	key = x+' '+y
	if key in count_wordtags:
		return count_wordtags[x+' '+y]/count_unigrams[y]
	else:
		return 0 
def calc(x, tag1, tag2):
	if(x == 0):
		return 1
	if(x == 1):
		return qparam('*', '*', tag2) *  emiss(sentence[x-1], tag2)
	if(str(x)+' '+tag1+' '+tag2 in dp):
		return dp[str(x)+' '+tag1+' '+tag2]
	ans_prob = 0
	ans_tag = '_RARE_'
	for tag in tags:
		temp_prob = calc(x-1, tag, tag1) * qparam(tag, tag1, tag2) * emiss(sentence[x-1], tag2)
		if(temp_prob > ans_prob):
			ans_prob = temp_prob
			ans_tag = tag
	dp[str(x)+' '+tag1+' '+tag2] = ans_prob
	bt[str(x)+' '+tag1+' '+tag2] = str(x-1)+' '+ans_tag+' '+tag1 
	return dp[str(x)+' '+tag1+' '+tag2]

def print_ans(x, tag1, tag2):
	global ans_tags
	if(x == '2'):
		ans_tags = [tag1, tag2] + ans_tags
		return
	else:
		ans_tags = [tag2] + ans_tags
		[x_, tag1_, tag2_] = bt[x+' '+tag1+' '+tag2].split()
		print_ans(x_, tag1_, tag2_)

def main():
	x = len(sentence)
	ans_prob = 0
	ans_tag1 = '_RARE_'
	ans_tag2 = '_RARE_'
	for tag1 in tags:
		for tag2 in tags:
			temp_prob = calc(x, tag1, tag2)
			if(temp_prob > ans_prob):
				ans_prob = temp_prob
				ans_tag1 = tag1
				ans_tag2 = tag2
	print_ans(str(x), ans_tag1, ans_tag2)

main()
print(ans_tags)
