def swapSort(nums: [int]):
    """
    原地交换
    :param nums: num array
    """
    i = 0
    while i < len(nums):
        if nums[i] == i:
            i += 1
            continue
        nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


if __name__ == '__main__':
    num_array = [6, 3, 5, 7, 1, 0, 2, 4]
    swapSort(num_array)
    print(num_array)
