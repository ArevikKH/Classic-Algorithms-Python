T = "01010101010101001010101010111100001100"
P = "01011110"
sigma_star = "01"

def delta_f(P, sigma_star):
    m = len(P)
    delta = [[0] * 2 for _ in range(m + 1)]  #  2 is sigma_star len
    
    for q in range(0, m + 1):
        for i in sigma_star:
            k = min(m + 1, q + 2) # երկարությունից դուրս չգա, հնարավորություն լինի +i անել
            while k > 0 and P[:k - 1] != (P[:q] + i)[-k + 1:]: # no matches - state=0
                k = k - 1
            delta[q][int(i)] = k  # Use int(i) to convert '0' or '1' to the corresponding index

    return delta

def automata(T, delta, m):
    n = len(T)
    q = 0
    for i in range(n):
        q = delta[q][int(T[i])]  # Use int(T[i]) to convert the character to the corresponding index
        if q == m:
            print("Pattern found at position", i - m + 1)

delta = delta_f(P, sigma_star)
m = len(P)
automata(T, delta, m)
print(delta_f(P, sigma_star))