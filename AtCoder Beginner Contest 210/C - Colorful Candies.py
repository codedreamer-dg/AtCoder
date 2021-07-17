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
n, k = minp()
c = linp()
d = dd(int)
for i in range(k):
    d[c[i]] += 1
ans = len(d)
for i in range(k, n):
    d[c[i - k]] -= 1
    if not d[c[i - k]]:
        del d[c[i - k]]
    d[c[i]] += 1
    ans = max(ans, len(d))
pr(ans)