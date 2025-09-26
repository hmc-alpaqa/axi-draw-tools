from mock_axidraw import AxiDraw

ad = AxiDraw()
ad.interactive()
ad.connect()

ad.go(1, 1)
ad.pendown()
ad.go(2.5, 0)
ad.go(0, 2.5)
ad.go(-2.5, 0)
ad.go(0, -2.5)
ad.penup()
ad.go(-1, -1)

ad.disconnect()
