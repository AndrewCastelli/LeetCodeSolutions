def findMedianSortedArrays(nums1, nums2) -> float:
    length = float(len(nums1) + len(nums2))
    nums3 = [a for b in [nums1, nums2] for a in b]
    nums3.sort()

    # If length is odd
    if length % 2 != 0:
        med = int(length / 2)
        median = float(nums3[med])

    # If length is even
    else:
        med_1 = int(length / 2 - 1)
        med_2 = int(length / 2)
        median = (nums3[med_1] + nums3[med_2]) / 2

    return float(median)
