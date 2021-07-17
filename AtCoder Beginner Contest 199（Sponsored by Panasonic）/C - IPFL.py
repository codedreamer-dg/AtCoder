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
s = strl()
q = inp()
c = 0
for i in range(q):
    t, a, b = minp()
    if t == 1:
        if c & 1:
            if a > n:
                a -= n
            else:
                a += n
            if b > n:
                b -= n
            else:
                b += n
        s[a - 1], s[b - 1] = s[b - 1], s[a - 1]
    else:
        c += 1
if c & 1:
    print(''.join(s[n:] + s[:n]))
else:
    print(''.join(s))