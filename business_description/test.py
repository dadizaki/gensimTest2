raw_corpus_meaningful = []
f = open("new19", "r")
lines = f.readlines()
for line in lines:
    raw_corpus_meaningful.append(line.strip('\n'))

print(raw_corpus_meaningful)