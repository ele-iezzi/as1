from hsros import downheap
from hsros import upheap

filein = open('rosalind_ps.txt', encoding = 'UTF-8')

n = int(filein.readline())
A = filein.readline().replace('\n','').split(' ')
k = int(filein.readline())
tree = []

for elem in A:
    tree.append(int(elem))
    i = len(tree) - 1
    if i > 0:
        upheap(tree, i)

res = []
while len(tree) > 0:
    res.append(int(tree[0]))
    tree[0] = tree[len(tree)-1]
    tree.pop(len(tree)-1)
    downheap(tree, 0)

res.reverse()
res = res[0:k]
out = str(res).replace(',','')

out = out[1:len(out)-1]
#file where to save the solution, result too big to print
fileout = open('rosalind_ps_sol.txt', 'w', encoding = 'UTF-8')
fileout.write(out)
filein.close()
fileout.close()
print(out)
