import re

# Build an object class
class Document:
    def __init__(self):
        self.author    = ''
        self.title     = ''
        self.body_text = ''
        self.number = -1

    # Creates document object
    @staticmethod
    def buildDocument(initAuth, initTitle, initBody, num):
        d = Document()
        d.author    = initAuth
        d.title     = initTitle
        d.body_text = initBody
        d.number    = num
        return d

#END CLASS

class Index:
    def __init__(self):
        self.tier1 = {}
        self.tier2 = {}
        self.numDouments = -1
        
    def __str__(self):
        return 'Index'
    
    @staticmethod
    def createIndex():
        index = Index()
        index.numDocuments = 0
        return index
	
    #adds all terms in list of documents docList to the index self
    def populateIndex(self, docList):
        for doc in docList:
            print(self.numDocuments)
            self.updateIndex(self.tier1, doc.title, doc.number)
            self.updateIndex(self.tier2, doc.body_text, doc.number)
            self.numDocments += 1
			
    #adds all terms in string content to tier tier of index self
    def updateIndex(self, tier, content, docID):
        wordList = content.split()
        for word in wordList:
            token = tokenize(word)
            print('curToken: ' + token)
            if token in tier:
                termList = tier[token][0]
                #print('type termList: ' + type(termList))
                lastDocTuple = termList.getLast()
                if(lastDocTup[0] == docID):
                    termList.incLastTF()
                else:
                    termList.addDoc(docID)
            else:
                print('token added: ' + token)
                #print('in else type termList: ' + str(type(tier[token])))
                tier[token] = TermList.buildTermList(token, docID)
                
				
		
#END CLASS

class TermList:
    def __init__(self):
        self.termStr = ''
        self.documentFrequency = -1
        self.docList = [] #list of tuples of the form (docID, term frequency)
	
    def __str__(self):
        return 'TermList'
    
    def __repr__(self):
        return 'TermList'
        
    @staticmethod
    def buildTermList(t, docID):
        term = TermList()
        term.termStr = t
        term.documentFrequency = 1
        term.docList.append((docID, 1))
        
    def getLast(self):
        return self.docList[len(self.docList) - 1]
    
    def incLastTF(self):
        last = self.getLast()
        self.docList[len(self.docList) - 1] = (last[0], last[1] + 1)
        
    def addDoc(self, docID):
        self.docList.append((docID, 1))
        
    def incDocFreq(self):
        self.documentFrequency += 1
	

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
    #w = porter.stem(w)
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
    #corpus split on entries
    re_entry = re.compile("\.I ")
    docs = re.split(re_entry, corpus)

    #print(docs[1])
    #print(len(docs))

    # for some reason the first entry is originally blank.
    # this fucks everything up so we have to make it die.
    del(docs[0])
    #getArticleInformation(docs[0])

    for entry in docs:
        docList.append(getArticleInformation(entry))

    #print("returning doclist")
    return docList


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
    doc_buster = re.compile("\.[A-Z]\n")
    doc_attributes = re.split(doc_buster, unprocessedDocs)

    # build a document using the relevant information and return it
    return Document.buildDocument(doc_attributes[2],doc_attributes[1],doc_attributes[4],doc_attributes[0])


''' MAIN '''
theFile = getRawText('corpus/cran.all.1400')
docList = parseCorpus(theFile)

'''
doc1 = doclist[0]
print(doc1.author)
print(doc1.title)
print(doc1.body_text)
print(doc1.number)
'''


index = Index.createIndex()
dls = docList[0:2]
index.populateIndex(dls)

print(index.tier1['the'].docList)
