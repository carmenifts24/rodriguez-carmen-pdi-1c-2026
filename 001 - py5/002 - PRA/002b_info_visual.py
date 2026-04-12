import py5


def setup():
    # Crea una ventana de 800 x 600 pixeles.
    py5.size(800, 600)

    # Evita que draw() se repita continuamente porque esta escena es estatica.
    py5.no_loop()

    # Muestra en la consola las dimensiones del lienzo y la cantidad total de pixeles.
    print(f"Ancho: {py5.width} pixeles")
    print(f"Alto: {py5.height} pixeles")
    print(f"Total de pixeles: {py5.width * py5.height}")


def draw():
    # Pinta el fondo con un color oscuro para que el contenido resalte.
    py5.background(18, 24, 38)

    # Dibuja un panel central como base visual para la informacion.
    py5.fill(38, 70, 120)
    py5.no_stroke()
    py5.rect(60, 60, py5.width - 120, py5.height - 120, 18)

    # Agrega un borde blanco para delimitar mejor el area del panel.
    py5.stroke(255)
    py5.stroke_weight(3)
    py5.no_fill()
    py5.rect(60, 60, py5.width - 120, py5.height - 120, 18)

    # Titulo breve que resume el objetivo del sketch.
    py5.fill(255)
    py5.text_size(26)
    py5.text("Información del lienzo", 80, 120)

    # Muestra el ancho, el alto y el total de pixeles dentro de la ventana.
    py5.text_size(20)
    py5.text(f"width: {py5.width} px", 80, 180)
    py5.text(f"height: {py5.height} px", 80, 220)
    py5.text(f"total: {py5.width * py5.height} pixeles", 80, 260)

    # Esta linea horizontal representa visualmente el ancho del lienzo.
    py5.stroke(255, 190, 90)
    py5.line(80, 320, py5.width - 80, 320)

    # Estas dos lineas pequenas forman la punta de una flecha.
    py5.line(py5.width - 100, 300, py5.width - 80, 320)
    py5.line(py5.width - 100, 340, py5.width - 80, 320)
    #py5.line(...): llama a la función que dibuja una línea
    # 80: coordenada x1, o sea donde empieza la línea en el eje horizontal
    # 320: coordenada y1, o sea donde empieza la línea en el eje vertical
    # py5.width - 80: coordenada x2, o sea donde termina la línea horizontalmente
    # 320: coordenada y2, o sea donde termina la línea verticalmente

    # Esta linea vertical representa visualmente el alto del lienzo.
    py5.stroke(90, 220, 255)
    py5.line(120, 340, 120, py5.height - 80)

    # Estas dos lineas pequenas completan la flecha del alto.
    py5.line(100, py5.height - 100, 120, py5.height - 80)
    py5.line(140, py5.height - 100, 120, py5.height - 80)

    # Etiquetas de color para identificar cada medida.
    py5.no_stroke()
    py5.fill(255, 190, 90)
    py5.text("ancho", py5.width - 170, 300)

    py5.fill(90, 220, 255)
    py5.text("alto", 140, py5.height - 120)


py5.run_sketch()
