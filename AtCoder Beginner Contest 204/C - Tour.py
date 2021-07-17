from sys import *
'''sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w') '''
from collections import defaultdict as dd
from math import *
from bisect import *
from collections import deque
#sys.setrecursionlimit(10 ** 8)
def sinp():
    return input()
def inp():
    return int(sinp())
def minp():
    return map(int, sinp().split())
def linp():
    return list(minp())
def strl():
    return list(sinp())
def pr(x):
    print(x)
mod = int(1e9+7)
def isReachable(s):
    visited = [False] * n
    queue = deque()
    queue.append(s)
    visited[s] = True
    c = 0
    while queue:
        node = queue.popleft()
        c += 1
        for i in g[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return c
n, m = minp()
g = dd(list)
for i in range(m):
    a, b = minp()
    g[a - 1].append(b - 1)
res = 0
for i in range(n):
    res += isReachable(i)
pr(res)