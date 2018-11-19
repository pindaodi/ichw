#!/usr/bin/env python3

"""planets.py: Description of how do planets move.

__author__ = "Changrui"
__pkuid__  = "1800011758"
__email__  = "706771104@qq.com"
"""
import turtle 
import math

Sun = turtle.Turtle()
s = turtle.Turtle()#shuixing#
j = turtle.Turtle()#jinxing#
h = turtle.Turtle()#huoxing#
d = turtle.Turtle()#diqiu#
m = turtle.Turtle()#muxing#
t = turtle.Turtle()#tuxing#

def planet(name,color,q):
    name.shape("circle")
    name.color(color)
    name.speed(0)
    name.penup()
    name.fd(q)#q is the distance between planet and the sun#
    name.pendown()

    
def orbit(name,a,i):#define the orbit#
    b=(a/2)
    x=a*math.cos(math.radians(i*4))
    y=b*math.sin(math.radians(i*4))
    name.goto(x,y)
    
def main():
    planet(Sun,"red",0)
    planet(s,"blue",50)
    planet(j,"yellow",100)
    planet(h,"black",150)
    planet(d,"pink",200)
    planet(m,"green",250)
    planet(t,"brown",350)   
    for i in range(10000):
        orbit(s,50,0.5*i)
        orbit(j,100,0.4*i)
        orbit(h,150,0.3*i)
        orbit(d,200,0.2*i)
        orbit(m,250,0.1*i)
        orbit(t,350,0.05*i)
    turtle.mainloop()                                 
                                                    

if __name__ == "__main__":
    main()
