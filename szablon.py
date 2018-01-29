from turtle import *

p = Turtle()

def rzad(a,m):
    p.rt(60)
    for i in range(m):
        p.fd(a)
        p.lt(120)
        p.fd(a)
        p.rt(120)
    p.fd(a)
    p.rt(120)
    p.fd(a*m)
    p.lt(180)

def siatka(n):
    a = 50
    p.fd(a*n)
    p.lt(180)
    for i in range(n):
        rzad(a,n-i-1)
    p.lt(60)
    p.fd(n*a)
    p.lt(120)
    
siatka(5)
