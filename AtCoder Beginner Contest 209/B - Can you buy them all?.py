#                _          _                                        _       
#   ___ ___   __| | ___  __| |_ __ ___  __ _ _ __ ___   ___ _ __  __| | __ _ 
#  / __/ _ \ / _` |/ _ \/ _` | '__/ _ \/ _` | '_ ` _ \ / _ \ '__|/ _` |/ _` |
# | (_| (_) | (_| |  __/ (_| | | |  __/ (_| | | | | | |  __/ |  | (_| | (_| |
#  \___\___/ \__,_|\___|\__,_|_|  \___|\__,_|_| |_| |_|\___|_|___\__,_|\__, |
#                                                           |_____|    |___/ 
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
n, x = minp()
a = linp()
for i in range(n):
    if i & 1:
        a[i] -= 1
if sum(a) <= x:
    pr("Yes")
else:
    pr("No")