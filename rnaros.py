filein = open('rosalind_rna.txt', encoding = 'UTF-8')

dna = filein.readline()
out = ''
for car in dna:
    if car == 'T':
        out = out + 'U'
    else:
        out = out + car

filein.close()
print(out)