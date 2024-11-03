filein = open('rosalind_dna.txt', encoding = 'UTF-8')

dna = filein.readline()
numA = dna.count('A')
numC = dna.count('C')
numG = dna.count('G')
numT = dna.count('T')
out = str(numA) + ' ' + str(numC) + ' ' + str(numG) + ' ' + str(numT)

filein.close()
print(out)
