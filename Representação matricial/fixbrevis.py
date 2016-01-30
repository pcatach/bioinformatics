file=open("brevis.txt")
one=''
for line in file:
    one+=line[:-1]
file.close()

file2=open("Bbrevis.txt", 'w')
file2.write(one)
file2.close()
