from turtle import *

p = Turtle()

def platek():
    for i in range(2):
        p.fd(60)
        p.rt(360/8)
        p.fd(60)
        p.rt(180-(360/8))

def czysc():
    p.begin_fill()
    p.color("white")
    for i in range(2):
        p.fd(60)
        p.rt(360/8)
        p.fd(60)
        p.rt(180-(360/8))
    p.end_fill()
        
def kwiatek(start,ile):
    for i in range(8):
        platek()
        p.rt(360/8)
    p.lt(90)
    p.rt(360/8*(start-1))
    for i in range(ile):
        czysc()
        p.rt(360/8)
    
        
kwiatek(3,4)
