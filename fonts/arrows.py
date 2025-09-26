from pyaxidraw import axidraw   # import module

# from mock_axidraw import AxiDraw
# from time import sleep



STEPSIZE = 0.07
LINESKIP = 3.5 * STEPSIZE

def read_lines(path: str) -> list[str]:
    """
    Read a text file and return its lines as a list of strings (no trailing newlines).
    """
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()



def draw_from_string(ad, instructions, step=STEPSIZE, half_step=STEPSIZE/2):
    directions = {
        '↑': (0, -step),
        '→': (step, 0),
        '↓': (0, step),
        '←': (-step, 0),
        '.↑': (0, -half_step),
        '.→': (half_step, 0),
        '.↓': (0, half_step),
        '.←': (-half_step, 0),
    }

    i = 0
    while i < len(instructions):
        ch = instructions[i]
        print(ch)
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

def write_string(ad, word):
    for char in word:
        print(char)
        cmds = char_code[char]
        draw_char(ad, cmds)

def draw_char(ad, description):
    draw_from_string(ad, description)
    ad.penup()
    ad.go(0.05,0)

ad = axidraw.AxiDraw()          # Initialize class
ad.interactive()                # Enter interactive context
if not ad.connect():            # Open serial port to AxiDraw;
    quit()                      #   Exit, if no connection.

# ad = AxiDraw(draw_delay=0.1)
# ad.interactive()
# ad.connect()

# Sample drawing string

char_code = {"a" : "↥↑↧→↓←.↑→↥.↓",
"b" : "↥↑↑↧↓↓→↑←↥→↓",
"c" : "↥→↧←↑→↥↓",
"d" : "↥↑↑→↧↓↓←↑→↥↓",
"e" : "↥→↧←↑→.↓←↥.↓→",
"f" : "↥.→↧↑↑.→↥←↓↧→↥↓",
"g" : "↥→↧←↑→↓↓←↥→↑",
"h" : "↧↑↑↥↓↧→↓",
"i" : "↥.→↧↑↥.↑↧↥.↓↓.→",
"j" : "↥.→↑.↑↧↥.↓↧↓↓.←↥.→.→↑",
"k" : "↥↧.↑↑↥↓↧→↥.←.↑↧.↓↥.→↧.↓↥",
"l" : "↥↑↑↧↓↓.→↥.→",
"m" : "↧↑.→↓↥↑↧.→↓",
"n" : "↧↑→↓",
"o" : "↧↑→↓←↥→",
"p" : "↧→↑←↓↓↥↑→",
"q" : "↥→↧←↑→↓↓↥↑",
"r" : "↥↧↑→↥↓",
"s" : "↥↧→.↑←.↑→↥↓",
"t" : "↥→↧.←↑↑↥.←↓↧→↥↓",
"u" : "↥↑↧↓→↑↥↓",
"v" : "↥↑↧↓.→↑.→↥↓",
"w" : "↥↑↧↓.→↑↥↓↧.→↑↥↓",
"x" : "↥↧→.↑↥.↑↧←.↓↥.→.↑↧↓↥.→",
"y" : "↥↑↧↓→↓←↥→↑↑↧↓",
"z" : "↥↥↑↧→.↓←.↓→",
"A" : "↥↧↑↑→↓↓↥↑←↧→↥↓",
"B" : "↥↧↑↑.→↓↥.←↧→↓←↥→",
"C" : "↥→↑↑↧←↓↓→↥",
"D" : "↥↧↑↑→↓↓←↥→",
"E" : "↥↧↑↑→↥↓↧←↥↓↧→",
"F" : "↥↧↑↑→↥↓↧←↥↓→",
"G" : "↥↑↑→↧←↓↓→↑.←↥.→↓",
"H" : "↥↧↑↑↥→↧↓←↥→↧↓",
"I" : "↥↧→↥.←↧↑↑.←↥.→↧.→↥↓↓",
"J" : "↥↧→↑↑↥↓↓",
"K" : "↥↧↑↑↥↓↧.→.↑↥.↓↧.→↧↓",
"L" : "↥↑↑↧↓↓→↥",
"M" : "↥↧↑↑.→↓↥↑↧.→↓↓↥",
"N" : "↥↧↑↑↥.↓↧.→↓.→↥↑.↑↧↓↓↥",
"O" : "↥↧↑↑→↓↓←↥→",
"P" : "↥↧↑↑→↓←↥→↓",
"Q" : "↥↧↑↑→↓↓←↥→↧.↓.↑↥",
"R" : "↥↧↑↑→↓←↥.→↧.↓.→↧.↓↥",
"S" : "↥↧→↑←↑→↥↓↓",
"T" : "↥.→↧↑↑↥.←↧→↥↓↓",
"U" : "↥↑↑↧↓↓→↑↑↥↓↓",
"V" : "↥↑↑↧↓.→.↓.→↥.↑↑↧↓↓↥",
"W" : "↥↑↑↧↓↓.→↑↥↓↧.→↑↑↥↓↓",
"X" : "↥↑↑↧.↓→.↑↥.←.↓↧↓↥.←.↓↧.↑→.↓↥",
"Y" : "↥↑↑↧↓→↑↥.←↓↧↓↥.→",
"Z" : "↥↑↑↧→.↓.←.↓.←↓→",
" " : "↥→",
"." : "↥.→↧↥.→",
"," : "↥.→↧.↓↥.↑.→",
";" : "↥.→.↑↧↥.↓↧.↓↥.↑.→",
":" : "↥.→↧↥.↑↧↥.↓.→",
"[" : "↥↑↑.→↧.←↓↓.→↥.→",
"]" : "↥↑↑.→↧.→↓↓.←↥.→",
"(" : "↥↑↑.→↧.←↓↓.→↥.→",
")" : "↥↑↑.→↧.→↓↓.←↥.→",
"!" : "↥.→↧↥.↑↧.↑↑↥↓↓.→",
"_" : "↥↧→↥",
"-" : "↥↑↧→↥↓",
"=" : "↥↑↧→↥←.↓↧→↥.↓",
"+" : "↥↑↧→↥.←.↑↧↓↥.↓.→",
"|" : "↥↑↑.→↧↓↓↥.→",
'"' : "↥↑↑.→↧.↓↥.↑.→↧.↓↥.↓↓",
"'" : "↥↑↑.→↧.↓↥.↓↓.→",
"1" : "↥↑↑↧.→↓↓↥.←↧→↥",
"2" : "↥↑↑↧→↓←↓→↥",
"3" : "↥↧→↑↑←↥↓↧→↥↓",
"4" : "↥↑↑↧↓→↥↑↧↓↓↥",
"5" : "↥↧→↑←↑→↥↓↓",
"6" : "↥↑↧→↓←↑↑→↥↓↓",
"7" : "↥↑↑↧→↓↓↥",
"8" : "↥↧→↑↑←↓↓↥↑↧→↥↓",
"9" : "↥↧→↑↑←↓→↥↓",
"0" : "↥↧→↑↑←↓↓↥↑.→↧↥.→↓",
"@" : "↥↧↑→↓.←.↑.→↥.↓",
"#" : "↥.→↧↑.↑↥.→↧.↓↓↥.←.←.↑↧.→→↥.↑↧←.←↥→.→↓",
"$" : "↥.↑↧.↓→↑←.↑→↥.↑.←↧↓↓.↓↥.→.↑",
"*" : "↥.↑↧↑↥.→↧↓↥.→↧↑↥←.↓↧→↥↓",
"^" : "↥↑↧.↑.→.↑↥.↓↧.→.↓↥↓",
"%" : "↥.↑.→↧↑↥.←↧↥→↓↧↥.↓",
"{" : "↥↑↧.→↥↑.→↧.←↓↓.→↥",
"}" : "↥↧.→↑↑.←↥↓.→↧.→↥↓",
"~" : "↥↑↧→.↓↧↥.↓"}




# write_string(ad, "Don't you, foreget about me...")

# ad.moveto(0,2)
# write_string(ad, "Never gonna give you up, ")

# ad.moveto(0,2.5)
# write_string(ad, "Never gonna let you down!:;[]()+-_ ")

# draw_char(ad, char_code["k"])
# draw_char(ad, char_code["x"])




text_lines = ["About Me ",
"My name ",
" ",
"is Lucas(Bang): ",
"    he = him(I, 'am', an='Associate-Professor').in() ",
"    the Department.of(Computer Science+|at+|[Harvey Mudd], College) ",
" ",
"More information(is): ",
"    available in(my, 'CV', Lucas='Bang-CV') PDF Teaching: ",
"        I = am.on() ",
"    sabbatical for.the(2024'2025+', academic) ",
" ",
" ",
"year I(have, taught): ",
"    Programming = Languages(CS) ",
"    131 = [] ",
"    Minds Brains and Programs: ",
"        COGS 123.NEUR(125'Data+', Structures): ",
"            Program: ",
"                Development.CS(70(Applied)) ",
"            Logic and: ",
"                Automated.Reasoning(CS) ",
"        181U: ",
"            Software.Verification(HMC) ",
"    CS181F Scholarship ",
" ",
" ",
"In my == 'research': ",
"    I = apply('principles.from')         ",
"    combinatorics = and('information.theory') ",
"    to = program(analysis, problems) ",
"    You = ''.can(find) ",
"    out(more) "]

text_lines = ["Don't you, forget about me...",
    "Never gonna give you up, ",
    "Never gonna let you down!:;[]()+-_ ",
    "1234567890!@#$%^*",
    "the quick red fox jumps over the",
    "lazy brown dog!"]



y_pos = LINESKIP 
ad.moveto(0, y_pos)
for line in text_lines:
    write_string(ad, line)
    y_pos = y_pos + LINESKIP
    ad.moveto(0, y_pos)


# chars = ["↥.→↧↑↥↓.→","↥.→↑↧↓↓.←↥.→↑.→","↥→↧←↑→↓↓↥↑","↥↧↑→↥↓","↥↧→.↑←.↑→↥↓","↥↑↧↓→↑↥↓"]

# chars_a_i = [h,e,l,l,o,o,w,o,r,l,d]
# chars_j_s  = [j,l,m,n,o,p,q,r,s]
# chars_t_z = [t,u,v,w,y,z]


# new_chars = read_lines("patterns.txt")

# for c in chars:
#     draw_char(ad, c)


# for c in chars_a_i:
#     draw_char(ad, c)

# ad.moveto(0,2)


# for c in chars_j_s:
#     draw_char(ad, c)

# ad.moveto(0,3)


# for c in chars_t_z:
#     draw_char(ad, c)



ad.moveto(0,0)

ad.disconnect()


# next_char = "↥→↧←↑→↓↓↥↑"
# 
# 
# 
# # draw_char(ad, a)
# # draw_char(ad, b)
# draw_char(ad, c)
# draw_char(ad, d)
# draw_char(ad, e)
# draw_char(ad, f)
# draw_char(ad, g)
# 
# 
# draw_char(ad, h)
# draw_char(ad, l)
# draw_char(ad, m)
# draw_char(ad, n)
# draw_char(ad, o)
# 
# ad.moveto(0,3)
# 
# 
# draw_char(ad, p)
# draw_char(ad, t)



# draw_char(ad, next_char)

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


