for _ in range(int(input())):
    n = int(input())
    initial = list(map(int, input()[::-1]))
    target = list(map(int, input()[::-1]))

    zeroes = initial.count(0)
    ones = n - zeroes  
    operations = 0

    for i in range(n):
        if ((initial[i] + operations) % 2) != target[i]:
            if zeroes != ones:
                # print(i, zeroes, ones)
                print('NO')
                break
                
            operations += 1
        if (initial[i] + operations) % 2:
            ones -= 1
        else:
            zeroes -= 1
    else:
        print('YES')
    
