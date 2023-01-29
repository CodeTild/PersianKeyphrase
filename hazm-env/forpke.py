from __future__ import unicode_literals
import os
from hazm import *
import pandas as pd
tagger = POSTagger(model='resources/postagger.model')
stemmer = Stemmer()
import json
file_in_path ="filesforpketfidf" #relative path for inputfile: docs
file_out_path="inputforpketfidf" #relative path for outputfile: prepared texts for pke package
file_list = os.listdir('filesforpketfidf')
for i,doc in enumerate (file_list):
	file_in="".join([file_in_path,"/",doc])
	print(file_in)
	with open(file_in, 'r') as f:
		items = f.read()
		sent= sent_tokenize(items)
		sent_id=0
		list_sentence =[]
		list_sentence_stems =[]
		list_sentence_wps=[]
		for item in sent: 
			sent_word_token = tagger.tag(word_tokenize(item))
			stems = [stemmer.stem(word) for word, pos_tag in sent_word_token]
			list_sentence.append( sent_word_token )
			list_sentence_stems.append (stems)						
			list_sentence_wps.append ([sent_word_token,stems])
			

	#file_out="".join([file_out_path,"/file_list_sentence",str(i+1),'.txt'])
	#with open(file_out, 'w') as f: #encoding="utf-8"
	#	f.write(json.dumps(list_sentence))
	#file_out="".join([file_out_path,"/file_list_sentence_stems",str(i+1),'.txt'])
	#with open(file_out, 'w',) as f: #encoding="utf-8"
	#	f.write(json.dumps(list_sentence_stems))
	#file_out="".join([file_out_path,"/file_list_sentence_wps",str(i+1),'.txt'])
	with open(file_out, 'w',) as f: #encoding="utf-8"
		f.write(json.dumps(list_sentence_wps))
