filein = open('rosalind_fib.txt', encoding = 'UTF-8')

num = filein.readline().split(' ')
n = int(num[0])
k = int(num[1])
list = []
list.append(1)
list.append(1)
for i in range(2,n):
    list.append(list[i-2]*k + list[i-1])

filein.close()
print(list[n-1])
