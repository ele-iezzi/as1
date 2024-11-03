filein = open('rosalind_par3.txt', encoding = 'UTF-8')

n = int(filein.readline())
A = filein.readline().replace('\n','').split(' ')
B = []
L = []
E = []
G = []
num = int(A[0])

for i in range(0,n):
    if int(A[i]) < num:
        L.append(A[i])
    elif int(A[i]) == num:
        E.append(A[i])
    else:
        G.append(A[i])

B = L + E + G

out = ''
for elem in B:
    out = out + ' ' + str(elem)

out = out[1::]
#file where to save the solution, result too big to print
fileout = open('rosalind_par3_sol.txt', 'w', encoding = 'UTF-8')
fileout.write(out)
filein.close()
fileout.close()
print(out)

