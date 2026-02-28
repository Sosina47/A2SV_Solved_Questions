for _ in range(int(input())):
    n, k = map(int, input().split())
    colors = input()

    count = left = 0

    for i in range(k):
        if colors[i] == 'B':
            count += 1

    min_recolor = k - count

    for right in range(k, len(colors)):
        if colors[right] == 'B':
            count += 1

        while right - left + 1 > k:
            if colors[left] == 'B':
                count -= 1
            left += 1

        if right - left + 1 == k:
            min_recolor = min(min_recolor, k - count)
    
    print(min_recolor)
