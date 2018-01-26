from turtle import *
from math import *

p = Turtle()
wys = 150
samogloski = ["a","e","i","o","u","y"]

def kartka(kolor):
    p.begin_fill()
    p.fillcolor(kolor)
    for k in range(2):
        p.fd(150)
        p.lt(45)
        p.fd(150)
        p.lt(135)
    p.end_fill()
    
def kartki(wyraz):
    for litera in wyraz[::-1]:
        if litera in samogloski:
            kartka("black")
        else:
            kartka("white")
        p.lt(90)
        p.pu()
        p.fd(wys/len(wyraz))
        p.rt(90)
        p.pd()

tracer(0)
kartki("ala")
update()

        
