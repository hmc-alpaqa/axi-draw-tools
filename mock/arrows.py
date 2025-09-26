from mock_axidraw import AxiDraw
from time import sleep

def draw_from_string(ad, instructions, step=1.0, half_step=0.5):
    directions = {
        '↑': (0, step),
        '→': (step, 0),
        '↓': (0, -step),
        '←': (-step, 0),
        '.↑': (0, half_step),
        '.→': (half_step, 0),
        '.↓': (0, -half_step),
        '.←': (-half_step, 0),
    }

    i = 0
    while i < len(instructions):
        ch = instructions[i]

        # Handle half-step notation
        if ch == '.' and i + 1 < len(instructions):
            i += 1
            dir = '.' + instructions[i]
        else:
            dir = ch

        if dir == '↥':
            ad.penup()
        elif dir == '↧':
            ad.pendown()
        elif dir in directions:
            dx, dy = directions[dir]
            ad.go(dx, dy)
        else:
            print(f"Unknown instruction: {dir}")
        i += 1

def draw_char(ad, description):
    draw_from_string(ad, description)
    ad.penup()
    ad.go(0.5,0)

ad = AxiDraw(draw_delay=0.1)
ad.interactive()
ad.connect()

ad.go(0,7)
# Sample drawing string
a = "↥↑↧→↓←.↑→↥.↓"
b = "↥↑↑↧↓↓→↑←↥→↓"
c = "↥→↧←↑→↥↓"
d = "↥↑↑→↧↓↓←↑→↥↓"
e = "↥→↧←↑→.↓←↥.↓→"
f = "↥.→↧↑↑.→↥←↓↧→↥↓"

t = "↥→↧.←↑↑↥.←↓↧→↥↓"
g = "↥→↧←↑→↓↓←↥→↑"
h = "↧↑↑↥↓↧→↓"
l = "↥↑↑↧↓↓.→↥.→"
m = "↧↑.→↓↥↑↧.→↓"
n = "↧↑→↓"
o = "↧↑→↓←↥→"
p = "↧→↑←↓↓↥↑→"

next_char = "↥→↧←↑→↓↓↥↑"

draw_char(ad, a)
draw_char(ad, next_char)

# 
# ↧↑→↥↓
# ↧→.↑←.↑→↥↓
# ↥.→↑↑↧↓↓.→↥↑.↓←




# draw_char(ad, a)
# draw_char(ad, b)
# draw_char(ad, c)
# draw_char(ad, d)
# draw_char(ad, e)
# draw_char(ad, f)


ad.disconnect()
