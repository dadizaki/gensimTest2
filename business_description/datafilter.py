f = open("corpus.txt", "r",encoding="utf8")
file = open("corpus_filter.txt", "w",encoding="utf8")
lines = f.readlines()
for line in lines:
    if (len(line.split()) < 5):
        continue
    elif (line[0:7] == "Mobile:" or line[0:7] == "Office:"):
        continue
    else:
        file.write(line)
f.close()
file.close()
