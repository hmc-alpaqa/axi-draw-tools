from mock_axidraw import AxiDraw

ad = AxiDraw()
ad.interactive()
ad.connect()

ad.moveto(1, 1)
ad.lineto(3.5, 1)
ad.lineto(3.5, 3.5)
ad.lineto(1, 3.5)
ad.lineto(1, 1)
ad.moveto(0, 0)

ad.disconnect()
