import nltk

file_list = []

def get_magnitude(vector):
    mag = 0
    for i in vector:
        mag += i*i
    return mag**0.5

def get_scalar_product(vector1,vector2):
    length = len(vector1)
    i = 0
    prod = 0
    while i<length:
        prod += vector1[i]*vector2[i]
        i += 1
    return prod


def get_word_count(text):
    words = {}
    for i in text.split():
        words[i] = words.get(i,0)+1
    return words

def check_plagiarism(text1,text2):
    list1 = get_word_count(text1)
    list2 = get_word_count(text2)
    list2_copy = dict(list2)
    vector_1 = []
    vector_2 = []
    for word in list1:
        if word in list2:
            vector_1.append(list1[word])
            vector_2.append(list2[word])
            del list2[word]
        else:
            vector_1.append(list1[word])
            vector_2.append(0)
    for word in list2:
        vector_1.append(0)
        vector_2.append(list2[word])
    scalar = get_scalar_product(vector_1,vector_2)
    mag1 = get_magnitude(vector_1)
    mag2 = get_magnitude(vector_2)
    similarity = scalar/(mag1*mag2)
    print "COSINE SIMILARITY: " + str(similarity)
    return similarity>0.89



def cleanse(path):
    file1 = {
        'PN':[],
        'NN':[],
        'VB':[],
        'JJ':[],
    }
    s = []

    infile = open(path,'r')
    data = infile.read()
    tokens = nltk.word_tokenize(data.lower())
    pos_tags = nltk.pos_tag(tokens)
    for word in pos_tags:
        s.append(word[1])
        if word[1][:2] in ('PN','NN','VB','JJ'):
            file1[word[1][:2]].append(word[0])
    file_list.append(file1)


#print "Ente r the path to the first file"
"""print "Enter the path to the first file"
path1 = raw_input()

print "Enter the path to the second file"
path2 = raw_input()


 
if check_plagiarism(path1,path2):
	print "PLAGIARISM FOUND!!!"
else:
	cleanse(path1)
	cleanse(path2)
        print file_list"""


