word_list =[]
word_dic = dict()
with open('filename.txt', 'r',encoding="UTF-8") as f:
	lines = f.readlines();
	total_tokens =0;
	for line in lines:
		total_tokens = total_tokens+1 
		line_strip = line.strip()
		if (line_strip in word_dic):
			word_dic[line_strip]= 	word_dic[line_strip]+1;
		else:
			word_dic.update({line_strip: 1}) 
			
sorted_word_list = sorted(word_dic.items(), key=lambda x:x[1],reverse=True)
with open('wordlist.txt', 'w') as f:
	a=[" ".join([key, " ", str(value),"\n"]) for key, value in word_dic.items()]
	f.writelines(a)

with open('sortedwordlist.txt', 'w') as f:
	a=[" ".join([item[0], " ", str(item[1]),"\n"]) for item in sorted_word_list]
	f.writelines(a)
		
