import re

# Build an object class
class Document:
    def __init__(self):
        author    = ''
        title     = ''
        body_text = ''
        number = -1

    # Creates document object
    @staticmethod
    def buildDocument(initAuth, initTitle, initBody, num):
        d = Document()
        d.author    = initAuth
        d.title     = initTitle
        d.body_text = initBody
        d.number    = num
        return d

# Build the inverted index

#toknizeWordList(line) tokenizes a string of words. 
#line is the string to tokenize.
#returns list of tokenized words.
def tokenizeWordList(line):
    wordlist = []
    
    for token in line.split():
        wordlist.extend(token.replace('--', '-').split('-'))
    
    i = 0
    while(i < len(wordlist)):
        
        wordlist[i] = tokenize(wordlist[i])
        i = i + 1
    
    return wordlist
    
#tokenize(word) tokenizes a string. 
#word is the string to tokenize.
def tokenize(word):
    regex = re.compile('[^a-zA-Z]+')
    w = regex.sub('', word)
    w = w.lower()
    w = porter.stem(w)
    return w

# extract the raw text from a file
#
def getRawText(filename):
    f = open(filename, 'r')
    fileText = f.read()
    return fileText


def parseCorpus(corpus):
    docList = []
    dracula = -1
    docs = []
    print('i\'m alive!')
    #corpus split on entries
    re_entry = re.compile("\.I ")
    docs = re.split(re_entry, corpus)

    #print(docs[1])
    #print(len(docs))

    for entry in docs:
        docList.append(getArticleInformation(entry))


'''   
#giveWordList(filename) converts a file called filename
#to a list of words breaking the string the same way
#as tokenizeWordList. returns a list of words.
def giveWordList(filename):
    f = open(filename, 'r')
    words = []
    for line in f:
        for token in line.split():
            words.extend(token.replace('--', '-').split('-'))
    return words
'''
    
def getArticleInformation(unprocessedDocs):
    #print(type(unprocessedDocs))
    doc_buster = re.compile("\.[A-Z]")
    doc_attributes = re.split(doc_buster, unprocessedDocs)
    for x in doc_attributes:
        print (x)

''' MAIN '''
theFile = getRawText('cran.all.1400')
parseCorpus(theFile)
