#                   __         __                                         __     
#   _________  ____/ /__  ____/ /_______  ____ _____ ___  ___  _____ ____/ /___ _
#  / ___/ __ \/ __  / _ \/ __  / ___/ _ \/ __ `/ __ `__ \/ _ \/ ___// __  / __ `/
# / /__/ /_/ / /_/ /  __/ /_/ / /  /  __/ /_/ / / / / / /  __/ /   / /_/ / /_/ / 
# \___/\____/\__,_/\___/\__,_/_/   \___/\__,_/_/ /_/ /_/\___/_/____\__,_/\__, /  
#                                                            /_____/    /____/   
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
a, b, c = minp()
if a >= 0 and b >= 0:
    if a > b:
        pr(">")
    elif a == b:
        pr("=")
    else:
        pr("<")
elif a >= 0 and b < 0:
    if c & 1:
        pr(">")
    else:
        b = abs(b)
        if a > b:
            pr(">")
        elif a == b:
            pr("=")
        else:
            pr("<")
elif a < 0 and b >= 0:
    if c & 1:
        pr("<")
    else:
        a = abs(a)
        if a > b:
            pr(">")
        elif a == b:
            pr("=")
        else:
            pr("<")
else:
    if c & 1:
        if a > b:
            pr(">")
        elif a == b:
            pr("=")
        else:
            pr("<")
    else:
        if a < b:
            pr(">")
        elif a == b:
            pr("=")
        else:
            pr("<")