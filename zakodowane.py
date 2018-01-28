def zakoduj(wyraz):
    zakodowany = []
    kody = {"a":"z", "b":"x", "c":"v"}
    for ch in wyraz:
        if ch in kody:
            zakodowany.append(kody[ch])
        else:
            zakodowany.append(ch)
        

    return "".join(zakodowany)

print(zakoduj("abcy"))


            
