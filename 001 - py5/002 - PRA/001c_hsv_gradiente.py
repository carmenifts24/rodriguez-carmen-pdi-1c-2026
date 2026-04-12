import py5


def setup():
    py5.size(720, 240)
    py5.color_mode(py5.HSB, 360, 100, 100)
    py5.no_stroke()
    py5.no_loop()


def draw():
    py5.background(0, 0, 15)

    # Recorremos toda la ventana y cambiamos el tono segun la posicion x.
    for x in range(py5.width):
        tono = py5.remap(x, 0, py5.width, 0, 360)
        py5.fill(tono, 80, 90)
        py5.rect(x, 0, 1, py5.height)

    # Este rectangulo central usa un tono fijo para comparar con el fondo.
    py5.fill(210, 40, 35)
    py5.rect(285, 70, 150, 100)


py5.run_sketch()
