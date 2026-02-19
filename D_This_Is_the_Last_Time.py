tests = int(input())
for _ in range(tests):
    length, coin = map(int, input().split())
    casinos = []

    for _ in range(length):
        c = list(map(int, input().split()))
        casinos.append(c)

    casinos.sort(key = lambda x: (x[0], x[2]))

    merged = [casinos[0]]
    for i in range(1, length):
        if merged[-1][2] >= casinos[i][0]:
            merged[-1][1] = max(merged[-1][1], casinos[i][1])
            merged[-1][2] = max(merged[-1][2], casinos[i][2])
            
        else:
            merged.append(casinos[i])

    for casino in casinos:
        if coin < casino[2]:
            if casino[0] <= coin <= casino[1]:
                coin = casino[2]

    print(coin) 
