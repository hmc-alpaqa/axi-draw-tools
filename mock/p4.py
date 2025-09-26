from mock_axidraw import AxiDraw

ad = AxiDraw()
ad.interactive()
ad.connect()

ad.move(1, 1)
ad.line(2.5, 0)
ad.line(0, 2.5)
ad.line(-2.5, 0)
ad.line(0, -2.5)
ad.move(-1, -1)

ad.disconnect()
