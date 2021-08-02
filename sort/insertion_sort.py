def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current
    return arr


if __name__ == '__main__':
    num_array = [6, 3, 5, 7, 1, 0, 2, 4]
    insertionSort(num_array)
    print(num_array)
