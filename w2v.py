import gensim, logging
import pandas as pd
import numpy as np
from collections import Counter
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = []
f = open("corpus_filter.txt", "r")
lines = f.readlines()
for line in lines:
    sentences.append(line.strip('\n'))
f.close()

# word2vec = gensim.models.word2vec.Word2Vec(sentences, size=256, window=10, min_count=64, sg=1, hs=1, iter=10)
word2vec = gensim.models.word2vec.Word2Vec(sentences, size=100, min_count=1, hs=1, negative = 0)
word2vec.save('word2vec_wx')
model = gensim.models.Word2Vec.load('word2vec_wx')


def predict_proba(oword, iword):
    iword_vec = model[iword]
    oword = model.wv.vocab[oword]
    oword_l = model.syn1[oword.point].T
    dot = np.dot(iword_vec, oword_l)
    lprob = -sum(np.logaddexp(0, -dot) + oword.code*dot)
    return lprob

def keywords(s):
    s = [w for w in s if w in model]
    ws = {w:sum([predict_proba(u, w) for u in s]) for w in s}
    return Counter(ws).most_common()



file = open("all-w2v.txt", "w")
f = open("biz_all", "r")
lines = f.readlines()
for line in lines:
    sentences.append(line.strip('\n'))
    file.write(line)
    file.write("similarity: \r\n")
    print(line)
    print("\r\n")
    print(pd.Series(keywords(line.split())))
    # file.write(str(keywords(line.strip('\n').split())))
f.close()
file.close()