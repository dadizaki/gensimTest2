# https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/gensim%20Quick%20Start.ipynb
import logging
logging.basicConfig(format='%(asctime)s: %(levelname)s : %(message)s', level = logging.INFO)
# corpus

raw_corpus = []
f = open("corpus_filter.txt", "r")
lines = f.readlines()
for line in lines:
    raw_corpus.append(line.strip('\n'))
f.close()

# Create a set of frequent words and add stopwords
stoplist = set('for a an of the and to in test from this that'.split(' '))
# Lowercase each document, split it by white space and filter resource stopwords
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in raw_corpus]

# Count word frequencies
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

# Only keep words that appear more than once
processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]
# print(processed_corpus)

from gensim import corpora

dictionary = corpora.Dictionary(processed_corpus)
# print(dictionary)

# vector
# print(dictionary.token2id)

# new_doc = "Human computer interaction"
# new_vec = dictionary.doc2bow(new_doc.lower().split())
# print(new_vec)

bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]
# print(bow_corpus)

from gensim import models
# train the model
tfidf = models.TfidfModel(bow_corpus)
# transform the "system minors" string
testset = []
f = open("biz_all", "r")
lines = f.readlines()
for line in lines:
    testset.append(line.strip('\n'))
f.close()

f = open("all-tfidf.txt", "w")
for str in testset:
    t = tfidf[dictionary.doc2bow(str.lower().split())]
    f.write(str)
    print(t)
    if (t == []):
        f.write("\r\nScore : %d\r\n" %0)
    else:
        count = 0
        sum = 0
        for item in t:
            count += 1
            sum += item[1]
        # res = sum/count
        res = sum
        f.write("\r\nScore : %f\r\n" % res)
f.close()