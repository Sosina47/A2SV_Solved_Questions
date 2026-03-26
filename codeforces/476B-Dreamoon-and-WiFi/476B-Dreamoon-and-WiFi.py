def backtrack(i, end, command):
    if i >= len(command):
        final.append(end)
        return 
    
    if command[i] == '+':
        end += 1
        i += 1
        backtrack(i, end, command)

    elif command[i] == '-':
        end -= 1
        i += 1
        backtrack(i, end, command)

    else:
        for dxn in (1, -1):
            end += dxn
            backtrack(i + 1, end, command)
            end -= dxn

        i += 1 

sent = input()
recieved = input()

final = []
backtrack(0, 0, recieved)

destined = 0
for command in sent:
    if command == '+':
        destined += 1
    
    else:
        destined -= 1

correct = final.count(destined)
print(correct / len(final))