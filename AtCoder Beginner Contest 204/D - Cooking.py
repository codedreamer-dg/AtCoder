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
def solve(a, n):
    s = 0
    s = sum(a)
    dp = [[0 for i in range(s + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for j in range(1, s + 1):
        dp[0][j] = False
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            dp[i][j] = dp[i - 1][j]
            if a[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - a[i - 1]]
    d = maxsize
    for j in range(s // 2, -1, -1):
        if dp[n][j] == True:
            d = s - (2 * j)
            break
    return d
n = inp()
t = linp()
ans = solve(t, n)
pr(((sum(t) - ans) // 2 + ans))