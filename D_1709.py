tests = int(input())
for _ in range(tests):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    operations = []
    
    for i in range(n):
        for j in range(1, n - i):
            if a[j] < a[j - 1]:
                operations.append(f'{1} {j}')
                a[j], a[j - 1] = a[j - 1], a[j]
            
            if b[j] < b[j - 1]: 
                operations.append(f'{2} {j}')
                b[j], b[j - 1] = b[j - 1], b[j]

    for i in range(n):
        if a[i] > b[i]:
            operations.append(f'{3} {i + 1}')
            a[i], b[i] = b[i], a[i]

    print(len(operations))
    for i in operations:
        print(i)
