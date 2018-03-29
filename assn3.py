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

#END CLASS

class Index:
	def __init__(self):
		tier1 = {}
		tier2 = {}
		numDouments = -1
	@staticmethod
	def creatIndex():
		index = Index()
		index.uments = 0
		return Index
	
	#adds all terms in list of documents docList to the index self
	def populateIndex(self, docList):
		for doc in docList:
			self.updateIndex(self.tier1, doc.title)
			self.updateIndex(self.tier2, doc.body_text)
			self.numDocments += 1
			
	#adds all terms in string content to tier tier of index self
	def updateIndex(self, tier, content):
		termList = content.split()
		for word in termList:
			token = tokenize(word)
			if token in tier:
				
				
		
#END CLASS

class TermList:
	def __init__(self):
		termStr = ''
		documentFrequency = -1
		docList = [] #list of tuples of the form (docID, term frequency)
		
	@staticmethod
	def buildTerm(t):
		term = TermList()
		term.termStr = t
		documentFrequency = 1
        
#END CLASS

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

    print("returning doclist")
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
theFile = getRawText('cran.all.1400')
theImportantDoclist = parseCorpus(theFile)

doc1 = theImportantDoclist[0]
print(doc1.author)
print(doc1.title)
print(doc1.body_text)
print(doc1.number)

print("testing body text")
print(doc1.body_text[1])
