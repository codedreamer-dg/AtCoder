#                   __         __                                         __     
#   _________  ____/ /__  ____/ /_______  ____ _____ ___  ___  _____ ____/ /___ _
#  / ___/ __ \/ __  / _ \/ __  / ___/ _ \/ __ `/ __ `__ \/ _ \/ ___// __  / __ `/
# / /__/ /_/ / /_/ /  __/ /_/ / /  /  __/ /_/ / / / / / /  __/ /   / /_/ / /_/ / 
# \___/\____/\__,_/\___/\__,_/_/   \___/\__,_/_/ /_/ /_/\___/_/____\__,_/\__, /  
#                                                            /_____/    /____/   
from sys import *
'''sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w') '''
from collections import defaultdict as dd
from math import *
from bisect import *
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
n, q = minp()
a = linp()
s = [a[0] - 1]
p = [s[0]]
for i in range(1, n):
    s.append(a[i] - a[i - 1] - 1)
    p.append(p[len(p) - 1] + s[len(s) - 1])
res = []
for i in range(q):
    k = inp()
    if k <= p[0]:
        res.append(k)
        continue
    if k > p[-1]:
        k -= p[-1]
        res.append(a[len(a) - 1] + k)
        continue
    l = 0
    idx = -1
    h = len(p) - 1
    while l <= h:
        m = (l + h) // 2
        if p[m] < k:
            idx = m
            l = m + 1
        else:
            h = m - 1
    left = k - p[idx]
    res.append(a[idx] + left)
print(*res, sep='\n')