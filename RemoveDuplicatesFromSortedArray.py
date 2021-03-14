def removeDuplicates(nums):
    if len(nums) < 2:
        return len(nums)

    x = 0
    for i, j in enumerate(nums):
        if j == nums[x]:
            continue

        x += 1
        if x != i:
            nums[x] = j

    return x + 1
