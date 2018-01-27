from turtle import*

cyfry = ["0","1","2","3","4","5","6","7","8","9"]
samogloski = ["a","e","i","o","u","y"]

litery_dol = ["g","j","p","q","y"]
litery_gora = ["b","d","f","h","k","l","t"]
p = Turtle()

def wys(a,kolor):
    p.begin_fill()
    p.fillcolor(kolor)
    for i in range(2):
        p.fd(a)
        p.lt(90)
        p.fd(a*2)
        p.lt(90)
    p.end_fill()
    p.fd(a)

def nis(a,kolor):
    p.begin_fill()
    p.fillcolor(kolor)
    for i in range(4):
        p.fd(a)
        p.lt(90)
    p.end_fill()
    p.fd(a)

def dol(a,kolor):
    p.lt(90)
    p.fd(a)
    p.rt(90)
    p.begin_fill()
    p.fillcolor(kolor)
    for i in range(2):
        p.fd(a)
        p.rt(90)
        p.fd(a*2)
        p.rt(90)
    p.end_fill()
    p.fd(a)
    p.rt(90)
    p.fd(a)
    p.lt(90)

def rysuj(s):
    a = 470/len(s)
    kolor = 0
    p.pu()
    p.bk(470/2)
    p.pd()
    for l in s:
        #wybor koloru
        if l in cyfry:
            kolor = "green"
        elif l in samogloski:
            kolor = "red"
        else:
            kolor = "yellow"
            
        #rysowanie
        if l in litery_gora or l in cyfry:
            wys(a,kolor)
        elif l in litery_dol:
            dol(a,kolor)
        else:
            nis(a,kolor)
        
        
rysuj("2krokodyle")
        
        
    
