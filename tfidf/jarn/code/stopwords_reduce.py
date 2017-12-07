#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys
import os

word_list = {}

def order_function(word_list):
	new_list = [(tfidf, word) for word, tfidf in word_list.items()]
	return sorted(new_list, key=lambda item: item[0])

for line in sys.stdin:
	word, tfidf, doc_id = line.strip().split("\t")
        
	# se a palavra não está na lista word_list, adiciona
	if word not in word_list:
		word_list[word] = tfidf
	else:
	# se o tfidf armazenado for menor que o próximo tfidf 
	# encontrado para a mesma palavra, substitui na list
		if word_list[word] > tfidf:
			word_list[word] = tfidf

stopwords = order_function(word_list)

counter = 0
for tfidf, word in stopwords:
	if counter == 30:
		break
	counter += 1
	print('{}\t{}'.format(tfidf, word))
