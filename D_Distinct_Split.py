from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    s_count = Counter(s)
    set_a = set()

    max_possible = 0
    cur_a = 0
    cur_b = len(s_count)

    for i in range(n - 1):
        s_count[s[i]] -= 1

        if s[i] not in set_a:
            set_a.add(s[i])
            cur_a += 1
        
        if s_count[s[i]] == 0:
            cur_b -= 1         
        
        max_possible = max(max_possible, cur_a + cur_b)

    print(max_possible) 
