def inp():
    return input()
def linp():
    return list(map(int, input().split()))
def minp():
    return map(int, input().split())
n, x = minp()
s = 0
flag = 0
l = []
for _ in range(n):
    l.append(linp())
for i in range(len(l)):
    v = l[i][0]
    p = l[i][1]
    s += int(v * p)
    if s > x * 100 :
        pos = i + 1
        flag = 1
        break
if flag:
    print(pos)
else:
    print(-1)


