import time

def timer(arr, function):
    start = time.time()
    function(arr)
    end = time.time()
    print(end-start)
    
arr = [4, 9, 11, 8, 7, 6]

#min to max
def insertion_sort_min(arr):
   for i in range(1, len(arr)):
      j = i
      value = arr[i] 
      while j > 0 and arr[j-1] > value:
         arr[j] = arr[j-1]
         j-=1
      arr[j] = value
      print(arr)
      
#max to min
def insertion_sort_max(arr):
    for i in range(1, len(arr)):
        j = i
        value = arr[i] 
        while j > 0 and arr[j-1] < value:  #changes
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = value
        print(arr)
        
print("insertion_sort min")        
timer(arr, insertion_sort_min)
arr = [4, 9, 11, 8, 7, 6]

print("insertion_sort max")        
timer(arr, insertion_sort_max)
arr = [4, 9, 11, 8, 7, 6]
