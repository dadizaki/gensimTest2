import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim.summarization import summarize
from gensim.summarization import keywords


f = open("biz_all", "r")
lines = f.readlines()
for line in lines:
    print("text is: ", line)
    print('Keywords:', keywords(line, ratio=0.5))
f.close()