def inp():
    return input()
def linp():
    return list(map(int, input().split()))
def minp():
    return map(int, input().split())
n = inp()
if len(set(n)) == 1:
    print("Won")
else:
    print("Lost")

