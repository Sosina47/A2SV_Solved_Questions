from itertools import accumulate

for _ in range(int(input())):
    len_r = int(input())
    red = list(accumulate(list(map(int, input().split()))))

    len_b = int(input())
    blue = list(accumulate(list(map(int, input().split()))))

    max_blue = max(blue)
    max_red = max(red)
    
    print(max(0, max_blue, max_red, max_blue + max_red))
