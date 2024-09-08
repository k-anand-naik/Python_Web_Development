f = open('read_text_file.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)