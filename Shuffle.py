def shuffle(nums: list[int], n: int) -> list[int]:
    reps = int(len(nums)/2)
    shuffle = []
    for i in range(reps):
        shuffle.append(nums[i])
        shuffle.append(nums[reps+i])
    return shuffle


if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    print(shuffle(nums, n))


'''
Runtime: 56 ms
Memory Usage: 14.1 MB
'''
