# T="01010101010101001010101010111100001100"
# P="01011110"
# P="12345"
# T="12345678"
T="qwertyuiopasdfghjklzxcvbnm"
P="assdfguio"
def naive(T,P):
    n = len(T)
    m = len(P)
    print(m)
    for i in range(1,m+1):
        for p in range(0,m-i+1):
            for s in range (0,n-i+1):
                # print(i,p,s, "p", P[p:p+i],"t", T[s:s+i])
                if P[p:p+i] == T[s:s+i]:
                    max_ = P[p:p+i]
    if max_:
        print(max_)
    else:
        print("not found")

naive(T,P)
