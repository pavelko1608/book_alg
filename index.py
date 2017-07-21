# coding: utf-8
# import numpy as np
# import matplotlib.pyplot as plt
# import pylab as pl
#from sklearn.cluster import KMeans


#from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from text import chapters_train
from text import set_train_index
from text import chapters_test
from text import set_test_index
from nltk.stem.snowball import SnowballStemmer
#cats = ['alt.atheism', 'sci.space', 'comp.graphics']
book_titles = ["Fear and Loathing in Las Vegas", "The Foundation"]
# newsgroups_train = fetch_20newsgroups(subset='train', categories=cats)
stemmer = SnowballStemmer("english", ignore_stopwords=True)
chapters_train = chapters_train()
# newsgroups_test = fetch_20newsgroups(subset='test', categories=cats)
chapters_test = chapters_test()
index_train = set_train_index()
index_test = set_test_index()


for chapter in chapters_train:
	chapter = chapter.decode('utf-8').split()
	for word in chapter:
		word = stemmer.stem(word)
		word = word.replace('"', '')
		word = word.replace('.', '')
		word = word.replace(',', '')
		word = word.replace('!', '')
		word = word.replace('?', '')
		word = word.replace("'", '')
	' '.join(chapter)
	
for chapter in chapters_test:
	chapter = chapter.decode('utf-8').split()
	for word in chapter:
		word = stemmer.stem(word)
		word = word.replace('"', '')
		word = word.replace('.', '')
		word = word.replace(',', '')
		word = word.replace('!', '')
		word = word.replace('?', '')
		word = word.replace("'", '')
	' '.join(chapter)






vectorizer = TfidfVectorizer()
# vectors = vectorizer.fit_transform(newsgroups_train.data)
vectors = vectorizer.fit_transform(chapters_train)
# vectors_test = vectorizer.transform(newsgroups_test.data)
vectors_test = vectorizer.transform(chapters_test)
clf = MultinomialNB(alpha=.01)
#clf.fit(vectors, newsgroups_train.target)
clf.fit(vectors, index_train)
pred = clf.predict(vectors_test)
# print metrics.f1_score(newsgroups_test.target, pred, average='macro')
print("f1_score:") 
print metrics.f1_score(index_test, pred, average='macro')
print("recall_score:") 
print metrics.recall_score(index_test, pred, average='macro')
print("precision_score:") 
print metrics.precision_score(index_test, pred, average='macro')
print("accuracy_score:") 
print metrics.accuracy_score(index_test, pred, normalize = False)


# atheism = []
# space = []
# graphics = []
HST = []
IA = []
for c, i in zip(vectors_test, pred):
    if i == 0:
        HST.append(c)
    if i == 1:
        IA.append(c)
# for a, i in zip(vectors, newsgroups_train.target):
#     if i == 0:
#         atheism.append(a)
#     if i == 1:
#         space.append(a)
#     if i == 2:
#         graphics.append(a)    
# print len(atheism)
# print len(space)
print("HST:")
print len(HST)
print("IA:")
print len(IA)
# print len(graphics)
# print len(chapters_train())
# print len(set_train_index())
# print len(chapters_test())
# print len(set_test_index())



