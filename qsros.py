filein = open('rosalind_qs.txt', encoding = 'UTF-8')

m = int(filein.readline())
A = filein.readline().replace('\n','').split(' ')

def quickSort(S):
    n = len(S)
    if n < 2:
        return
    p = int(S[0])
    L = []
    E = []
    G = []
    while len(S) > 0:
        elem = int(S.pop(0))
        if elem < p:
            L.append(elem)
        elif elem == p:
            E.append(elem)
        else:
            G.append(elem)
    quickSort(L)
    quickSort(G)
    while len(L) > 0:
        S.append(int(L.pop(0)))
    while len(E) > 0:
        S.append(int(E.pop(0)))
    while len(G) > 0:
        S.append(int(G.pop(0)))

quickSort(A)

out = ''
for elem in A:
    out = out + ' ' + str(elem)

out = out[1::]
#file where to save the solution, result too big to print
fileout = open('rosalind_qs_sol.txt', 'w', encoding = 'UTF-8')
fileout.write(out)
filein.close()
fileout.close()
print(out)

