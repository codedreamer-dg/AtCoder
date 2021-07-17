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
s = sinp()
pr(s[1:] + s[0])