def quickSort1(arr, left, right):
    """
    快速排序
    :param arr: array
    :param left: 左边界
    :param right: 右边界
    """
    # 子数组长度为 1 时终止递归
    if left >= right: return
    # 哨兵划分操作（以 arr[l] 作为基准数）
    i, j = left, right
    while i < j:
        while i < j and arr[j] >= arr[left]: j -= 1
        while i < j and arr[i] <= arr[left]: i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[i] = arr[i], arr[left]
    # 递归左（右）子数组执行哨兵划分
    quickSort1(arr, left, i - 1)
    quickSort1(arr, i + 1, right)


# =====================================================================

def quickSort2(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort2(arr, left, partitionIndex - 1)
        quickSort2(arr, partitionIndex + 1, right)
    return arr


def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index - 1)
    return index - 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    num_array = [6, 3, 5, 7, 1, 0, 2, 4]
    # quick_sort(num_array, 0, 7)
    num_array = quickSort2(num_array, 0, 7)
    print(num_array)
