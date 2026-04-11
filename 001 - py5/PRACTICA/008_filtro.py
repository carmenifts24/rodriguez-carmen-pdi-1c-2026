# Crear un filtro que solo muestre un canal de color

"""muestra un ejemplo simple de filtro de color aplicado a una imagen. En este caso, 
primero se crea una imagen de prueba con colores aleatorios y luego se la dibuja varias veces 
para visualizar distintos canales de color mediante tint().

Qué hace en general:

crea una imagen de 200x200 píxeles
llena esa imagen con colores aleatorios
la muestra una vez original
la vuelve a mostrar con un tinte rojo
la vuelve a mostrar con un tinte verde"""
import py5

img = None


def setup():
    global img
    py5.size(600, 200)
    img = py5.create_image(200, 200, py5.RGB)
    #Crea una imagen vacía de 200 x 200 en formato RGB.
    #No carga una imagen desde archivo; la genera en memoria.

    # Crear imagen de prueba
    img.load_pixels()
    for i in range(len(img.pixels)):
        img.pixels[i] = py5.color(py5.random(255), py5.random(255), py5.random(255))
        #Asigna a cada píxel un color aleatorio:
        #rojo aleatorio
        #verde aleatorio
        #azul aleatorio
    img.update_pixels()


def draw():
    # Imagen original
    py5.image(img, 0, 0)

    # Solo canal rojo
    py5.tint(255, 0, 0)
    py5.image(img, 200, 0)

    # Solo canal verde
    py5.tint(0, 255, 0)
    py5.image(img, 400, 0)

    py5.no_tint()
"""Quita el tinte para que no afecte dibujos posteriores.
Qué estás viendo en la ventana:
a la izquierda: imagen original
en el centro: imagen teñida de rojo
a la derecha: imagen teñida de verde"""


py5.run_sketch()
# Este programa crea una imagen con colores aleatorios y la muestra con distintos tintes
# para comparar la imagen original con versiones filtradas por color.
