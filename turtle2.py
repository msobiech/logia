from turtle import *

p = Turtle()



a = 10

def ruch1():
    bierz1 = p.pos()
    p.pu()
    p.fd(a*2)
    p.rt(90)
    p.fd(a)
    bierz2 = p.pos()
    p.pd()
    p.goto(bierz1)
    p.goto(bierz2)
    p.seth(90)

def ruch2():
    bierz1 = p.pos()
    p.pu()
    p.rt(90)
    p.fd(a*2)
    p.lt(90)
    p.fd(a)
    bierz2 = p.pos()
    p.pd()
    p.goto(bierz1)
    p.goto(bierz2)
    p.seth(90)

def ruch3():
    bierz1 = p.pos()
    p.pu()
    p.rt(90)
    p.fd(a*2)
    p.rt(90)
    p.fd(a)
    bierz2 = p.pos()
    p.pd()
    p.goto(bierz1)
    p.goto(bierz2)
    p.seth(90)

def ruch4():
    bierz1 = p.pos()
    p.pu()
    p.lt(180)
    p.fd(a*2)
    p.lt(90)
    p.fd(a)
    bierz2 = p.pos()
    p.pd()
    p.goto(bierz1)
    p.goto(bierz2)
    p.seth(90)

def ruch5():
    bierz1 = p.pos()
    p.pu()
    p.lt(180)
    p.fd(a*2)
    p.rt(90)
    p.fd(a)
    bierz2 = p.pos()
    p.pd()
    p.goto(bierz1)
    p.goto(bierz2)
    p.seth(90)

def ruch6():
    bierz1 = p.pos()
    p.pu()
    p.lt(90)
    p.fd(a*2)
    p.lt(90)
    p.fd(a)
    bierz2 = p.pos()
    p.pd()
    p.goto(bierz1)
    p.goto(bierz2)
    p.seth(90)

def ruch7():
    bierz1 = p.pos()
    p.pu()
    p.lt(90)
    p.fd(a*2)
    p.rt(90)
    p.fd(a)
    bierz2 = p.pos()
    p.pd()
    p.goto(bierz1)
    p.goto(bierz2)
    p.seth(90)

def ruch8():
    bierz1 = p.pos()
    p.pu()

    p.fd(a*2)
    p.lt(90)
    p.fd(a)
    bierz2 = p.pos()
    p.pd()
    p.goto(bierz1)
    p.goto(bierz2)
    p.seth(90)

def droga(kd):
    p.lt(90)
    
    for ch in str(kd):
        print(str(ch))
        if ch == '1':
            ruch1()
        elif ch == '2':
            ruch2()
        elif ch == '3':
            ruch3()
        elif ch == '4':
            ruch4()
        elif ch == '5':
            ruch5()
        elif ch == '6':
            ruch6()
        elif ch == '7':
            ruch7()
        elif ch == '8':
            ruch8()

droga(12318) 
