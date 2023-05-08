#to write a selection sort
#iterative
print(" enter an array: ")
arr=list(map(int, input().split()))
size=len(arr)
for i in range(size):
    mini=i
    for j in range(i+1,size):
        if arr[j]<arr[mini]:
            mini=j
    (arr[i],arr[mini])=(arr[mini],arr[i])
print(arr)


#recursive
def selectionSort(a,start,n):
    if start>=n-1:
        return
    minpos=start
    for i in range(start+1,n):
        if a[i]<a[minpos]:
            minpos=i
    a[start],a[minpos]=a[minpos],a[start]
    selectionSort(a,start+1,n)
print(" enter an array: ")
arr=list(map(int, input().split()))
n=len(arr)
selectionSort(arr,0,n)
print(arr)