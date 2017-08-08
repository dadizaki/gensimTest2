file = open("new_biz_meaningless")
fo = open("processed_meaningless.txt", "w")

while True:
    line = file.readline()
    if not line:
        break
    fo.write("\"")
    fo.write(line.strip('\n'))
    fo.write("\",\n")  # do something

file.close()
fo.close()

