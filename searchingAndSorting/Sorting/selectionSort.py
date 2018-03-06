# This code imlements selection Sort

arr = [3,4,6,2,8,7]


for i in range(len(arr)):
    min_index = i
    for j in range(min_index,len(arr)):
        if arr[min_index] >= arr[j]:
            min_index = j
    
    arr[i],arr[min_index] = arr[min_index],arr[i]
    
print (arr)