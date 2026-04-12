import py5

img = None

def setup():
    global img
    # La ventana mide 800x400: 400 px para la imagen y 400 px para la vista ampliada.
    py5.size(800, 400)
    img = py5.load_image("img/imagen.jpg")  # Usa una imagen disponible en tu carpeta img/
    # Ajusta la imagen a un tamaño fijo para que las coordenadas sean predecibles.
    img.resize(400, 400)

def draw():
    # Limpia la ventana en cada cuadro para redibujar todo desde cero.
    py5.background(255)

    # Dibuja la imagen original en la mitad izquierda de la ventana.
    py5.image(img, 0, 0)

    # Versión original segura: constrain() limita el mouse al rango válido
    # de la imagen (0 a 399 en X y en Y) para evitar lecturas fuera de rango.
    # mx = py5.constrain(py5.mouse_x, 0, 399)
    # my = py5.constrain(py5.mouse_y, 0, 399)
    # En esta prueba se usa el mouse sin limitar para poder provocar el error
    # al salir del área de la imagen.
    mx = py5.mouse_x
    my = py5.mouse_y

    # Lee el color directamente desde la imagen de 400x400.
    # Si mx o my quedan fuera del rango válido, esta línea puede generar error.
    color_pixel = img.get_pixels(int(mx), int(my))

    # Alternativa original: leer desde el lienzo completo.
    # Queda comentada como referencia para comparar ambos comportamientos.
    # color_pixel = py5.get_pixels(int(mx), int(my))

    # Extraen cada canal de color por separado a partir del color compacto.
    r = py5.red(color_pixel)
    g = py5.green(color_pixel)
    b = py5.blue(color_pixel)

    # Establece el color de relleno para las figuras que se dibujen a continuación.
    # En este caso, el rectángulo toma exactamente el color del píxel leído.
    py5.fill(color_pixel)
    # Variante 1: muestra el negativo del color.
    # py5.fill(255 - r, 255 - g, 255 - b)
    # Variante 2: muestra solo la intensidad del canal rojo.
    # py5.fill(r, 0, 0)
    # Dibuja un borde negro para separar visualmente la muestra del fondo blanco.
    py5.stroke(0)
    py5.rect(450, 50, 300, 300)

    # Cambia el relleno a negro para escribir los textos con buen contraste.
    py5.fill(0)
    py5.text_size(18)
    # Muestra la posición del cursor dentro de la imagen y los valores RGB del píxel.
    py5.text(f"Posición: ({mx}, {my})", 450, 30)
    py5.text(f"R: {r:.0f}   G: {g:.0f}   B: {b:.0f}", 450, 380)

py5.run_sketch()
