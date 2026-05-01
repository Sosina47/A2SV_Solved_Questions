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
    adj_list = defaultdict(list)

    node = None
    for _ in range(n - 1):
        i, j = nums()

        adj_list[i].append(j) 
        adj_list[j].append(i) 
        node = i

    if node == None:
        print(0)
        return 
    
    que = deque([node])
    new = None 

    visited = {node}

    while que:
        for _ in range(len(que)):

            node = que.popleft()
            new = node

            for val in adj_list[node]:
                if val not in visited:

                    que.append(val)
                    visited.add(val)

    que = deque([new])
    count = -1
    visited = {new}
    
    while que:
        count += 1
        for _ in range(len(que)):
            node = que.popleft()

            for val in adj_list[node]:
                if val not in visited:

                    visited.add(val)
                    que.append(val)

    print(3 * count)

def main():
    t = 1

    # t = num()
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()