from pyaxidraw import axidraw   # import module
ad = axidraw.AxiDraw()          # Initialize class
ad.interactive()                # Enter interactive context
if not ad.connect():            # Open serial port to AxiDraw;
    quit()                      #   Exit, if no connection.


                                # Absolute moves follow:
ad.moveto(0, 0)                 # Pen-up move, back to origin.



for i in range(10):
    ad.moveto(1, 1 + i/2)                 # Pen-up move to (1 inch, 1 inch)
    ad.lineto(2, 1 + i/2)                 # Pen-down move, to (2 inch, 1 inch)
    ad.lineto(3, 1 + i/2)                 # Pen-down move, to (2 inch, 1 inch)
    ad.lineto(2, 2 + i/2)                 # Pen-down move, to (2 inch, 1 inch)
    ad.lineto(4, 1 + i/2)                 # Pen-down move, to (2 inch, 1 inch)


ad.moveto(0, 0)                 # Pen-up move, back to origin.


ad.disconnect()                 # Close serial port to AxiDraw
