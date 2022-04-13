def lengthOfLastWord(s: str) -> int:
    List = list(s.split())
    lastWord = len(List[-1])
    return (lastWord)


if __name__ == "__main__":
    String = input()
    print(lengthOfLastWord(String))
