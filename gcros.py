filein = open('rosalind_gc.txt', encoding = 'UTF-8')

line = filein.read().replace('\n', '').split('>')
max = 0
for i in range(1, len(line)): 
    string = line[i]
    ID = string[0:13]
    dna = string[13:len(string)]
    numC = dna.count('C')
    numG = dna.count('G')
    perc = (numC + numG)*100 / len(dna)
    if perc >= max:
        max = perc
        out = str(ID) + '\n' + str(perc)

filein.close()
print(out)
