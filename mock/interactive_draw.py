import turtle
import tkinter as tk

# Store symbolic instructions
instructions = []
description_mode = False
description_buffer = []

# Create turtle screen and turtle
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.setworldcoordinates(0, 0, 10, 10)

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

marker = turtle.Turtle()  # Pen position indicator
marker.hideturtle()
marker.penup()
marker.speed(0)

# Constants
step = 1.0
half_step = 0.5
start_x, start_y = 4, 4

# Movement maps
full_moves = {
    'Up':    ('↑', 0, step),
    'Down':  ('↓', 0, -step),
    'Left':  ('←', -step, 0),
    'Right': ('→', step, 0),
}

half_moves = {
    'Up':    ('.↑', 0, half_step),
    'Down':  ('.↓', 0, -half_step),
    'Left':  ('.←', -half_step, 0),
    'Right': ('.→', half_step, 0),
}

# Drawing state
is_pen_down = False

def move(dx, dy):
    pen.goto(pen.xcor() + dx, pen.ycor() + dy)
    update_marker()

def draw(symbol, dx, dy):
    global is_pen_down
    if is_pen_down:
        pen.pendown()
    else:
        pen.penup()
    move(dx, dy)
    instructions.append(symbol)
    print_log(f"{symbol} → move by ({dx}, {dy})")

def print_log(message):
    state = "DOWN" if is_pen_down else "UP"
    print(f"{message} | Pen: {state}")


def update_marker():
    marker.clear()
    marker.goto(pen.xcor(), pen.ycor())
    if is_pen_down:
        marker.begin_fill()
        marker.dot(10, "black")  # filled black circle
        marker.end_fill()
    else:
        marker.dot(10, "white")  # white dot with black outline
        marker.pencolor("black")
        marker.fillcolor("white")
        marker.pendown()
        marker.circle(0.1)
        marker.penup()



# def update_marker():
#     marker.clear()
#     marker.goto(pen.xcor(), pen.ycor())
#     if is_pen_down:
#         marker.pendown()
#         marker.circle(0.1)
#         marker.penup()
#     else:
#         marker.begin_fill()
#         marker.circle(0.1)
#         marker.end_fill()

def key_handler(event):
    global is_pen_down, description_mode

    key = event.keysym
    shift = event.state & 0x0001
    ctrl  = event.state & 0x0004

    if description_mode:
        if key == 'Return':
            save_with_description()
        elif key == 'BackSpace':
            if description_buffer:
                description_buffer.pop()
        elif key == 'space':
            description_buffer.append(' ')
        elif len(key) == 1:
            description_buffer.append(key)
        return

    if key in full_moves:
        if shift:
            if key == 'Up':
                pen.penup()
                is_pen_down = False
                instructions.append('↥')
                print_log("↥ (pen up)")
                update_marker()
            elif key == 'Down':
                pen.pendown()
                is_pen_down = True
                instructions.append('↧')
                print_log("↧ (pen down)")
                update_marker()
        elif ctrl:
            symbol, dx, dy = half_moves[key]
            draw(symbol, dx, dy)
        else:
            symbol, dx, dy = full_moves[key]
            draw(symbol, dx, dy)

    elif key == 'Return':
        if instructions:
            print("Enter a short description for the pattern, then press Enter again:")
            description_mode = True
            description_buffer.clear()

    elif key.lower() == 'q':
        print("Quitting.")
        screen.bye()

    elif key.lower() == 's':
        print("Start over — pattern discarded.\n")
        discard_and_reset()

def save_with_description():
    global description_mode
    description = ''.join(description_buffer).strip()
    pattern_line = f"{description} {''.join(instructions)}\n"
    with open("patterns.txt", "a", encoding='utf-8') as f:
        f.write(pattern_line)
    print(f"Saved: {pattern_line.strip()}")
    instructions.clear()
    description_buffer.clear()
    description_mode = False
    pen.clear()
    marker.clear()
    pen.penup()
    pen.goto(start_x, start_y)
    update_marker()


# def save_with_description():
#     global description_mode
#     description = ''.join(description_buffer).strip()
#     pattern_line = f"{description} {' '.join(instructions)}\n"
#     with open("patterns.txt", "a", encoding='utf-8') as f:
#         f.write(pattern_line)
#     print(f"Saved: {pattern_line.strip()}")
#     instructions.clear()
#     description_buffer.clear()
#     description_mode = False
#     pen.clear()
#     marker.clear()
#     pen.penup()
#     pen.goto(start_x, start_y)
#     update_marker()

def discard_and_reset():
    instructions.clear()
    pen.clear()
    marker.clear()
    pen.penup()
    pen.goto(start_x, start_y)
    update_marker()

# Setup initial state
cv = screen.getcanvas()
cv.bind_all('<Key>', key_handler)
pen.goto(start_x, start_y)
update_marker()

# Welcome message
print("Use arrow keys to draw:")
print("- Arrow keys: full moves")
print("- Ctrl+arrow: half moves")
print("- Shift+Up = pen up (↥), Shift+Down = pen down (↧)")
print("- Press Enter to save to patterns.txt and reset")
print("- Press S to discard and start over")
print("- Press Q to quit")

# Start event loop
turtle.mainloop()
