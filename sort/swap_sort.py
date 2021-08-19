def swapSort(nums):
    """
    不能有重复
    """
    i = 0
    while i < len(nums):
        if nums[i] == i:
            i += 1
            continue
        nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


def FailureAwareSwapSort(nums):
    """
    如果有重复返回 False
    """
    i = 0
    while i < len(nums):
        if nums[i] == i:
            i += 1
            continue
        if nums[i] >= len(nums) or nums[i] == nums[nums[i]]:
            return False
        nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return True


if __name__ == '__main__':

    # num_array = [6, 3, 5, 7, 1, 0, 2, 4]
    # swapSort(num_array)
    # print(num_array)

    num_array = [6, 3, 5, 7, 1, 0, 2, 8]
    result = FailureAwareSwapSort(num_array)
    if result:
        print(num_array)
    else:
        print(result)
