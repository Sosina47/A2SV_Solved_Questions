from itertools import accumulate

for _ in range(int(input())):
    len_r = int(input())
    red = list(accumulate(list(map(int, input().split()))))

    len_b = int(input())
    blue = list(accumulate(list(map(int, input().split()))))
    output = [] 
    r = b = 0
    max_ = 0

    for r in range(len_r):
        max_ = max(max_, red[r])
        for b in range(len_b):
            max_ = max(max_, blue[b])
            max_ = max(max_, red[r] + blue[b])
    
    print(max_)
    
    
    
    
    
    

    # while r < len_r and b < len_b:
    #     if red[r] >= 0 and red[r] > blue[b]:
    #         output.append(red[r])
    #         r += 1

    #     elif blue[b] >= 0 and blue[b] > red[r]:
    #         output.append(blue[b])
    #         b += 1

    #     elif suffix_blue[b] > suffix_red[r]:
    #         output.append(blue[b])
    #         b += 1
    #     elif suffix_red[r] > suffix_blue[b]:
    #         output.append(red[r])
    #         r += 1

    #     else:
    #         if red[r] > blue[b]:
    #             output.append(red[r])
    #             r += 1
    #         else:
    #             output.append(blue[b])
    #             b += 1

    # output.extend(red[r:])
    # output.extend(blue[b:])
    
    # output = list(accumulate(output))
    # print(max(0, max(output)))