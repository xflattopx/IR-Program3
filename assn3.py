import re

# Build an object class
class Document:
    def __init__(self):
        author    = ''
        title     = ''
        body_text = ''

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
def get_raw_text(filename):
 
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
    
def getArticleInformation(text):
    re_entry = re.compile("^(\.I )\d+")
