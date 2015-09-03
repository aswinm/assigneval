import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet as wn
file_list = []
st=PorterStemmer()

def cleanse(data):
    file1 = {
        'PN':[],
        'NN':[],
        'VB':[],
        'JJ':[],
    }
    s = []

    tokens = nltk.word_tokenize(data.lower())
    pos_tags = nltk.pos_tag(tokens)
    #print pos_tags
    for word in pos_tags:
        s.append(word[1])
        if word[1][:2] in ('PN','NN','VB','JJ'):
            file1[word[1][:2]].append(word[0])
    file_list.append(file1)
    return file1

def wordcompare(): 
	i,count,tc=0,0,0
	for part in file_list[0]:
		file1=file_list[0][part]
		file2=file_list[1][part]
		
		for par in file1:
			tc=tc+1
			if par in file2:
				count=count+1		

			else:
				flag = False
				for par2 in file2:
					if not flag:
						for wk in wn.synsets(par2):
                        				if par2 in wk.lemma_names():				
								count += 0.85
								flag = True
                                                                break
        print count,tc
	return float(count)/tc

	#print file1,file2		
	   

def compare_words(str1,str2):

    first=cleanse(str1)
#else:
    second=cleanse(str2)
#print second
    return wordcompare()
