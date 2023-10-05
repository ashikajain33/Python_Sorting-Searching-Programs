arr=[3,7,4,9,1,6,5]
target=6
n=len(arr)-1
#iterative
def LinearSearch(arr,n, target):
    for i in range(n+1):
        if arr[i] == target:
            return i
        i+=1
    return -1
print(target," value found at ",end="")
print(LinearSearch(arr,n,target))
#recursive
def linear_search(arr,i,target,n):
    if i > n:
        return -1
    if arr[i] == target :
        return i
    else:
        return linear_search(arr,i+1, target,n)
print(target," value found at ",end="")
print(linear_search(arr, 0, target, n))
