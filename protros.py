filein = open('rosalind_prot.txt', encoding = 'UTF-8')

convert = open('rna_codon_table.txt', encoding = 'UTF-8')
line = filein.read().replace('\n','')
tab = convert.read()
out = ''
for i in range(0, len(line)-2, 3):
    string = line[i:i+3]
    index = tab.find(string)
    if tab[index+4:index + 8] == 'Stop':
        break
    out = out + str(tab[index + 4])

filein.close()
convert.close()
print(out)
