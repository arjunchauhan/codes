# This code imlements bubble sort

arr = [3,7,5,1,9,8]

for i in range(len(arr)):
    swapped = False
    
    for j in range(len(arr)-i-1):
        if arr[j] >= arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            swapped = True
    
    if swapped == False:
        break
        
print (arr)