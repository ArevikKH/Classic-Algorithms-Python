def add_polynomials(A, B):
    m = len(A)
    n = len(B)
    max_length = max(m, n)
    summation = [0] * max_length

    for i in range(max_length):
        if i < m and i < n:
            summation[i] = A[i] + B[i]
        elif i < m:
            summation[i] = A[i]
        else:
            summation[i] = B[i]

    return summation

A = [3,4,5]
B = [9,0,3,4]

sum_ = add_polynomials(A, B)
print(sum_)