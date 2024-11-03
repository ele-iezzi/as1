filein = open('rosalind_hamm.txt', encoding = 'UTF-8')

line = filein.read().split('\n')
dna1 = line[0]
dna2 = line[1]
count = 0
for i in range(0, len(dna1)):
    if dna1[i] != dna2[i]:
        count = count +1
    
filein.close()
print(count)
