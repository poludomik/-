from turtle import *
tracer(0)
screensize(10**4, 10**4)
m = 10
lt(90)
x = 29
for i in range(4):
    fd(x*m)
    rt(90)
    fd(48*m)
    rt(90)
up()
fd(27*m)
rt(90)
fd(24*m)
lt(90)
down()
for j in range(4):
    fd(29*m)
    rt(90)
    bk(18*m)
    rt(90)
up()
for k in range(-50, 50):
    for f in range(-10, 60):
        goto(k*m, f*m)
        dot(3, 'blue')
update()
