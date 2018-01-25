from turtle import *
from math import sqrt
p = Turtle()
b = 300

def kwadrat(a,b):
    p.begin_fill()
    p.fillcolor("purple")
    for i in range(2):
        p.fd(a)
        p.lt(90)
        p.fd(b)
        p.lt(90)
    p.end_fill()

def romb(kolor,a):
    p.lt(45)
    p.begin_fill()
    p.color(kolor)
    for i in range(4):
        p.fd(a)
        p.lt(90)
    p.end_fill()
    p.rt(45)

def trojkat(a):
    p.begin_fill()
    p.color("green")
    p.fd(a)
    p.lt(135)
    p.fd(a/sqrt(2))
    p.lt(90)
    p.fd(a/sqrt(2))
    p.lt(135)
    p.end_fill()

    
def ramfio(a):
    
    for i in range(2):
        kwadrat(a/2,a/2)
        p.pu()
        p.fd(a*1.5)
        p.pd()
        for i in range(4):
            kwadrat(a,a/2)
            p.pu()
            p.fd(a*2)
            p.pd()
        p.fd(a/2)
        p.lt(90)
        kwadrat(a/2,a/2)
        p.pu()
        p.fd(a*1.5)
        p.pd()
        for i in range(2):
            kwadrat(a,a/2)
            p.pu()
            p.fd(a*2)
            p.pd()
        kwadrat(a/2,a/2)
        p.fd(a/2)
        p.lt(90)
        
def ramziel(a):
    for i in range(2):
        p.pu()
        p.fd(a/2)
        p.pd()
        for i in range(5):
            trojkat(a)
            p.pu()
            p.fd(a*2)
            p.pd()
        p.pu()
        p.bk(a/2)
        p.lt(90)
        p.fd(a/2)
        p.pd()
        for i in range(3):
            trojkat(a)
            p.pu()
            p.fd(a*2)
            p.pd()

        p.pu()
        p.fd(-a/2)
        p.lt(90)
        p.pd()

def pas1(a):
    for i in range(9):
        if i == 0 or i == 2 or i == 4 or i == 6 or i == 8:
            romb("purple",a/sqrt(2))
            p.pu()
            p.fd(a)
            p.pd()
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 9:
            romb("green",a/sqrt(2))
            p.pu()
            p.fd(a)
            p.pd()
            
def dywan():
    a = b/6
    ramfio(a)
    ramziel(a)
    p.pu()
    p.fd(a*1)
    p.lt(90)
    p.fd(a/2)
    p.rt(90)
    p.pd()
    for i in range(5):
        
        
    
    
        
