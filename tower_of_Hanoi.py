def Hanoi (N, from_, to, alt):
    if(N != 0):
        Hanoi (N-1, from_, alt, to)
        print("element:", N, "from:", from_, "to:", to)
        Hanoi (N-1, alt, to, from_)


N = 3

Hanoi(N,1,3,2)