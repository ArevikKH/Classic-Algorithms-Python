def table(P):
    l = {}
    m = len(P)
    for i in range(m):
        l[P[i]] = m - 1 - i
    l[P[m - 1]] = m
    return l

def Boyer_Moore(T, P):
    i = 0
    L = table(P)
    m = len(P)
    n = len(T)
    while i <= n - m:
        j = m - 1
        while j >= 0 and T[i + j] == P[j]:
            j -= 1
        if j == -1:
            print(f"Found at position {i}")
            k = 1

        char_to_shift = T[i + m - 1]

        if char_to_shift in L:
            bad_char_shift = L[char_to_shift]
        else:
            bad_char_shift = m

        i += max(1, j - bad_char_shift)
    if k != 1:
        return "fail"
    else:
        return "search is over"

T = "ADSghSFaaaSFa"
P = "SFa"

print(table(P))
print(Boyer_Moore(T, P))
