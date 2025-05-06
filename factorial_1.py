def fac(n):
    f=1
    if n>=0:
        for i in range(1,n+1):
            f=f*i
    else: 
        f = "impossible"
    print(f)
fac(-3)

def fac_r(n):
    if n <0:
        return "impossible"
    elif n ==1 or n == 0:
        return 1
    else:
        return n*fac_r(n-1)

print(fac_r(0))
