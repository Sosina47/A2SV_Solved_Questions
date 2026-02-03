def swap_case(s):
    result = ''
    for i in s:
        if 48 <= ord(i) <= 57:
            result += i
            continue
        if i == i.lower():
            temp = i.upper()
            result += temp
        else:
            temp = i.lower()
            result += temp
            
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
