def binarySearch(arr, l, r, key):
    while ( l <= r):
        mid = int(l + (r-1)/2)

        if arr[mid] == key:
            return mid

        elif arr[mid] < key :
            l = mid + 1

        else:
            r = mid - 1

    return -1

# testing

# arr = [1,2,3,4,5,6,7]
# key = 6

# print(binarySearch(arr,0,6,key))
