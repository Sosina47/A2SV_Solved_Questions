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
    words = []

    for i in range(n): 
        words.append(string())

    adj = defaultdict(list)
    depends = defaultdict(int)
    
    for i in range(1, n):
        j = k = 0

        while j < len(words[i - 1]) and k < len(words[i]):
            if words[i - 1][j] != words[i][k]: 

                adj[words[i - 1][j]].append(words[i][k])
                depends[words[i][k]] += 1

                break

            j += 1
            k += 1

        if j < len(words[i - 1]) and k == len(words[i]):
            return print("Impossible")
        
    output = []
    que = deque()
    
    ch = 'a'
    while ch <= 'z':
        if depends[ch] == 0: 
            que.append(ch)

        ch = chr(ord(ch) + 1)

    while que:
        ch = que.popleft()
        output.append(ch)

        for val in adj[ch]: 
            depends[val] -= 1

            if depends[val] == 0:
                que.append(val)

    if len(output) < 26:
        print("Impossible")

    else: 
        print("".join(output))

        






def main():
    t = 1

    # t = num()
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()