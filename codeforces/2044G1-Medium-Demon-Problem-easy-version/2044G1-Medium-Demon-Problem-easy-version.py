import sys
import math
import random

from itertools import accumulate
from bisect import bisect_left, bisect_right
from collections import defaultdict, Counter, deque

input = sys.stdin.readline

INF = float('inf')
MOD = 10**9 + 7
XOR = random.randint(1, 10 ** 7)

def num(): return int(input())
def lst(): return list(map(int, input().split()))
def nums(): return tuple(map(int, input().split()))
def string(): return input().strip() 

def solve():
    n = num()
    arr = lst()
    s = set(arr)

    adj = [[] for _ in range(n + 1)]
    givers = [0] * (n + 1)

    for i, give in enumerate(arr):
        givers[give] += 1
        adj[i + 1].append(give)

    q = deque()

    for i in range(1, n + 1): 
        if i not in s: 
            q.append(i)

    count = 2
    while q: 
        for _ in range(len(q)):
            spider = q.popleft()

            for val in adj[spider]:
                givers[val] -= 1

                if givers[val] == 0:
                    q.append(val)

        count += 1

    print(count)
    
            




def main():
    t = 1

    t = num()
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()