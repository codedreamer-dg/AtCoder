import sys
from collections import defaultdict as dd
from math import *
from bisect import *
#sys.setrecursionlimit(10 ** 8)
def sinp():
    return input()
def inp():
    return int(input())
def minp():
    return map(int, input().split())
def linp():
    return list(minp())
def strl():
    return list(input())
def pr(x):
    print(x)
    return
mod = int(1e9+7)
def countConsecutive(N): 
    count = 0
    L = 1
    while( L * (L + 1) < 2 * N): 
        a = (1.0 * N - (L * (L + 1) ) / 2) / (L + 1) 
        if (a - int(a) == 0.0): 
            count += 1
        L += 1
    return count 
n = inp()
print(2 * (countConsecutive(n) + 1))

