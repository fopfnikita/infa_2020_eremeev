import turtle as t

LENGTH = (20,20)

REFERENCE = {
    0 : [(1,0,1),(1,2,1),(0,2,1),(0,0,1)],
    1 : [(0,1,0),(1,0,1),(1,2,1)],
    2 : [(1,0,1),(1,1,1),(0,2,1),(1,2,1)],
    3 : [(1,0,1),(0,1,1),(1,1,1),(0,2,1)],
    4 : [(0,1,1),(1,1,1),(1,0,1),(1,2,1)],
    5 : [(1,0,1),(0,0,0),(0,1,1),(1,1,1),(1,2,1),(0,2,1)],
    6 : [(1,0,0),(0,1,1),(0,2,1),(1,2,1),(1,1,1),(0,1,1)],
    7 : [(1,0,1),(0,1,1),(0,2,1)],
    8 : [(1,0,1),(1,2,1),(0,2,1),(0,0,1),(0,1,0),(1,1,1)],
    9 : [(0,2,0),(1,1,1),(1,0,1),(0,0,1),(0,1,1),(1,1,1)]
}

def drawdigit(a):
    tupl = REFERENCE[a]
    pos = t.pos()
    for elem in tupl:
        t.penup()
        if(elem[2] == 1):
            t.pendown()
        t.goto(elem[0]*LENGTH[0]+pos[0], -(elem[1]*LENGTH[1])+pos[1])

def drawnumber(ls, offset=(0,0)):
    for i in range(0,len(ls)):
        t.penup()
        t.goto(1.5*i*LENGTH[0] - offset[0], 0 - offset[1])
        drawdigit(ls[i])

drawnumber([1,4,1,7,0,0],(50,0))

t.exitonclick()