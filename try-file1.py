filename = 'test.txt'
f = open(filename, 'w')

for i in range(1,6):
    data = 'Row no(%d) --- hello world\n' % i
    f.write(data)


f.close()
