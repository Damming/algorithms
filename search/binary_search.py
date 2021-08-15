def binary_search(items: list, item: str):
    if not len(items):
        return False
    if item > items[-1]:
        return False
    elif item < items[0]:
        return False
    n = len(items) // 2
    if items[n] == item:
        return True
    else:
        if items[n] < item:
            return binary_search(items[n:], item)
        else:
            return binary_search(items[:n], item)


if __name__ == '__main__':
    print(binary_search(['a', 'b', 'c'], 'b'))
