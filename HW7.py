#HW7.py
#This program produces 3 differently sized circles
#By Eric Ontiveros

from graphics import *

def main():
    
    win =  GraphWin("3 circles", 500, 500)
    win.setCoords(0,0,1000,1000)
    #list x and y coordinates of each circle center
    centerx = [100,500,800]
    centery = [100,500,800]
    radius  = [50, 100, 200]
    
    for i in range(3):
        shapes(centerx[i], centery[i], radius[i], win)
        print()
                                   
def shapes(centerx, centery, radius, win):
   
    center = Point(centerx, centery)
    circ = Circle(center, radius)
    circ.setOutline("black")
    circ.setFill("yellow")
    circ.draw(win)

main()
