# main.py
"""
Draws a text file line-by-line using the AxiDraw plotter and symbolic character motion codes.
Each character is defined as a series of pen-up/down and movement instructions.
"""

import argparse
from pyaxidraw import axidraw
from char_codes import char_code

# Default drawing parameters
DEFAULT_STEPSIZE = 0.08  # Default distance for a full directional move (in inches)


def read_lines(path: str) -> list[str]:
    """
    Read a UTF-8 text file and return its lines as a list of strings, stripped of newline characters.
    """
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()


def draw_from_string(ad, instructions: str, step: float, half_step: float):
    """
    Execute a symbolic movement string on the AxiDraw plotter.
    Supports full and half directional steps, plus pen-up (↥) and pen-down (↧) commands.
    """
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
        # Handle half-step notation like '.↑'
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
            print(f"[Warning] Unknown instruction: {dir}")

        i += 1


def draw_char(ad, symbol: str, step: float, half_step: float):
    """
    Draw a single character using its symbolic command sequence.
    """
    print(symbol)
    if symbol not in char_code:
        print(f"[Warning] No drawing instructions for character: '{symbol}'")
        return
    draw_from_string(ad, char_code[symbol], step, half_step)
    ad.penup()
    ad.go(0.75 * step, 0)  # Space between characters


def write_string(ad, text: str, step: float, half_step: float):
    """
    Draw a string of characters using AxiDraw.
    """
    for char in text:
        draw_char(ad, char, step, half_step)


def plot_file(filename: str, step_size: float):
    """
    Read lines from a file and draw them sequentially on the AxiDraw.
    """
    line_skip = 4 * step_size
    half_step = step_size / 2

    lines = read_lines(filename)

    ad = axidraw.AxiDraw()
    ad.interactive()
    if not ad.connect():
        print("[Error] Could not connect to AxiDraw.")
        return

    y_pos = line_skip * 2
    ad.moveto(0, y_pos)

    for line in lines:
        write_string(ad, line, step_size, half_step)
        y_pos += line_skip
        ad.moveto(0, y_pos)

    ad.moveto(0, 0)
    ad.disconnect()


def main():
    parser = argparse.ArgumentParser(description="Plot text using AxiDraw and symbolic instructions.")
    parser.add_argument("input_file", help="Path to input .txt file to draw")
    parser.add_argument("--step-size", type=float, default=DEFAULT_STEPSIZE,
                        help="Base step size for pen movement in inches (default: 0.08)")
    args = parser.parse_args()

    plot_file(args.input_file, step_size=args.step_size)


if __name__ == "__main__":
    main()
