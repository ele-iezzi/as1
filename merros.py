filein = open('rosalind_mer.txt', encoding = 'UTF-8')

n = int(filein.readline())
A = filein.readline().replace('\n','').split(' ')
m = int(filein.readline())
B = filein.read().replace('\n','').split(' ')
i = 0
j = 0
C = []

while len(A)>0 and len(B)>0:
    if int(A[0]) < int(B[0]):
        C.append(A[0])
        A = A[1::]
    else:
        C.append(B[0])
        B = B[1::]
        
while len(A) > 0:
    C.append(A[0])
    A = A[1::]

while len(B) > 0:
    C.append(B[0])
    B = B[1::]
    

out = ''
for elem in C:
    out = out + ' ' + str(elem)

out = out[1::]
#file where to save the solution, result too big to print
fileout = open('rosalind_mer_sol.txt', 'w', encoding = 'UTF-8')
fileout.write(out)
filein.close()
fileout.close()
print(out)

