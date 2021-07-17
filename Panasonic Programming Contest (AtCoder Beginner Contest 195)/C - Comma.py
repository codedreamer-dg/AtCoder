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
cnt = 0
n = sinp()
x = len(n) // 3
if len(n) % 3 == 0:
    x -= 1
while x:
    y = int(pow(10, x * 3))
    cnt += x * (int(n) - y + 1)
    n = str(y - 1)
    x -= 1
pr(cnt)

