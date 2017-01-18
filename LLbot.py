#!/usr/bin/python
# This Python file uses the following encoding: utf-8

import nltk, sys, os
from textblob import TextBlob
from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist
from textblob import Word
import csv

###PATH to your file - make sure you update it
nltkfile = nltk.corpus.PlaintextCorpusReader(r'C:\Users\You\Documents', 'myfile.txt')
corpus  = nltk.Text(nltkfile.words())
text = nltk.Text(corpus)

#opening file for TextBlob
file = open(r'C:\Users\You\Documents\myfile.txt')
tblobread = file.read()
corpusblob = TextBlob(tblobread)

###Tagged file - use for Part of Speech tagging is needed
tagged = nltk.pos_tag(corpus)

###stopwords
stopwords = nltk.corpus.stopwords.words('english')
mystopwords = ['.', ',','\'', '!', '...', '--', '-', '?', ';', '#', '$', 'i', 'i\'ll', 'i\'d','that\'s','could','would','there\'s','don''t','can\'t','you\'ll','i\'m', 'i\'ve','you\'ve','we\'re','you\'re','no', 'yes', 'the', 'you', 'me', 'he', 'she', 'it', 'that','we','(',')','s','t','a']
fullstop = stopwords + mystopwords
spellchars = "[('.', )qwertyuiopasdfghjklzxcvbnm!@#$%^&*()--+={}\|;:]"

###ignore list location (used for spellchecker)
ignorelist = open(r'C:\Users\You\Documents\ignorelist.txt').read()

#allWords = nltk.word_tokenize(corpus)
allWordDist = nltk.FreqDist(w.lower() for w in text)
allWordExceptStopDist = nltk.FreqDist(w.lower() for w in text if w not in fullstop)
mostCommon = allWordExceptStopDist.most_common(50) # this didn't word - trying mostcommon2 and mostcommon3 below
mostcommon2 = nltk.FreqDist(i for i in corpusblob.lower().split() if i not in fullstop)
mostcommon3 = mostcommon2.most_common(50)

###Frequency distribution
fdistcorpus = FreqDist(corpus)

###Functions start here

#finding number of words by lenght in corpus
def fdistlen():
    fdistlen = FreqDist([len(w) for w in corpus])
    print ("Number of words by Length (length, number of words) =", fdistlen.items())

#less frequent words
def findhapaxes():
    fdist = fdistcorpus.hapaxes()
    print ("50 least common words =", fdist[:50])

#hapaxes + definition (for terms not in stopwords and longer than 3 chars.)
def hapaxdef():
    fdist = fdistcorpus.hapaxes()
    print('Least common words defined:')
    for a in fdist[:20]:
        if len(a) > 3:
            if not a in stopwords:
                print(a,": ",Word(a).definitions)

#spell and print <1, >0 using ignore list
def spell():
    for term in fdist:
        typo = Word(term.lower())
        typostr = str(typo.spellcheck())
        if not '1.0' in typostr:
            if not term in ignorelist:
                print(term, ': ', typostr)

#longest sentence - uses goslate, reads first sentence
def __longestsent__():
    maxlen = max(len(sent) for sent in corpusblob.sentences)
    print('Longest sentence: ', [sent for sent in corpusblob.sentences if len(sent) == maxlen], 'chars: ', maxlen)
    
#average sentence length
def __averagesentlen__():
    avlen = sum(len(sent) for sent in nltkfile.sents()) / len(nltkfile.sents())
    print('Average sentence length :', avlen)

#used to find frequency by part of speech
def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                  if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())

tagdictNN = findtags('NN', tagged)
tagdictJJ = findtags('JJ', tagged)

#recurring NNs
def findNN():
    for tag in sorted(tagdictNN):
        print('Frequent',tag,':', tagdictNN[tag])

#recurring adjectives
def findJJ():
    for tag in sorted(tagdictJJ):
        print('Frequent', tag,':', tagdictJJ[tag])

#DICTIONARY matches, reads CSV file in C:, show if word in txt + translation
def glossarymatch():
    count = 0
    with open(r'C:\glossary.csv', mode='r') as infile:
        reader = csv.reader(infile)
        with open(r'C:\glossary_new.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            mydict = {rows[0]:rows[1] for rows in reader}
            for word in sorted(corpusblob.words):
                if word in mydict:
                    count = count + 1
                    print(word, 'is in glossary as:',mydict[word])
    print('Glossary matches found:', count)
                    


###print report
print("This is your report:\n\n")
print ('***Counts***')
print ("Number of sentences =", len(nltkfile.sents()))
print ("-----------------------------------------")
print ("Number of paragraphs =", len(nltkfile.paras()))
print ("-----------------------------------------")
print ("Number of characters =", len([char for sentence in nltkfile.sents() for word in sentence for char in word]))
print ("-----------------------------------------")
print ("Number of tokens =", len([word for sentence in nltkfile.sents() for word in sentence]))
print ("-----------------------------------------")
print ("Number of Unique Words =", len(set(corpus)))
print ("-----------------------------------------")
print ("Wordcount =",len([word for sentence in nltkfile.sents() for word in sentence if word.isalpha()]))
print ("-----------------------------------------")
fdistlen()
print ("-----------------------------------------")
__longestsent__()
print ("-----------------------------------------")
__averagesentlen__()
print ("-----------------------------------------")
print ("-----------------------------------------")
print ('***Lexical Information***')
print ("Lexical richness =", len([word for sentence in nltkfile.sents() for word in sentence])/len(set(corpus)))
print ("-----------------------------------------")
print ("Frequent collocations = ")
print(corpus.collocations(50))
print ("-----------------------------------------")
print('***Frequencies***')
print ("Most common words =", mostcommon3)
print ("-----------------------------------------")
findhapaxes()
print ("-----------------------------------------")
findNN()
print ("-----------------------------------------")
findJJ()
print ("-----------------------------------------")
print ("-----------------------------------------")
print('***Glossaries and Dictionaries***')
glossarymatch()
print ("-----------------------------------------")
hapaxdef()
#print ("-----------------------------------------")
#print ("-----------------------------------------")
#print ('***Spelling***')
#print("Potential mispellings (suggestions + confidence)")
#spell()
