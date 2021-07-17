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
n = input()
if len(n) % 2 == 0:
    a = n[:len(n)//2]
    b = n[len(n)//2:]
    if int(a) > int(b):
        pr(int(a) - 1)
    else:
        pr(int(a))
else:
    m = len(n) // 2
    pr(int(pow(10, m)) - 1)