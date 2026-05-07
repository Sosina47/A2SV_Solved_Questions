import sys
import math
import random
import heapq

input = sys.stdin.readline

def num(): return int(input())
def lst(): return list(map(int, input().split()))
def nums(): return tuple(map(int, input().split()))
def string(): return input().strip() 

def solve():
    n = num()
    heap = []
    output = []

    for _ in range(n):
        line = string()

        if 'removeMin' in line: 
            if not heap: 
                heapq.heappush(heap, 0)
                output.append("insert 0")
                
            heapq.heappop(heap)

            output.append(line)

        else: 
            op, n = line.split(' ')
            n = int(n)

            if op == 'insert': 
                heapq.heappush(heap, n)

                output.append(line)

            else: 
                while heap and heap[0] < n:
                    heapq.heappop(heap)

                    output.append("removeMin")

                if not heap or heap[0] > n: 
                    heapq.heappush(heap, n)

                    output.append(f'insert {n}')

                output.append(line)

    print(len(output))
    for line in output: 
        print(line)

        




def main():
    t = 1

    # t = num()
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()