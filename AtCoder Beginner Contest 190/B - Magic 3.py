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
n, s, d = minp()
flag = False
for i in range(n):
    x, y = minp()
    if x < s and y > d:
        flag = True
if flag:
    print("Yes")
else:
    print("No")
