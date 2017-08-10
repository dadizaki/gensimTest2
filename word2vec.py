# import modules & set up logging
import os
import numpy as np
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# sentences = gensim.models.word2vec.LineSentence('new_biz')
# more_sentences = gensim.models.word2vec.LineSentence('biz_all')
# model = gensim.models.Word2Vec(sentences)
# model.save("w2vmodel")
# model = gensim.models.Word2Vec.load("w2vmodel")
# model.train(more_sentences)

documents = ["Human machine interface for lab abc computer applications",
              "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
              "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]

model=gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300-SLIM.bin.gz', binary=True)
print("The most similar words with accounts: \n", model.wv.most_similar('account'))
model.score(["The fox jumped over a lazy dog".split()])

# stoplist = set('for a of the and to in'.split())
# texts = [[word for word in document.lower().split() if word not in stoplist]
#          for document in documents]
# from collections import defaultdict
# frequency = defaultdict(int)
# for text in texts:
#     for token in text:
#         frequency[token] += 1
# texts = [[token for token in text if frequency[token] > 1]
#          for text in texts]
# from pprint import pprint  # pretty-printer
# pprint(texts)

