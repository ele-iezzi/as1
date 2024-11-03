filein = open('rosalind_subs.txt', encoding = 'UTF-8')

line = filein.read().split('\n')
dna = line[0]
sub = line[1]
l = []
out = ''
for i in range(0, len(dna)):
    if dna[i:i+len(sub)] == sub:
        l.append(i+1)
    
filein.close()
for elem in l:
    out = out + ' ' + str(elem)
print(out[1::])

