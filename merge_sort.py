A = [4, 9, 11, 8, 7, 6, 2, 1, 12]

"""unsuccessful attempt using 
   pseudocde from slide"""

# low = 0
# high = len(A)

# def Merge_sort(A, low, high):
#     if low < high:
#         mid=(low+high)//2
#     Merge_sort(A, low, mid)
#     Merge_sort(A, mid+1, high)
#     Merge(A, low, mid, high)
# #mid=q, low = p, high = r
# def Merge(A, low, mid, high):
#     n1=mid-low+1
#     n2=high-mid
#     K=[i for i in range(low,n1+1)]
    

def Merge_sort(A):
    if len(A) <= 1:
        return A
    
    Left = [A[i] for i in range(0,len(A)//2)]
    Right = [A[i] for i in range(len(A)//2,len(A))]

    Left = Merge_sort(Left)
    Right = Merge_sort(Right)

    return Merge(Left, Right)



def Merge(Left, Right):
    New = []

    while Left and Right:
        if Left[0] > Right[0]:
           New.append(Right[0])
           Right.pop(0)
        else:
            New.append(Left[0])
            Left.pop(0)  
    
    while Left:
        New.append(Left[0])
        Left.pop(0)

    while Right:
        New.append(Right[0])
        Right.pop(0)  

    return New      



print(Merge_sort(A))
