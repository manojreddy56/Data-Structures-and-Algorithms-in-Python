def binary_search_itr(Arr, key):
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


def binary_search_rec(Arr, key, l, r):
    if l > r:
        return -1
    else:
        mid = (l + r) // 2
        if Arr[mid] == key:
            return mid
        elif Arr[mid] > key:
            return binary_search_rec(Arr, key, l, mid-1)
        elif Arr[mid] < key:
            return binary_search_rec(Arr, key, mid+1, r)


Arr = [84, 21, 47, 96, 15]
print(binary_search_itr(Arr, 47))
print(binary_search_rec(Arr, 47))
