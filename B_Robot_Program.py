from math import ceil

t = int(input())
for _ in range(t):
    n, pos, k = map(int, input().split())
    instructions = input()

    for i in range(n):
        if instructions[i] == 'L':
            pos -= 1
        else:
            pos += 1
        
        
        if pos == 0:
            k -= i + 1
            break
    else:
        print(0)
        continue
    
    count = 1
    cycle = 0
    for i in range(n):
        if instructions[i] == 'L': 
            pos -= 1
        
        else:
            pos += 1

        if pos == 0:
            cycle = i + 1
            break

    else:
        print(1)
        continue

    print(count + k // cycle)
