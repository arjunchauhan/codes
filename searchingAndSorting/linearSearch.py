# returns the index of the array if key is found.
# returns -1 if key is not found in array.


def linearSearch(arr, key):

    for i in range(len(arr)):
        if arr[i] == key :
            return i

    return -1


# testing
# a = [1,2,3,4]
# print (linearSearch(a,3))
    
