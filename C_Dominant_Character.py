test = int(input())
for _ in range(test):
    length = int(input())
    s = input()

    if length < 2:
        print(-1)
        continue

    if 'aa' in s:
        print(2)
    elif 'aba' in s or 'aca' in s:
        print(3)
    elif 'abca' in s or 'acba' in s:
        print(4)
    elif 'abbacca' in s or 'accabba' in s:
        print(7)
    else:
        print(-1) 
