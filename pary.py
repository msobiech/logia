def ilepar(liczba):
    p = 0
    suma = 0
    for ch in liczba:
        if ch == p :
            suma = suma +1
        p = ch

    return(suma)

print(ilepar("221123"))
        
