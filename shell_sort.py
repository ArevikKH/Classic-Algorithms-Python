def shell_sort(arr):
    n = len(arr)
    gap = n//2
    while gap>0:
        flag = True
        while flag:
            flag = False
            for i in range(n-gap):
                print(arr[i], arr[i+gap])
                if arr[i] > arr[i+gap]:
                    arr[i+gap], arr[i] = arr[i], arr[i+gap]
                    flag = True
                print(arr)
        gap = int(gap/2) 

arr = [4, 9, 11, 8, 7, 6, 5]

shell_sort(arr)        
