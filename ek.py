from turtle import*

p = Turtle()
a = 10

def el():
    p.fd(a*4)
    p.lt(60)
    p.fd(4*a)
    p.lt(60)
    p.fd(a*4)
    p.lt(60)
    p.fd(a*4)
    p.lt(120)
    p.fd(a*4)
    p.rt(60)
    p.fd(a*4)
    p.lt(120)

def kwiatek():
    p.rt(30)
    for i in range(6):
        p.pu()
        p.fd(a)
        p.pd()
        p.rt(60)
        el()
        p.lt(60)
        p.pu()
        p.bk(a)
        p.pd()
        p.lt(60)
        
        
kwiatek() 
    
    
