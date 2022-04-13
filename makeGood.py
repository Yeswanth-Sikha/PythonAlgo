def makeGood(s: str) -> str:
    chars = list(s)
    change = 1
    while change > 0:
        change = 0
        for i in range(len(chars[:-1])):
            # check for Lower, Upper
            if (chars[i].islower()):
                if(chars[i].upper() == chars[i+1]):
                    chars.pop(i)
                    chars.pop(i)
                    change = 1
                    break
            # check for Upper, Lower
            else:
                if(chars[i].lower() == chars[i+1]):
                    chars.pop(i)
                    chars.pop(i)
                    change = 1
                    break

    s = ''.join(chars)
    return s


if __name__ == '__main__':
    s = input()
    print(makeGood(s))

'''
Runtime: 80 ms
Memory Usage: 13.8 MB
'''
