def partition(arr, low, hig):
    p=arr[low]
    start=low
    end=hig
    while True:
        while start <= end and arr[end] >= p:
            end-=1
        while start <= end and arr[start] <= p:
            start+=1
        if start <= end :
            arr[start], arr[end] = arr[end], arr[start]
        else:
            break
    arr[low], arr[end] = arr[end], arr[low]
    return end

def quick_sort(arr, start, end):
    if start < end :
        idx = partition(arr, start, end)

        quick_sort(arr, start, idx-1)
        quick_sort(arr, idx+1, end)      

arr1=[7,6,10,5,9,2,1,15,7]
quick_sort(arr1, 0, len(arr1)-1)
print(arr1)  