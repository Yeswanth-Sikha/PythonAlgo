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


nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(search(nums, target))

'''
Runtime: 308 ms
Memory Usage: 15.6 MB
'''
