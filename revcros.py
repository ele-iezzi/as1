filein = open('rosalind_revc.txt', encoding = 'UTF-8')

dna = filein.readline()
out = ''
for car in dna:
    if car == 'T':
        out ='A' + out
    elif car == 'A':
        out ='T' + out
    elif car == 'C':
        out ='G' + out
    elif car == 'G':
        out ='C' + out

filein.close()
print(out)
