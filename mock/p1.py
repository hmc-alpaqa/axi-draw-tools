from mock_axidraw import AxiDraw

ad = AxiDraw()
ad.interactive()
ad.connect()

ad.goto(1, 1)
ad.pendown()
ad.goto(3.5, 1)
ad.goto(3.5, 3.5)
ad.goto(1, 3.5)
ad.goto(1, 1)
ad.penup()
ad.goto(0, 0)

ad.disconnect()

