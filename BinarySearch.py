def search(nums: list[int], target: int) -> int:
    # Input: nums = [-1,0,3,5,9,12], target = 2
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = ((r+l) // 2)  # always center index or left index of center
        if(nums[m] < target):
            l = m + 1
            continue
        elif(nums[m] > target):
            r = m - 1
            continue
        elif(nums[m] == target):
            return m
    return -1


nums = list(map(int, input().split(',')))
target = int(input())
print(search(nums, target))
