import py5


# Sketch tipo paint brush:
# permite dibujar con el mouse, cambiar el color del trazo,
# activar un borrador, cambiar el grosor, insertar figuras
# y limpiar el lienzo.

# Color actual del pincel.
brush_color = None
# Grosor actual del trazo.
brush_size = 12
# Indica si el borrador esta activo.
eraser_mode = False
# Color del fondo del lienzo.
background_color = 255
# Lista de colores disponibles.
palette = []
# Herramienta activa: pincel, rectangulo, circulo, triangulo o linea.
tool_mode = "pincel"
# Punto inicial para crear figuras al arrastrar el mouse.
shape_start = None


def setup():
    global brush_color, palette

    # Configura la ventana principal del sketch.
    py5.size(1000, 700)

    # Define el color inicial del lienzo.
    py5.background(background_color)

    # Ajusta el estilo general del trazo y del texto.
    py5.stroke_weight(brush_size)
    py5.stroke_cap(py5.ROUND)
    py5.text_align(py5.LEFT, py5.TOP)

    # Paleta de colores disponibles para el pincel.
    palette = [
        py5.color(0, 0, 0),        # negro
        py5.color(220, 50, 47),    # rojo
        py5.color(38, 139, 210),   # azul
        py5.color(133, 153, 0),    # verde
        py5.color(211, 54, 130),   # rosa
        py5.color(203, 75, 22),    # naranja
        py5.color(240, 200, 20),   # amarillo
    ]

    # El pincel empieza usando el primer color de la paleta.
    brush_color = palette[0]


def draw():
    # Panel superior con instrucciones y estado actual.
    py5.no_stroke()
    py5.fill(245, 245, 245)
    py5.rect(0, 0, py5.width, 90)

    py5.fill(30)
    py5.text_size(24)
    py5.text("Paint Brush en py5", 20, 16)

    py5.text_size(14)
    py5.text("Dibuja arrastrando el mouse", 20, 52)
    py5.text("Teclas 1-7: color | b: borrador | p: pincel | c: limpiar", 260, 18)
    py5.text("+ y -: grosor | s: guardar | r/o/t/l: figuras", 260, 42)

    py5.text(
        f"Herramienta: {'Borrador' if eraser_mode else tool_mode.title()}   "
        f"Grosor: {brush_size}",
        760,
        18,
    )

    py5.fill(brush_color if not eraser_mode else py5.color(255))
    py5.circle(940, 48, 28)

    # Muestra una paleta simple de referencia.
    for i, color_value in enumerate(palette):
        py5.fill(color_value)
        py5.circle(30 + i * 30, 84, 14)

    # Si hay una figura en proceso, muestra una vista previa mientras arrastras.
    if shape_start is not None and py5.is_mouse_pressed and py5.mouse_y > 90:
        py5.stroke(brush_color)
        py5.stroke_weight(max(2, brush_size // 3))
        py5.fill(brush_color, 120)
        draw_shape(shape_start[0], shape_start[1], py5.mouse_x, py5.mouse_y)


def mouse_dragged():
    # Evita dibujar sobre el panel de instrucciones.
    if py5.mouse_y <= 90 or py5.pmouse_y <= 90:
        return

    if tool_mode != "pincel":
        return

    py5.stroke_weight(brush_size)

    if eraser_mode:
        py5.stroke(background_color)
    else:
        py5.stroke(brush_color)

    py5.line(py5.pmouse_x, py5.pmouse_y, py5.mouse_x, py5.mouse_y)


def mouse_pressed():
    global shape_start

    # Ignora clics sobre el panel superior.
    if py5.mouse_y <= 90:
        return

    # Solo guarda un punto inicial cuando estamos en modo figura.
    if eraser_mode or tool_mode == "pincel":
        return

    shape_start = (py5.mouse_x, py5.mouse_y)


def mouse_released():
    global shape_start

    # Si no habia una figura en proceso, no hace nada.
    if shape_start is None:
        return

    # Si el mouse se suelta sobre el panel, cancela la figura.
    if py5.mouse_y <= 90:
        shape_start = None
        return

    # Dibuja la figura definitiva usando el punto inicial y final del arrastre.
    py5.stroke(brush_color)
    py5.stroke_weight(max(2, brush_size // 3))
    py5.fill(brush_color)
    draw_shape(shape_start[0], shape_start[1], py5.mouse_x, py5.mouse_y)

    # Limpia el estado para la siguiente figura.
    shape_start = None


def draw_shape(x1, y1, x2, y2):
    # Calcula medidas basicas a partir del arrastre del mouse.
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    shape_width = abs(x2 - x1)
    shape_height = abs(y2 - y1)

    # Si el arrastre es demasiado pequeno, usa un tamano minimo visible.
    shape_width = max(20, shape_width)
    shape_height = max(20, shape_height)

    if tool_mode == "rectangulo":
        py5.rect_mode(py5.CENTER)
        py5.rect(center_x, center_y, shape_width, shape_height)
        py5.rect_mode(py5.CORNER)
    elif tool_mode == "circulo":
        diameter = max(shape_width, shape_height)
        py5.circle(center_x, center_y, diameter)
    elif tool_mode == "triangulo":
        py5.triangle(
            center_x,
            center_y - shape_height / 2,
            center_x - shape_width / 2,
            center_y + shape_height / 2,
            center_x + shape_width / 2,
            center_y + shape_height / 2,
        )
    elif tool_mode == "linea":
        py5.line(x1, y1, x2, y2)


def key_pressed():
    global brush_color, eraser_mode, brush_size, tool_mode, shape_start

    # Seleccion de color con teclas numericas.
    if py5.key == "1":
        brush_color = palette[0]
        eraser_mode = False
        tool_mode = "pincel"
    elif py5.key == "2":
        brush_color = palette[1]
        eraser_mode = False
        tool_mode = "pincel"
    elif py5.key == "3":
        brush_color = palette[2]
        eraser_mode = False
        tool_mode = "pincel"
    elif py5.key == "4":
        brush_color = palette[3]
        eraser_mode = False
        tool_mode = "pincel"
    elif py5.key == "5":
        brush_color = palette[4]
        eraser_mode = False
        tool_mode = "pincel"
    elif py5.key == "6":
        brush_color = palette[5]
        eraser_mode = False
        tool_mode = "pincel"
    elif py5.key == "7":
        brush_color = palette[6]
        eraser_mode = False
        tool_mode = "pincel"
    elif py5.key == "b":
        eraser_mode = True
        shape_start = None
    elif py5.key == "p":
        eraser_mode = False
        tool_mode = "pincel"
        shape_start = None
    elif py5.key == "c":
        py5.background(background_color)
    elif py5.key == "-":
        brush_size = max(2, brush_size - 2)
    elif py5.key == "+":
        brush_size = min(60, brush_size + 2)
    elif py5.key == "s":
        py5.save_frame("save/paint_brush_####.png")
    elif py5.key == "r":
        eraser_mode = False
        tool_mode = "rectangulo"
        shape_start = None
    elif py5.key == "o":
        eraser_mode = False
        tool_mode = "circulo"
        shape_start = None
    elif py5.key == "t":
        eraser_mode = False
        tool_mode = "triangulo"
        shape_start = None
    elif py5.key == "l":
        eraser_mode = False
        tool_mode = "linea"
        shape_start = None


py5.run_sketch()
