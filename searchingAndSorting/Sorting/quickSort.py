# This code implements quick sort

def partition(arr,start, end):
    i = (start - 1)
    pivot = arr[end]
    
    for j in  range(start , end) :
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
            
    arr[i+1],arr[end] = arr[end],arr[i+1]
    return (i+1)
    
    
def quickSort(arr, start, end):
    if start < end :
        pi = partition(arr,start,end)
        
        quickSort(arr,start,pi-1)
        quickSort(arr,pi+1,end)
        
arr = [10,7,8,9,1,5]

quickSort(arr,0,len(arr)-1)
print (arr)