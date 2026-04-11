import py5


def setup():
    py5.size(400, 400)
    py5.background(0)  # RGB -> Red (rojo), Green (verde), Blue (azul)
#En py5, background(0) significa negro.
#Si usaras background(255), sería blanco.
    print("py5 funcionando correctamente")


def draw():
#draw() es otra función especial de py5. A diferencia de setup(), se ejecuta una y otra vez, frame por frame, 
# mientras el sketch está abierto.
#Aunque aquí no cambien las posiciones ni el color, py5 vuelve a dibujar este contenido continuamente.
    py5.fill(90, 237, 221)
    py5.no_stroke()#Quita el borde de las figuras. O sea, la figura tendrá relleno, pero no contorno.
    py5.ellipse(200, 200, 100, 100)
    


py5.run_sketch()
