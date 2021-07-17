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
def countPair(arr, n, k):
    cnt = 0
    for i in range(n):
        arr[i] = (arr[i] + k) % k
    hash = [0] * k
    for i in range(n):
        hash[arr[i]] += 1
    for i in range(k):
        cnt += (hash[i] * (hash[i] - 1)) / 2
    return int(cnt)
n = inp()
a = linp()
pr(countPair(a, n, 200))