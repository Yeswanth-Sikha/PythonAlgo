from math import ceil, sqrt
'''
JUMP SEARCH
- find the steps m needed to jump for optimal condition (m = sqrt(n))
- when a we find a index whose value is greater than num, take it as max index, min index = max index - jump,
- recurse with max index and min index and min index being the result value

'''


def JumpSearch(num, arr, minIndex, maxIndex):
    jump = int(ceil(sqrt(len(arr))))
    linearSearch = (maxIndex - minIndex) % jump
    for i in range(maxIndex-linearSearch+1, maxIndex+1):
        if (arr[i] == num):
            return i
    for i in range(minIndex, maxIndex+1, jump):
        print(arr[i], num)
        if (arr[i] > num):
            maxIndex = i-1
            minIndex = (i - jump)+1 if (i > 0) else 0
            return JumpSearch(num, arr, minIndex, maxIndex)
        elif (arr[i] == num):
            return i
        else:
            continue
        print('')


num = int(input())
arr = list(map(int, input().split()))
minIndex = 0
maxIndex = len(arr)-1
arr.sort()

print(JumpSearch(num, arr, minIndex, maxIndex))
