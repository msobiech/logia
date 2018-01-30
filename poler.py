
def poler(n):
    '''
    p1 = 0
    p2 = 0
    p11 = 0
    p22 = 0
    s1 = 0
    s2 = 0
    for ch in n:
        print(ch)
        if ch == "p":
            s1 = s1 - 1
            if s1 < p11:
                p11 = s1
            elif s1 > p1:
                p1 = s1
        elif ch == "g":
            s2 = s2 - 1
            if s2 < p22:
                p22 = s2
            elif s2 > p2:
                p2 = s2
        elif ch == "l":
            s1 = s1 + 1
            if s1 < p11:
                p11 = s1
            elif s1 > p1:
                p1 = s1
        elif ch == "d":
            s2 = s2 + 1
            if s2 < p22:
                p22 = s2
            elif s2 > p2:
                p2 = s2
        p1 = abs(p1)
        p11 = abs(p11)
        p2 = abs(p2)
        p22 = abs(p22)
        p111 = p1 + p11
        p222 = p2 + p22
        '''
    g = 0
    d = 0
    p = 0
    l = 0
    s1 = 0
    s2 = 0
    for ch in n:
        if ch == "g":
            g = g + 1
        elif ch == "d":
            d = d + 1
        elif ch == "p":
            p = p + 1
        elif ch == "l":
            l = l + 1
    s1 = abs((p+l)-abs(p-l)-abs(l-p))
    s2 = abs((g+d)-abs(g-d)-abs(d-g))
    suma = s1*s2
    return suma

print(poler("ggdp"))
