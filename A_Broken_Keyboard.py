for _ in range(int(input())):
    s = input()
    res = set()
    left = 0

    for right in range(len(s)):
        if s[right] != s[left]:
            if (right - left) % 2:
                res.add(s[left])
            left = right

    if (len(s) - left) % 2:
        res.add(s[-1])           
            
    print(''.join(sorted(list(res))))
