# Iterative Approach
def insertionsort1(arr):
    for i in range (1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp :
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp
    return arr

# T(n) = O(n**2) --> worst case complexity
# T(n) = O(n)    --> best case complexity

# Recursive Approach
def insertionsort2(arr, start, n):
    if start >= n:
        return
    pos = start
    while pos > 0 and arr[pos] < arr[pos-1] :
        arr[pos], arr[pos-1] = arr[pos-1], arr[pos]
        pos = pos - 1
    insertionsort ( arr, start+1, n)
    return arr

print(" enter an array: ")
arr1 = list(map(int, input().split()))
print("Resultent Array :")
print( insertionsort1( arr1 ) )

print(" enter an array: ")
arr2 = list(map(int, input().split()))
print("Resultent Array :")
print( insertionsort2( arr2, 1, len(arr2) ) )

#  T(n) = T(n-1)+T(n-1), T(1)=1