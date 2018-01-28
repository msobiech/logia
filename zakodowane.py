def zakoduj(wyraz):
    zakodowany = []
    for ch in wyraz:
        if ch == "a":
            zakodowany.append("f")
        elif ch == "b":
            zakodowany.append("h")
        elif ch == "c":
            zakodowany.append("v")
        else:
            zakodowany.append(ch)

    return "".join(zakodowany)

print(zakoduj("abcy"))


            
