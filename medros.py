filein = open('rosalind_med.txt', encoding = 'UTF-8')

n = int(filein.readline())
A = filein.readline().replace('\n','').split(' ')
k = int(filein.readline())
B = []
for elem in A:
    B.append(int(elem))

out = ''
B.sort()
filein.close()

print(B[k-1])

