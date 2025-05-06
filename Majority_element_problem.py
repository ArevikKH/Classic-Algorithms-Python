def Majority_element(A):
    if len(A) == 1:
        return A[0]
    
    Left = [A[i] for i in range(0,len(A)//2)]
    Right = [A[i] for i in range(len(A)//2,len(A))]

    Left_Major = Majority_element(Left)
    Right_Major = Majority_element(Right)

    if Left_Major == Right_Major:
        return Left_Major
    
    Left_Major_count = Count(A, Left_Major)
    Right_Major_count = Count(A, Right_Major)

    if Left_Major_count > len(A)//2:
        return Left_Major
    elif Right_Major_count > len(A)//2:
        return Right_Major
    else:
        return "not fount"
    

def Count(A,major):
    c = 0
    for i in A:
       if i == major:
           c+=1
    return c 

A = [3,4,3,5,3,2,2,2,2,2]
print("Majority Element is", Majority_element(A))