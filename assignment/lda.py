import nltk
#from nltk.stem import PorterStemmer
from nltk.corpus import wordnet as wn
#file_list = []
#st=PorterStemmer()
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

def ldamax(para1,para2):
	a=para1
	a=nltk.word_tokenize(a.lower())
	pos_tags=nltk.pos_tag(a)
	dic={}
	for word in pos_tags:
     		if word[1][:2] in ('PN','NN','VB','JJ'):
             		if word[0] not in dic.keys():		
		     		b=[]
                     		for keys in dic.keys():
                             		for wk in wn.synsets(keys):
                                     		for k in wk.lemma_names():
                                           		b.append(k)  
	             		if word[0] in b:
                    	     		dic[keys].append(word[0])
             	     		else:       
                    	     		dic[word[0]]=[]
	
	a=para2
	a=nltk.word_tokenize(a.lower())
	pos_tags=nltk.pos_tag(a)
	for word in pos_tags:
     		if word[1][:2] in ('PN','NN','VB','JJ'):
             		if word[0] not in dic.keys():		
		     		b=[]
                     		for keys in dic.keys():
                             		for wk in wn.synsets(keys):
                                     		for k in wk.lemma_names():
                                           		b.append(k)  
	             		if word[0] in b:
                    	     		dic[keys].append(word[0])
             	     		else:       
                    	     		dic[word[0]]=[]
	
	final={"data1":para1,"data2":para2,"score":'0.0'}
	para1=sent_detector.tokenize(para1.strip()) #sentence tagging using nltk sentence segmentation
	para2=sent_detector.tokenize(para2.strip()) #sentence tagging using nltk sentence segmentation
	#print para1,'\n',para2	
	dic1,dic2={},{} #dictionary 1 and 2 contains sentences with their ID's
	#st=LancasterStemmer()
	n=0 # iterator for sentences in para1
	for i in para1:
		i=nltk.word_tokenize(i.lower()) # tokenizing the sentence
		i=nltk.pos_tag(i) # parts of speech tagging the sentence
		para1[n]=i # sentence with pos tag is saved
		dic1[n+1]=list() # dictionary 1[n+1] contains only the nouns and verbs and adjectives
		for word in i:
			#print word
			if word[1][:2] in ('PN','NN','VB','JJ'): # will save only the words with these tags in a sentence 
				dic1[n+1].append(word[0]) # appended to dic1's sentence id
				#print dic1[n]
		n=n+1
	#print dic1
	n=0  # iterator for sentences in para2
        for i in para2:
                i=nltk.word_tokenize(i.lower())  # tokenizing the sentence
                i=nltk.pos_tag(i) # parts of speech tagging the sentence
                para2[n]=i # sentence with pos tag is saved
                dic2[n+1]=list() # dictionary 2[n+1] contains only the nouns and verbs and adjectives
                for word in i:
                        #print word
                        if word[1][:2] in ('PN','NN','VB','JJ'):  # will save only the words with these tags in a sentence
                                dic2[n+1].append(word[0]) # appended to dic2's sentence id
                                #print dic1[n]
                n=n+1

	l1=len(dic1)       		
	l2=len(dic2)
	count,c=0,0 
	sco={'PN':1,'VB':0.90,'NN':0.95,'JJ':0.95} #scores for each POS
	#print file_list
	b=list() #contains all synsets of single words
	maxscore=list() #contains maxScore for each sentence
	sentencescore=list() #contains max of sentence[i] similarity with dic1
	countscore=[[]] # contains sentence wise dic1 count scores
	for keyi,i in dic2.iteritems(): # i-> every sent. in dic2
		#print keyi
		if i in dic1.values():
			sentencescore.append(1) # exact match condition
		else:
			maxscore.append(0) #maxscore of each sentence i is initialised to 0
			countscore.append([]) #countscore of each sent. i is initialsed to an empty list
			for w in i: # every word in sentence i
                		for wk in wn.synsets(w): # wordnet synset obj
                        		for k in wk.lemma_names(): #getting the strings alone 
                                		b.append(k) # appends to list b'''
                        	x=nltk.pos_tag(nltk.word_tokenize(w)) #POS tagging after tokenizing
                        	t=x[0][1][:2] #POS generalization ex: VBZ -> VB
                        	if t in sco: 
                        		maxscore[keyi-1]=maxscore[keyi-1]+sco[t] #maxscore is updated with the corresponding score for w
			#print keyi,maxscore[keyi-1]
			for keyj,j in dic1.iteritems(): # j-> every sentences in dic1
				for w in i: # every words in dic2
					for wk in wn.synsets(w):  # wordnet synset obj
						for k in wk.lemma_names(): #getting the strings alone 
							b.append(k) # appends to list b'''
					x=nltk.pos_tag(nltk.word_tokenize(w)) #POS tagging after tokenizing
					t=x[0][1][:2] #POS generalization ex: VBZ->VB
					if t in sco:
						#maxscore[keyi-1]=maxscore[keyi-1]+sco[t]
						for v in j: # every word in j
							if v in b or v==w: # either v exactly matches with w or it is present in synsets(w)
								count=count+sco[t] #increase score for that sentence j
					b=[] # clear b for next word w
				#print maxscore[keyi-1] 
				countscore[keyi-1].append(count) # append sentence score count -> similarity[keyi][keyj] 
				count=0 # clear count for next sentence j
			#print countscore[keyi-1]
			#for keyi,i in dic2.iteritems():
			if max(countscore[keyi-1])!=0 and maxscore[keyi-1]!=0: 
				# division by zero error check and if countscore is zero, don't append
				#print max(countscore[keyi-1]),maxscore[keyi-1],i
				sentencescore.append(max(countscore[keyi-1])/maxscore[keyi-1]) 
				# assign sentence i with a final sentence score by taking max(countscore[keyi-1])
				# and divide by maxscore calculated before for sentence i'''
	#print sentencescore
	#p1=infile1.read()
	#p2=infile2.read()
	#final={"data1":p1,"data2":p2,"score":'0.0'}
	if len(sentencescore)==0: # division by zero error check or no similarity
		return 0 # print default final
	else: # every other case
		fin=sum(sentencescore)/len(sentencescore)
		if fin>1:
			final['score']=1.0
		else:
			final["score"]=fin #set final score as sum of sentence scores / length of sentences
		return final["score"] # print the updated final




"""path1=raw_input("Text 1 (filename ): ")
path2=raw_input(" Text 2 (filename): ")
str1=open(path1,'r').read().split()
str2=open(path2,'r').read().split()"""
#cleanse(path1)
def sentence_comparison(str1,str2):
    if len(str1) >= len(str2):
	return ldamax(str1,str2)
    else:
	return ldamax(str2,str1)
