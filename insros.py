filein = open('rosalind_ins.txt', encoding = 'UTF-8')

n = int(filein.readline())
A = filein.read().replace('\n','').split(' ')
count = 0
for i in range(1, n):
    k = i
    while k>0 and int(A[k]) < int(A[k-1]):
        temp = A[k-1]
        A[k-1] = A[k]
        A[k] = temp
        count = count + 1
        k = k-1
        
filein.close()
print(count)
