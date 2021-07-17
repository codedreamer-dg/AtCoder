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
a, b, c = minp()
if a == b:
    if not c:
        print('Aoki')
    else:
        print('Takahashi')
elif a > b:
    print("Takahashi")
else:
    print('Aoki')