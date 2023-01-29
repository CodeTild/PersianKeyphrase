from __future__ import unicode_literals
from pke import *
from pke.base import LoadFile
from pke.readers import RawTextReader,PreprocessedReader    
from pke.utils import load_document_frequency_file
from pke.utils import compute_document_frequency

import json           

#import codecs
#import xml.etree.ElementTree as etree
#from nltk.tag import str2tuple, pos_tag_sents
#from nltk.tokenize import sent_tokenize, word_tokenize
#import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

#class RawTextReader(object):
#   """ Reader for raw text. """
#    def __init__(self, path):
#        self.sentences = []
#        with codecs.open(path, 'r', 'utf-8') as f:
#            sentences = [word_tokenize(s) for s in sent_tokenize(f.read())]
#            tuples = pos_tag_sents(sentences)
#            for sentence in tuples:
#                self.sentences.append({
#                    "words" : [u[0] for u in sentence],
#                    "POS" : [u[1] for u in sentence]
#                })

#read(self, text, spacy_model=None)
#doc = RawTextReader('normalreadmesample1.txt')
#import pandas as pd

#df = pd.read_csv('SENTENCES.csv')
#sentences_dic = df.to_dict()
#for item in sentences_dic:
#	print(item)

#Now read the file back into a Python list object
with open('list_sentence_tuples.txt', 'r') as f:
    list_sentence_tuples = json.loads(f.read())
stopword = []
with open ('stopwords.txt','r') as f:
	items=f.readlines()
	for item in items:
		stopword.append(item.strip())
		#print(item)


#list_of_sentence_tuples=[]
#df2.loc["California", : ]
#with open('list_sentence_tuples.txt', 'r') as f:
#	items=f.readlines()
#	sent_id = 1
#	for item in items:
#		print(item)
		#print(list(item.strip('/n')))
#		list_of_sentence_tuples.append((sent_id,list(item.strip('/n'))))
#		sent_id = sent_id+1
#		print(sent_id)
lfile=LoadFile()
print("after load file")
lfile.load_document(list_sentence_tuples, language=None, stoplist=stopword, normalization=None, spacy_model=None)
print("after load doc")
print(lfile.stoplist)
lfile.ngram_selection(n=3)
print("after ngram_selection")
#print(lfile.sentences)
result = lfile.sentences
cands = lfile.candidates
items = cands.values
#items =lfile.get_n_best()
lfile.candidate_filtering()
cands2 = lfile.candidates	
#doc = PreprocessedReader()
#result = doc.read(list_sentence_tuples)
for item in result:
	print (item.words)
	print(item.pos)
	print(item.stems)
	#print(item.meta)
	
#print(cands)
#for item in cands.values():
#	print(item)
#	print (item.surface_forms)
#	print(item.sentence_ids)
#	print(item.pos_patterns)
#	print(item.lexical_form)

#for item in cands2.values():
#	print(item)
#	print (item.surface_forms)
#	print(item.sentence_ids)
#	print(item.pos_patterns)
#	print(item.lexical_form)
doc_list =[]
doc_list.append(list_sentence_tuples)
doc_list.append(list_sentence_tuples)
	
compute_document_frequency(doc_list,
                               'df_sample.tsv.gz',
                               language=None,
                               stoplist=stopword,
                               normalization=None,
                               delimiter='\t',
                               # TODO: What is the use case for changing this ?
                               n=3)
                               
df= load_document_frequency_file('df_sample.tsv.gz')	
#lfile.candidate_weighting(df)
	
