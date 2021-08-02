def shellSort(arr):
    import math
    gap = 1
    while (gap < len(arr) / 3):
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap = math.floor(gap / 3)
    return arr


if __name__ == '__main__':
    num_array = [6, 3, 5, 7, 1, 0, 2, 4]
    num_array = shellSort(num_array)
    print(num_array)
