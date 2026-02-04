t = int(input())

for _ in range(t): 
    s = input()
    key = set()

    doors = {'R', 'G', 'B'}

    for letter in s:
        if letter in doors and letter.lower() not in key:
            print('NO')
            break
        key.add(letter.lower())
    
    else:
        print('YES')
        
