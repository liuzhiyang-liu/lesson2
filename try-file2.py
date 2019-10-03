filename = 'test.txt'
f = open(filename, 'r')

texts=f.read()
print(texts)

f.close()
