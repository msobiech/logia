from math import*

def losuj(slowo,ile):
    sl = []
    for i in range(ile):
        sl = []
        for ch in slowo[::-1]:
            sl.append(ch)
            
        
    return ''.join(sl)


print(losuj("abra",3))
