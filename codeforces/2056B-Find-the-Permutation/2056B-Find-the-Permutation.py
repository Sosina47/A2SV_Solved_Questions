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

def dfs():
    pass



def solve():
    n = num()

    positions = []

    for i in range(n): 
        count = 1
        row = list(string())

        for j in range(n): 
            if j < i and row[j] == '1' or j > i and row[j] == '0': 
                count += 1
        
        positions.append((count, i + 1))
    

    positions.sort()

    output = []
    for _, val in positions:
        output.append(val)

    print(*output)




def main():
    t = 1

    t = num()
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()