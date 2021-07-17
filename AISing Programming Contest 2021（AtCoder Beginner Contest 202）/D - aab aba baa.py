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
def solve(string, n): 
    fact = [None for i in range(60)] 
    fact[0] = 1
    for i in range(1, 60): 
        fact[i] = fact[i - 1] * i 
    length = len(string) 
    freq = [0 for i in range(60)]
    for i in range(0, length): 
        freq[ord(string[i]) - ord('a')] += 1
    out = [None for i in range(60)]
    s, k = 0, 0
    while s != n: 
        s = 0
        for i in range(60): 
            if freq[i] == 0: 
                continue
            freq[i] -= 1
            xsum = fact[length - 1 - k] 
            for j in range(60): 
                xsum //= fact[freq[j]] 
            s += xsum 
            if s >= n:
                out[k] = chr(i + 97) 
                n -= s - xsum 
                k += 1
                break
            if s < n: 
                freq[i] += 1
    i = 59
    while k < length and i >= 0: 
        if freq[i]: 
            out[k] = chr(i + 97) 
            freq[i] -= 1
            i += 1
            k += 1
        i -= 1 
    return ''.join(out[:k])
a, b, k = minp()
print(solve('a' * a + 'b' * b, k))