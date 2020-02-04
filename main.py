def root(p, c=0):
    global a, b
    if b[p] == -1:
        a[p] += c
        return p
    b[p] = root(b[p], a[p] + c)
    a[p] = 0
    return b[p]


n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) - 1 for i in input().split()]
unref = set([i for i in range(n)])
for i in range(n):
    if b[i] != -1:
        unref.remove(b[i])
unref = list(unref)
for point in unref:
    root(point)
print(*a)
