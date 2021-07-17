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
    return int(stdin.readline())
def minp():
    return map(int, stdin.readline().split())
def linp():
    return list(minp())
def strl():
    return list(stdin.readline())
def pr(x):
    print(x)
mod = int(1e9+7)
h, w, x, y = minp()
mat = []
for i in range(h):
    mat.append(list(input()))
i, j = x - 1, y - 1
cst = 0
while i > -1:
    if mat[i][j] == '.':
        cst += 1
    else:
        break
    i -= 1
i, j = x - 1, y - 1
while i < h:
    if mat[i][j] == '.':
        cst += 1
    else:
        break
    i += 1
i, j = x - 1, y - 1
while j > -1:
    if mat[i][j] == '.':
        cst += 1
    else:
        break
    j -= 1
i, j = x - 1, y - 1
while j < w:
    if mat[i][j] == '.':
        cst += 1
    else:
        break
    j += 1
pr(cst - 3)