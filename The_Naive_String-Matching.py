# T="01010101010101001010101010111100001100"
# P="01011110"
P="12345"
T="345612345678"
def naive(T,P):
    n = len(T)
    m = len(P)
    for s in range (0,n-m):
        # print(P,T[s:s+m])
        if P == T[s:s+m]:
            return "pass" , s
    return "not found"


print(naive(T,P))
