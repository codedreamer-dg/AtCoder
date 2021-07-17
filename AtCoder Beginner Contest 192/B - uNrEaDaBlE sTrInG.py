import sys
'''sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w')''' 
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
mod = int(1e9+7)
s = sinp()
a = s[::2]
b = s[1::2]
if (a.islower() and b.isupper()) or (a.islower() and len(b) == 0) or (b.isupper() and len(a) == 0):
    pr("Yes")
else:
    pr("No")