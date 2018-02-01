from turtle import *
from math import sqrt

a = 480/24
p = Turtle()

def krzyzyk():
    b = sqrt(2)*a
    p.lt(45)
    p.fd(b)
    p.bk(b/2)
    p.rt(90)
    p.bk(b/2)
    p.fd(b)
    p.lt(45)
    p.pu()
    p.bk(a)
    p.pd()

def ramka():
    for i in range(4):
        p.fd(480)
        p.lt(90)
    for i in range(4):
        for i in range(24):
            krzyzyk()
            p.pu()
            p.fd(a)
            p.pd()
        p.lt(90)
    p.pu()
    p.fd(a)
    p.lt(90)
    p.fd(a)
    p.rt(90)
    p.pd()
    for i in range(4):
        p.fd(480-(a*2))
        p.lt(90)

    
    
    
    
    
