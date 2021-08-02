def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    num_array = [6, 3, 5, 7, 1, 0, 2, 4]
    bubbleSort(num_array)
    print(num_array)
