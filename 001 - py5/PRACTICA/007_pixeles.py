"""muestra cómo cargar una imagen, recorrer sus píxeles, invertir sus colores y mostrar el resultado en pantalla. 
Además, permite guardar la imagen procesada presionando la tecla s.

Qué hace en general:

carga una imagen desde img/imagen.jpg
recorre todos sus píxeles
invierte los valores de rojo, verde y azul
muestra la imagen invertida en la ventana
permite guardarla como archivo nuevo"""


import py5

img = None


def setup():
    global img
    py5.size(400, 400)
    py5.background(255)

    # Verificar que la imagen existe
    try:
        img = py5.load_image("img/paisaje.jpg")
    except:
        print("⚠️  Error: Coloca una imagen en la carpeta 'img/imagen.jpg'")
        return

    # Procesar imagen en setup DESPUÉS de configurar el contexto
    if img is not None:
        procesar_imagen()


def procesar_imagen():
    """Procesa la imagen invirtiendo colores"""
    global img

    print("Procesando imagen...")

    img.load_pixels()

    for i in range(len(img.pixels)):
        # Obtener color actual
        c = img.pixels[i]

        # Extraer componentes
        r = py5.red(c)
        g = py5.green(c)
        b = py5.blue(c)

        # Invertir y asignar
        #Cómo funciona la inversión:
        #si un canal vale 255, pasa a 0
        #si vale 0, pasa a 255
        #si vale 100, pasa a 155
        img.pixels[i] = py5.color(255 - r, 255 - g, 255 - b)

    img.update_pixels() #Actualiza la imagen con los nuevos colores.
    print("✓ Imagen procesada")


def draw():
    py5.background(255)

    if img is not None:
        py5.image(img, 0, 0, py5.width, py5.height)#Si la imagen existe, la dibuja ocupando toda la ventana.
    else:
        py5.fill(255, 0, 0)
        py5.text("Error: Imagen no encontrada", 50, 200)


def key_pressed():
    if py5.key == "s" and img is not None:
        img.save("imagen_invertida.jpg")
        print("💾 Imagen guardada como 'imagen_invertida.jpg'")


if __name__ == "__main__":
    py5.run_sketch()



# Carga una imagen, invierte sus colores pixel por pixel y la muestra en pantalla.
# Si la tecla presionada es "s", guarda la imagen procesada.
# Recorre todos los pixeles de la imagen y calcula su color invertido.
