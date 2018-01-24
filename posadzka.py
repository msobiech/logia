from turtle import *
from math import sqrt

p = Turtle()
bok = 470*2

def element(a):
    for i in range(4):
        p.fd(a)
        p.rt(45)
        p.fd(a/sqrt(2))
        p.lt(90)
        p.fd(a/sqrt(2))
        p.rt(45)
        p.fd(a)
        p.lt(90)
    
    
def ramka(a):
    for i in range(2):
        p.fd(bok)
        p.lt(90)
        p.fd(12*a)
        p.lt(90)

def posadzka():
    a = bok/20
    p.pu()
    p.rt(90)
    p.fd(12*a/2)
    p.rt(90)
    p.fd(470)
    p.lt(180)
    p.pd()
    ramka(a)
    p.pu()
    p.fd(a/2)
    p.lt(90)
    p.fd(a/2)
    p.rt(90)
    p.pd()
    for i in range(3):
        for i in range(5):
            element(a)
            p.pu()
            p.fd(a*4)
            p.pd()
        p.pu()
        p.bk(a*(4+16))
        p.lt(90)
        p.fd(4*a)
        p.rt(90)
        p.pd()

tracer(0)
posadzka()
update()
    
