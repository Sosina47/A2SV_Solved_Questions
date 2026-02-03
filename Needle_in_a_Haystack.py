from collections import Counter

t = int(input())
for _ in range(t):
    s = input()
    t = input()

    s_counter = Counter(s)
    t_counter = Counter(t)

    for key, value in s_counter.items():
        if t_counter.get(key, 0) < value:
            print('Impossible')
            break

        t_counter[key] -= value
    
    else:
        output = ''
        t_key = list(t_counter.keys())
        t_key.sort()
        t = ''

        for key in t_key:
            for _ in range(t_counter[key]):
                t += key

        s_index = t_index = 0

        while s_index < len(s) and t_index < len(t):
            if s[s_index] <= t[t_index]:
                output += s[s_index]
                s_index += 1

            else:
                output += t[t_index]
                t_index += 1

        if s_index < len(s):
            output += s[s_index:]

        if t_index < len(t):
            output += t[t_index:]
        
        print(output)
