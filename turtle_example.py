import turtle

def square(t, length):
    for i in range (4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    for i in range (n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    t.pu()
    t.fd(r)
    t.pd()
    circum = int((2 * 3.14 * r)/3)
    polygon(t, circum, 3)

def arc(t, r, a):
    t.pu()
    t.fd(r)
    t.pd()
    circum = (2 * 3.14 * r)
    print(circum)
    p = int(circum * a/360)
    print(p)
    polygon(t, p, 3)

    for i in range (p):
        t.fd(3)
        t.lt(360/n)


bob = turtle.Turtle()

# for k in range(3,15):
#     polygon(bob, k, 100)

#polygon(bob, length=100, n=5)
#circle(bob, 100)
arc(bob, 100, 100)

turtle.mainloop()


