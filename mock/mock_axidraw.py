import turtle
import time

class AxiDraw:
    def __init__(self, draw_delay=0.2):
        self.screen = turtle.Screen()
        self.screen.setup(width=800, height=800)
        self.bounds = (0, 0, 10, 10)  # xmin, ymin, xmax, ymax
        self.screen.setworldcoordinates(*self.bounds)
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()
        self.pen.penup()
        self.interactive_mode = False
        self.draw_delay = draw_delay
        self.physical_position = (0.0, 0.0)  # Clipped position

    def interactive(self):
        self.interactive_mode = True

    def connect(self):
        return True

    def disconnect(self):
        self.screen.exitonclick()

    def pendown(self):
        self.pen.pendown()

    def penup(self):
        self.pen.penup()

    def _delay(self):
        time.sleep(self.draw_delay)

    def _clip_to_bounds(self, x, y):
        xmin, ymin, xmax, ymax = self.bounds
        return (
            min(max(x, xmin), xmax),
            min(max(y, ymin), ymax)
        )

    def _move_to(self, x, y):
        self.pen.goto(x, y)
        self._delay()

    def current_pos(self):
        return self.physical_position

    def turtle_pos(self):
        return self.pen.position()

    # Absolute commands
    def goto(self, x, y):
        self._move_to(x, y)
        self.physical_position = self._clip_to_bounds(x, y)

    def moveto(self, x, y):
        self.penup()
        self._move_to(x, y)
        self.physical_position = self._clip_to_bounds(x, y)

    def lineto(self, x, y):
        self.pendown()
        self._move_to(x, y)
        self.physical_position = self._clip_to_bounds(x, y)

    # Relative commands
    def go(self, dx, dy):
        x, y = self.pen.position()
        new_x, new_y = x + dx, y + dy
        self._move_to(new_x, new_y)
        self.physical_position = self._clip_to_bounds(new_x, new_y)

    def move(self, dx, dy):
        self.penup()
        self.go(dx, dy)

    def line(self, dx, dy):
        self.pendown()
        self.go(dx, dy)
