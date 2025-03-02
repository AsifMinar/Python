a = [1,2,3,4,5,6,7]
k = 3
kn = k%len(a)
a[:] = a[-kn:] + a[:-kn]
print(a)