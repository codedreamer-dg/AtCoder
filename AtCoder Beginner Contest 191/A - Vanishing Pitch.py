# This code is contributed by Devanshu Garg. Please do not copy the code.
# Time : 5:36:19 PM
# Date : 06/02/2021
#Importing Libraries
import sys
from collections import defaultdict as dd
from math import *
from bisect import *
#increasing recursion limit for prevention recursion depth exceed error
sys.setrecursionlimit(10 ** 8)
#some general functions for taking input from user
def sinp():
    return input()
def inp():
    return int(input())
def minp():
    return map(int, input().split())
def linp():
    return list(minp())
def strl():
    return list(input())
def pr(x):
    print(x)
# This code is contributed by Devanshu Garg. Please do not copy the code.
mod = int(1e9+7)
v, t, s, d = minp()
time = d // v
if d < t * v or d > s * v:
    print("Yes")
else:
    print("No")

