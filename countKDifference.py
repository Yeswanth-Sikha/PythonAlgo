def countKDifference(nums: list[int], k: int) -> int:
    count = 0
    for i, numOuter in enumerate(nums[:-1]):
        for numInner in nums[i+1:]:
            if(abs(numOuter-numInner) == k):
                print(numOuter, numInner)
                count += 1
    return count


if __name__ == '__main__':
    nums = list(map(int, input().split(',')))
    k = int(input())
    print(countKDifference(nums, k))
