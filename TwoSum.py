def twoSum(nums, target):
    for i in range(0, len(nums)):
        ni = nums[i]

        for j in range(1, len(nums)):
            if j != i:
                nj = nums[j]
            else:
                nj = None

            if nj is not None and ni + nj == target:
                return [i, j]
