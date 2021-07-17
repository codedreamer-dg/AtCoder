from sys import *
'''sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w') '''
from collections import defaultdict as dd
from collections import deque
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
s = sinp()
t = deque()
c = 0
for i in s:
    if i == 'R':
        c += 1
    else:
        if c & 1:
            if len(t) and t[0] == i:
                t.popleft()
            else:
                t.appendleft(i)
        else:
            if len(t) and t[-1] == i:
                t.pop()
            else:
                t.append(i)
s = t
# i = 0
# while i < len(t):
#     if len(s) == 0 or t[i] != s[-1]:
#         s.append(t[i])
#     else:
#         s.pop()
#     i += 1
if c & 1:
    for i in range(len(s) - 1, -1, -1):
        print(s[i], end="")
    print()
else:    
    for i in range(len(s)):
        print(s[i], end="")
    print()

