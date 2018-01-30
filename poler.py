
def poler(n):

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
