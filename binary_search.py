A = [6, 13, 24, 25, 33, 43, 51, 53]
key = 33
low = 0
high = len(A)

def Find(A, key, low, high):
    mid=(low+high)//2
    if A[mid] == key:
        return True, A[mid], mid
    if low >= high:
        return False
    elif A[mid]>key:
        return Find(A,key,mid-1,low)
    else:
         return Find(A, key, high, mid-1)

print(Find(A, key, low, high))


