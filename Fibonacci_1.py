def fib(n):
    f = [0, 1,1]
    if n<=0:
        return 0
    for i in range (3,n):
        f.append(f[i-2]+f[i-1])
    return f[n-1]
        
def fib_r(n):
    if n <=1:
        return 0
    elif n in (2,3):
        return 1
    return fib_r(n-1)+ fib_r(n-2)

#tests:
print(fib(-5))
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))

print(fib_r(-5))
print(fib_r(0))
print(fib_r(1))
print(fib_r(2))
print(fib_r(3))
print(fib_r(4))
