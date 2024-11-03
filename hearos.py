filein = open('rosalind_hea.txt', encoding = 'UTF-8')

n = int(filein.readline())
A = filein.readline().replace('\n','').split(' ')
tree = []

def downheap(T, i):
    if i == len(T)-1 or 2*i + 1 >= len(T) or len(T) == 0:
        return
    if 2*i + 2 < len(T):
        if T[i] > T[2*i + 1] and T[i] > T[2*i + 2]:
            return
        if T[i] < T[2*i + 1] and T[i] >= T[2*i + 2]:
            temp = T[2*i + 1]
            T[2*i + 1] = T[i]
            T[i] = temp
            downheap(T, 2*i+1)
        elif T[i] < T[2*i + 2] and T[i] >= T[2*i + 1]:
            temp = T[2*i + 2]
            T[2*i + 2] = T[i]
            T[i] = temp
            downheap(T, 2*i+2)
        elif T[i] < T[2*i + 1] and T[i] < T[2*i + 2]:
            if T[2*i + 1] > T[2*i + 2]:
                temp = T[i]
                T[i]= T[2*i + 1]
                T[2*i + 1] = temp
                downheap(T, 2*i+1)
            else:
                temp = T[i]
                T[i]= T[2*i + 2]
                T[2*i + 2] = temp
                downheap(T, 2*i+2)
    else:
        if T[i] > T[2*i + 1]:
            return
        if T[i] < T[2*i + 1]:
            temp = T[2*i + 1]
            T[2*i + 1] = T[i]
            T[i] = temp
            downheap(T, 2*i+1)
            

def upheap(T, i):
    if i == 0:
        downheap(T,i)
        return
    if i%2 == 1:
        if T[i] > T[(i - 1) // 2]:
            temp = T[(i - 1 ) // 2]
            T[(i - 1 ) // 2] = T[i]
            T[i] = temp
            upheap(T, (i - 1 ) // 2)
    if i%2 == 0:
        if T[i] > T[(i - 2 ) // 2]:
            temp = T[(i - 2 ) // 2]
            T[(i - 2 ) // 2] = T[i]
            T[i] = temp
            upheap(T, (i - 2 ) // 2)

for elem in A:
    tree.append(int(elem))
    i = len(tree) - 1
    if i > 0:
        upheap(tree, i)

out = str(tree).replace(',','')

out = out[1:len(out)-1]
#file where to save the solution, result too big to print
fileout = open('rosalind_hea_sol.txt', 'w', encoding = 'UTF-8')
fileout.write(out)
filein.close()
fileout.close()
print(out)

