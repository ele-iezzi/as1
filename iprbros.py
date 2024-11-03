filein = open('rosalind_iprb.txt', encoding = 'UTF-8')

num = filein.readline().split(' ')
k = int(num[0])
m = int(num[1])
n = int(num[2])
total = k+m+n
#Dom result in crossing: k x k 100% (1), k x m 100% (1), k x n 100% (1), m x m 75% (0.75), m x n 50% (0.5)
kk = (k / total) * ((k - 1) / (total - 1))
km = (k / total) * (m / (total - 1)) + (m / total) * (k / (total - 1))
kn = (k / total) * (n / (total - 1)) + (n / total) * (k / (total - 1))
mm = (m / total) * ((m - 1) / (total - 1)) * 0.75
mn = (m / total) * (n / (total - 1)) * 0.5 + (n / total) * (m / (total - 1)) * 0.5


out = kk + km + kn + mm + mn

filein.close()
print(out)
