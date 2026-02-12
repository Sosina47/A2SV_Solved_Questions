r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
r3 = list(map(int, input().split()))
r4 = list(map(int, input().split()))
r5 = list(map(int, input().split()))

if 1 in r1:
    idx = r1.index(1) + 1
    if idx < 3:
        print(2 + 3 - idx % 3)
    else:
        print(2 + idx % 3)

elif 1 in r2:
    idx = r2.index(1) + 1
    if idx < 3:
        print(1 + 3 - idx % 3)
    else:
        print(1 + idx % 3)

elif 1 in r3:
    idx = r3.index(1) + 1
    if idx < 3:
        print(3 - idx % 3)
    else:
        print(idx % 3)

elif 1 in r4:
    idx = r4.index(1) + 1
    if idx < 3: 
        print(1 + 3 - idx % 3)
    else:
        print(1 + idx % 3)

else:
    idx = r5.index(1) + 1
    if idx < 3:
        print(2 + 3 - idx % 3)
    else:
        print(2 + idx % 3)
