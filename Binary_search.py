def binary_search(Arr, key):
    l = 0
    r = len(Arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if key == Arr[mid]:
            return mid
        elif key < Arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1


Arr = [84, 21, 47, 96, 15]
print(binary_search(Arr, 47))