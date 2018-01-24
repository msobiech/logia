from turtle import *
from math import sqrt
from random import *
#15:42 -
p = Turtle()

def losuj():
    kolory = ["black"]#"yellow","green","brown","red","blue","pink","gray","magenta","lime")
    
    k = randint(0,len(kolory)-1)
    print(str(len(kolory)))
    return kolory[k]
        
    
def element(bok):
    for i in range(4):
        p.fd(bok)
        p.lt(90)
    p.fd(bok/2)
    p.lt(45)
    p.begin_fill()
    p.fillcolor(losuj())
    for i in range(4):
        p.fd(bok/sqrt(2))
        p.lt(90)
    p.end_fill()
    p.rt(45)
    p.bk(bok/2)
    

def trojkat(bok):
    p.begin_fill()
    p.fillcolor(losuj())
    p.fd(bok/2)
    p.lt(135)
    p.fd(bok/2/sqrt(2))
    p.lt(90)
    p.fd(bok/2/sqrt(2))
    p.lt(135)
    p.end_fill()

def element2(bok):
    for i in range(4):
        p.begin_fill()
        p.fillcolor(losuj())
        for i in range(4):
            p.fd(bok/4)
            p.lt(90)
        p.end_fill()
        p.fd(bok)
        p.lt(90)
    p.fd(bok/2)
    p.lt(90)
    p.fd(bok/2)
    p.rt(90)
    for i in range(4):
        trojkat(bok)
        p.lt(90)
    p.pu()
    p.rt(90)
    p.fd(bok/2)
    p.rt(90)
    p.fd(bok/2)
    p.lt(180)
    p.pd()

def pas(il,bok):
    if il == 0 or il == 2:
        element2(bok)
        p.fd(bok)
        element(bok)
        p.fd(bok)
        element2(bok)
        p.bk(bok*2)
    if il == 1:
        element(bok)
        p.fd(bok)
        element2(bok)
        p.fd(bok)
        element(bok)
        p.bk(bok*2)
        
    p.lt(90)
    p.fd(bok)
    p.rt(90)

def KT(bokl):
    p.pu()
    p.rt(90)
    p.fd(bokl/2)
    p.rt(90)
    p.fd(bokl/2)
    p.lt(180)
    p.pd()
    bok = bokl/3
    for i in range(3):
        pas(i,bok)
    
        
KT(400)
        
    
