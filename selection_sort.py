def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if j == i+1 :
                min_ind = j
            if arr[j] < arr[min_ind]:
                min_ind = j
        if arr[i] > arr[min_ind]:
            arr[min_ind], arr[i] = arr[i], arr[min_ind]
    return arr
            

arr = [4, 9, 11, 8, 7, 6]

print(selection_sort(arr))