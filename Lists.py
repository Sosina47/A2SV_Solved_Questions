if __name__ == '__main__':
    N = int(input())
    arr = []
    
    for _ in range(N):
        cmds = list(input().split())
        
        match cmds[0]:
            case 'print':
                print(arr)
            case 'insert':
                arr.insert(int(cmds[1]), int(cmds[2]))
            case 'remove':
                arr.remove(int(cmds[1]))
            case 'append':
                arr.append(int(cmds[1]))
            case 'sort':
                arr.sort()
            case 'pop':
                arr.pop()
            case _:
                arr.reverse()            
