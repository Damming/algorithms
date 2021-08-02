def countingSort(arr, maxValue):
    bucketLen = maxValue + 1
    bucket = [0] * bucketLen
    sortedIndex = 0
    arrLen = len(arr)
    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    for j in range(bucketLen):
        while bucket[j] > 0:
            arr[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1
    return arr


if __name__ == '__main__':
    num_array = [6, 3, 5, 7, 1, 0, 2, 4]
    num_array = countingSort(num_array, 7)
    print(num_array)
