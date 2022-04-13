def longestCommonPrefix(strs: list[str]) -> str:
    reference = strs[0]
    result = ''
    for i in range(len(reference)):
        for string in strs:
            try:
                if (reference[i] != string[i]):
                    return result
            except:
                return result
        result += reference[i]
    return result


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(longestCommonPrefix(strs))

'''
Runtime: 57 ms
Memory Usage: 13.9 MB
'''
