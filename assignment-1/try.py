import pickle

[count_words, count_wordtags, count_unigrams, count_bigrams, count_trigrams] = pickle.load(open('counts.p', 'rb'))
print(count_bigrams)