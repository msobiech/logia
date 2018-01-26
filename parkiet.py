from turtle import *

def panel(a):
    p.begin_fill()
    p.fillcolor("salmon")
    for i in range(2):
        p.fd(5*a)
        p.lt(90)
        p.fd(a)
        p.lt(90)
    p.end_fill()

def panele(a):
    for i in range(4):
        panel()
        p.lt(90)
        p.fd(a)
        p.rt(90)
    p.rt(90)
    p.fd(a*4)
    p.lt(90)

def srodek(a):
    p.begin_fill()
    p.fillcolor("yellow")
    for i in range(4):
        p.fd(a)
        p.lt(90)
    p.end_fill()

def element(a):
    for i in range(4):
        panele(a)
        p.fd(9*a)
        p.lt(90)
    p.fd(a*5)
    p.lt(90)
    p.fd(a*4)
    srodek()
    p.rt(180)
    p.fd(a*4)
    p.rt(90)
    p.fd(a*5)
    p.lt(180)

def pas(



    
