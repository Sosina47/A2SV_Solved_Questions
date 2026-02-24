from collections import Counter

for _ in range(int(input())):
    s = input()
    t = input()

    s_count = Counter(s)
    t_count = Counter(t)

    for key in s_count:
        if key not in t_count or t_count[key] < s_count[key]:
            print('Impossible')
            break
    
    else:
        t = []
        for key in t_count:
            for _ in range(t_count[key] - s_count[key]):
                t.append(key)
        
        t.sort()
        output = []
        
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] <= t[j]:
                output.append(s[i])
                i += 1

            else:
                output.append(t[j])
                j += 1

        output.extend(list(s[i:]))
        output.extend(list(t[j:]))
        
        print(''.join(output))
