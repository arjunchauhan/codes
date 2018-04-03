""" this code implements Longest Increasing Subsequence """


def lis(arr):
    n = len(arr)
    LIS = [1]*n
    
    
    # using bottom up manner
    for i in range(1,n):
        for j in range(0,i):
            if arr[i] > arr[j] and LIS[i] < LIS[j] + 1:
                LIS[i] = LIS[j] + 1
                
    maximum = 0
    
    return (max(LIS))

arr = [10,22,9,33,21,50,41,60]
print ("Lic is " + str(lis(arr)))