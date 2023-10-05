arr=[3,7,4,9,1,6,5]
n=len(arr)
#Iterative
def bubble_sort(arr,n):
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
print("The resultant Array is:", end=" ")
print(bubble_sort(arr,n))
#Recursive
def bubbleSort(arr,i,n):
    if i>=n-1:
        return arr
    else:
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        return bubbleSort(arr,i+1,n)
print("The resultant Array is:", end=" ")
print(bubbleSort(arr,0,n))