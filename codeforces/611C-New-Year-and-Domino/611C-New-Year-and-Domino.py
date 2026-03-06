# pad '#'
for i in range(row):
    grid[i].append('#')
grid.append(['#'] * (col + 1)) 

prefix_h = [[0] * (col + 1) for _ in range(row + 1)]
prefix_v = [[0] * (col + 1) for _ in range(row + 1)]

for r in range(row):
    for c in range(col):
        if grid[r][c] != '#':
            if grid[r][c - 1] != '#':
                prefix_h[r][c] = 1
            
            if grid[r - 1][c] != '#':
                prefix_v[r][c] = 1

for r in range(row):
    for c in range(col):
        prefix_v[r][c] += prefix_v[r - 1][c] + prefix_v[r][c - 1] - prefix_v[r - 1][c - 1]
        prefix_h[r][c] += prefix_h[r - 1][c] + prefix_h[r][c - 1] - prefix_h[r - 1][c - 1]
        
for _ in range(int(input())):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1 
    c2 -= 1 

    pre_v = prefix_v[r2][c2] - prefix_v[r2][c1 - 1] - prefix_v[r1][c2] + prefix_v[r1][c1 - 1]
    pre_h = prefix_h[r2][c2] - prefix_h[r2][c1] - prefix_h[r1 - 1][c2] + prefix_h[r1 - 1][c1] 

    print(pre_v + pre_h)