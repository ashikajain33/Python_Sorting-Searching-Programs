arr = list(map(int, input().split()))
search=int(input("enter the searching number: "))
#iterative
low = 0
high = len(arr)-1
mid = ( low + high )//2
while arr[mid] != search :
    mid = ( low + high )//2
    if arr[mid] > search :
        high = mid-1
    else :
        low = mid+1
if arr[mid] == search :
    print("found number at ",mid)
else :
    print("number not found")

# recursive
def binary_search(arr, l, r, x) :
    if r >= l:
        mid= (r+l)//2
        if arr[mid] == x :
            return mid
        elif arr[mid] > x :
            return binary_search(arr, l ,mid-1, x)
        else :
            return binary_search( arr, mid+1, r, x)
    else :
        return -1
print( binary_search(arr, 0, len(arr)-1, search) )

""" Recurrance relation 
T(n)    = T(n/2) + 1 ,T(1)=1
T(n/2)  = T(n/4) + 2
T(n/4)  = T(n/8) + 3  .......
        = T(n/2^k) + k
    let n/2^k = 1
       2^k = n
       k = log (n) /log (2)  or log₂(n)
        = T(1) + log₂(n)
        = 1 + log₂(n)
T( n )  = O( log₂(n) )
"""


