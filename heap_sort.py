
# def heap(arr):
#      i = 0
#      while i - len(arr) !=  0:
#          print(arr)
#          max_ = max(arr[:len(arr)-i])
#          arr.remove(max_)
#          arr.append(max_)
#          i += 1
#      return arr[::-1]

def heapify(arr, n, i):
    print(arr)
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2 
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] 
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)


arr = [4, 9, 11, 8, 7, 6]

# print(heap(arr))

heap_sort(arr)
