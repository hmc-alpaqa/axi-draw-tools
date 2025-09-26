from mock_axidraw import AxiDraw

# ←↑→↓ ↥↧
	
"↥↑↧→↓←.↑→↥.↓"

pen up
go up 1 unit 
pen down
go right 1 unit 
go down 1 unit 
go left 1 unit 
go up half unit
go right 1 unit 
pen up 
go down half unit  

# def a():
#     ad.go(0, 1)
#     ad.pendown()
#     ad.go(1, 0)
#     ad.go(0, -1)
#     ad.go(-1, 0)
#     ad.go(0, 0.5)
#     ad.go(1, 0)
#     ad.penup()
#     ad.go(-1, -1)

# L = "←" 

unit = 1;

# ▵
# ▵
# ▽

# a = "uu."




def mv(dir):
    if dir == "U":
        pen.move(0, unit)
    elif dir == "D":
        pen.move(0, -unit)
    elif dir == "L":
        pen.move(-unit, 0)
    elif dir == "R":
        pen.move(unit, 0)
    else:
        pen.move(0,0)

def draw(dir):
    if dir == "U":
        pen.line(0, unit)
    elif dir == "D":
        pen.line(0, -unit)
    elif dir == "L":
        pen.line(-unit, 0)
    elif dir == "R":
        pen.line(unit, 0)
    else:
        pen.line(0,0)

def a():
    mv("U")
    mv("U")
    draw("R")
    draw("D")
    draw("D")
    draw("L")
    draw("U")
    draw("R")
    mv("D")

def b():
    mv("U")
    mv("U")
    mv("U")
    mv("U")
    draw("D")
    draw("D")
    draw("D")
    draw("D")
    draw("R")
    draw("U")
    draw("U")
    draw("L")
    mv("D")
    mv("D")
    mv("R")


pen = AxiDraw()
pen.interactive()
pen.connect()

pen.goto(0,6)

a()
mv("R")
b()

# ad.goto(1, 1)
# ad.pendown()
# ad.goto(3.5, 1)
# ad.goto(3.5, 3.5)
# ad.goto(1, 3.5)
# ad.goto(1, 1)
# ad.penup()
# ad.goto(0, 0)


# ad.moveto(1, 1)
# ad.lineto(3.5, 1)
# ad.lineto(3.5, 3.5)
# ad.lineto(1, 3.5)
# ad.lineto(1, 1)
# ad.moveto(0, 0)


# ad.go(1, 1)
# ad.pendown()
# ad.go(2.5, 0)
# ad.go(0, 2.5)
# ad.go(-2.5, 0)
# ad.go(0, -2.5)
# ad.penup()
# ad.go(-1, -1)


# ad.move(1, 1)
# ad.line(2.5, 0)
# ad.line(0, 2.5)
# ad.line(-2.5, 0)
# ad.line(0, -2.5)
# ad.move(-1, -1)

pen.disconnect()
