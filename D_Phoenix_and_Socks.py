from collections import Counter

for _ in range(int(input())):
    n, l, r = map(int, input().split())
    socks = list(map(int, input().split()))

    left = socks[:l]
    right = socks[l:]

    left_count = Counter(left)
    right_count = Counter(right)
    to_delete = []

    for key in left_count:
        if key in right_count:
            if left_count[key] > right_count[key]:
                left_count[key] -= right_count[key]
                del right_count[key]

            elif left_count[key] < right_count[key]:
                right_count[key] -= left_count[key]
                to_delete.append(key)

            else:
                to_delete.append(key)
                del right_count[key]

    for val in to_delete:
        del left_count[val]

    left = list(left_count.values())
    left_values = sum(left)

    right = list(right_count.values())
    right_values = sum(right)

    if left_values == right_values:
        print(left_values)
        continue

    elif left_values < right_values:
        left, right = right, left

    count = 0
    diff = abs(left_values - right_values) // 2

    for val in range(len(left)):
        if left[val] > 1:
            i = min(diff, left[val] // 2) 
            diff -= i
            left[val] -= 2 * i
            count += i
        
        if diff == 0:
            break
        
    print(diff + count + ((sum(left) + sum(right)) // 2) )
            
