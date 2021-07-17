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
n = inp()
a = linp()
b = linp()
c = linp()
t = [0 for i in range(n)]
for i in range(n):
    t[i] = b[c[i] - 1]
d = dd(int)
for i in t:
    d[i] += 1
res = 0
for i in a:
    if i in d:
        res += d[i]
pr(res)