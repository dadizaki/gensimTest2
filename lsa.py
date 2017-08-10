import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities

raw_corpus_meaningful = []
f = open("new_biz_meaningful", "r")
lines = f.readlines()
for line in lines:
    raw_corpus_meaningful.append(line.strip('\n'))
f.close()

raw_corpus_meaningless = []
f = open("new_biz_meaningless", "r")
lines = f.readlines()
for line in lines:
    raw_corpus_meaningless.append(line.strip('\n'))
f.close()

raw_corpus = raw_corpus_meaningful + raw_corpus_meaningless

# Create a set of frequent words and add stopwords
stoplist = set('for a an of the and to in test from this that test'.split(' '))
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

dictionary = corpora.Dictionary(processed_corpus)
dictionary.save('/biz.dict')
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/biz.mm', corpus)

dictionary = corpora.Dictionary.load('/biz.dict')
corpus = corpora.MmCorpus('/biz.mm')  # comes from the first tutorial, "From strings to vectors"
print(corpus)

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=10)
index = similarities.MatrixSimilarity(lsi[corpus])
index.save('/biz.index')
index = similarities.MatrixSimilarity.load('/biz.index')

doc = []
f = open("new19", "r")
lines = f.readlines()
for line in lines:
    doc.append(line.strip('\n'))
f.close()

file = open("S2000_T200_topic200.txt", "w")
flag = "meaning"
for dd in doc:
    vec_bow = dictionary.doc2bow(dd.lower().split())
    vec_lsi = lsi[vec_bow]  # convert the query to LSI space
    # print(vec_lsi)
    # Performing queries

    sims = index[vec_lsi]  # perform a similarity query against the corpus
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    if raw_corpus[sims[0][0]] in raw_corpus_meaningless:
        flag = "meaningless"
        print("meaningless")
    elif sims[0][1] == 0.0:
        flag = "meaningless"
        print("meaningless")
    else:
        flag = "meaningful"
        print("meaningful")
    # print(sims[0], sims[1])
    # print("origin: %s" % dd)
    # print("first: %s" %raw_corpus[sims[0][0]])
    # print("similarity: %f" %sims[0][1])  # print sorted (document number, similarity score) 2-tuples
    # print("second: %s" % raw_corpus[sims[1][0]])
    # print("similarity: %f" % sims[1][1])
    file.write("\r\n")
    file.write("origin: %s\r\n" % dd)
    file.write(flag)
    file.write("first: %s\r\n" % raw_corpus[sims[0][0]])
    file.write("similarity: %.4f\r\n" % sims[0][1])  # print sorted (document number, similarity score) 2-tuples
    file.write("second: %s\r\n" % raw_corpus[sims[1][0]])
    file.write("similarity: %.4f\r\n" % sims[1][1])
file.close()


# print(list(enumerate(sims))) # print (document_number, document_similarity) 2-tuples
