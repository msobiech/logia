from math import*

def bieg (tempo):
    suma = 0
    p = 0
    for ch in str(tempo)[::-1]:
        if ch == p:
            suma = suma+1
        p = ch
        print(ch)  
    return print(suma)

def bieg2(tempo):
    suma = 0
    p = 0
    while tempo > 0:        
        if tempo%10 == p:
            suma = suma + 1
        p = tempo%10
        tempo = int(tempo/10)
    return print(suma)

bieg2(653327778)
