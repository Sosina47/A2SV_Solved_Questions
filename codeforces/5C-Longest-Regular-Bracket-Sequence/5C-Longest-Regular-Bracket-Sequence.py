s = input()
stack = [-1]
max_length = count = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)

    else:
        stack.pop()

        if not stack:
            stack.append(i)
    
    length = i - stack[-1]
    if length > max_length:
        count = 1
        max_length = length

    elif length == max_length and length > 0:
        count += 1

print(max_length, max(count, 1))