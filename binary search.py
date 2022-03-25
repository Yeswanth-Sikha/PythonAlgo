def binarySearch(num: int, arr: list, index: int):
    place = len(arr)//2
    midNum = arr[place]

    if (midNum < arr[place]):
        return binarySearch(num, arr[:place], index)
    elif (midNum > arr[place]):
        index += place
        return binarySearch(num, arr[place+1:], index)
    elif (midNum == arr[place]):
        index = place
        return (index)


num = int(input())
arr = list(map(int, input().split()))
arr.sort()
index = 0
print(binarySearch(num, arr, index))
