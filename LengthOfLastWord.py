def lengthOfLastWord(s: str) -> int:
    List = list(s.split())
    lastWord = len(List[-1])
    return (lastWord)


if __name__ == "__main__":
    String = input()
    print(lengthOfLastWord(String))

'''
Runtime: 32 ms
Memory Usage: 13.9 MB
'''
