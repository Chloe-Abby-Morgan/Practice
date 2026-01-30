#https://cses.fi/problemset/task/2422

N = int(input())
# table = sorted([j*elt for elt in (i for i in range(1,N+1)) for j in range(1,N+1)])
# print(table[len(table)//2])

median = (N*N+1)/2

left = 1
right = N*N

def lesser(x, n):
    total = 0
    for i in range(1, n+1):
        total += min(n, x // i)
    return total

while left < right:
    mid = (left+right) // 2
    if lesser(mid, N) >= median:
        right = mid
    else:
        left = mid + 1

print(left)