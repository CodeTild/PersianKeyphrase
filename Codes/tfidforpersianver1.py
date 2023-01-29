#import pke
from pke import *
from pke.base import LoadFile
from pke.readers import RawTextReader,PreprocessedReader    
from pke.utils import load_document_frequency_file
from pke.utils import compute_document_frequency
import json           
import os




file_in_path ="inputs" #relative path for inputfile: docs
file_list = os.listdir(file_in_path)
doc_info=[]
total_doc_list = []
#doc_len_list = []
for i,doc in enumerate (file_list):
	file_in="".join([file_in_path,"/",doc])
	with open(file_in, 'r') as f:
    		doc_name=doc.replace('.txt','')
    		doc_info.append(doc_name)
    		doc_name= json.loads(f.read())
    		total_doc_list.append(doc_name)     		
    		


stopword = []
with open ('stopwords.txt','r', encoding='utf-8') as f:
	items=f.readlines()
	for item in items:
		stopword.append(item.strip())

	
compute_document_frequency(total_doc_list,
                               'df_sample.tsv.gz',
                               language=None,
                               stoplist=stopword,
                               normalization=None,
                               delimiter='\t',
                               # TODO: What is the use case for changing this ?
                               n=3)

extractor = pke.unsupervised.TfIdf()
bias =0
for i,doc in  enumerate(total_doc_list):
	extractor.load_document(doc, language=None, stoplist=stopword, normalization=None, spacy_model=None)
	extractor.candidate_selection(n=3)
	df= load_document_frequency_file('df_sample.tsv.gz')
	extractor.candidate_weighting(df=df)
	keyphrases = extractor.get_n_best(n=10)
	name=doc_info[i]
	print(" key pharses for ", name )
	print (keyphrases)	
