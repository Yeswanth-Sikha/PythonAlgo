def minimumSum(num: int) -> int:
    numList = list(map(int, list(str(num))))
    numList.sort()
    return ((numList[0]*10 + numList[2]) + (numList[1]*10 + numList[3]))


if __name__ == "__main__":
    num = int(input())
    print(minimumSum(num))

'''
Runtime: 30 ms
Memory Usage: 13.8 MB
'''
