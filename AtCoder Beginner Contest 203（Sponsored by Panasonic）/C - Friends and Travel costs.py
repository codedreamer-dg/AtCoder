# cook your dish here
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
# for _ in range(inp()):
n, k = minp()
l = []
for i in range(n):
    a, b = minp()
    l.append([a, b])
l.sort()
c = 0
for i in range(n):
    x = l[i][0] - c
    if k >= x:
        k -= x
        c += x
        k += l[i][1]
    else:
        c += k
        k = 0
        break
pr(c + k)