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
setrecursionlimit(10 ** 6)
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
max_n = 2*int(1e5)
n = inp()
l = linp()
if l == l[::-1]:
    pr(0)
else:
    g = dd(list)
    s = 0
    e = n - 1
    vis = [0 for i in range(max(l) + 1)]
    while s < e:
        x, y = l[s], l[e]
        if x != y:
            vis[x] = vis[y] = 1
            g[x].append(y)
            g[y].append(x)
        s += 1
        e -= 1
    vis = [0 for i in range(max_n + 1)]
    ans = 0
    for i in range(1, max_n + 1):
        if vis[i]:
            continue
        st = []
        st.append(i)
        vis[i] = 1
        c = 1
        while len(st):
            node = st[-1]
            st.pop(-1)
            for j in g[node]:
                if not vis[j]:
                    st.append(j)
                    vis[j] = 1
                    c += 1
        ans += c - 1
    pr(ans)