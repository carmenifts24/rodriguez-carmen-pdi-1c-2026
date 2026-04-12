"""interacción básica con el mouse en py5: dibuja cuadrados pequeños siguiendo la posición del cursor y 
cambia el color de dibujo cada vez que haces clic.

Qué hace en general:

crea una ventana
dibuja un cuadrado donde está el mouse
deja una “huella” mientras mueves el cursor
cambia el color del cuadrado al presionar el mouse"""

import py5


def setup():
    py5.size(400, 400)
    py5.rect_mode(py5.CENTER)
    """Cambia la forma en que se posicionan los rectángulos y cuadrados.
    Normalmente, un rectángulo se dibuja usando la esquina superior izquierda como referencia.
    Con py5.CENTER, el rectángulo se dibuja usando su centro.
    Eso hace que el cuadrado quede centrado exactamente en la posición del mouse."""
    py5.no_stroke()


def draw():
    py5.square(py5.mouse_x, py5.mouse_y, 10)
    """Cambia el color de relleno a uno aleatorio.
    Cada vez que haces clic:
    se genera un rojo aleatorio
    un verde aleatorio
    un azul aleatorio"""


def mouse_pressed():
    py5.fill(py5.random_int(255), py5.random_int(255), py5.random_int(255))
    """Cambia el color de relleno a uno aleatorio.
    Cada vez que haces clic:
    se genera un rojo aleatorio
    un verde aleatorio
u   n azul aleatorio"""


py5.run_sketch()
# Este programa dibuja cuadrados en la posicion del mouse y cambia su color
# cada vez que se hace clic, creando una traza de colores en pantalla.


"""
draw() produce el dibujo continuo
mouse_pressed() modifica una condición del dibujo
Por eso juntos generan el efecto de “pintar” con el mouse y cambiar de color al hacer clic.

Una forma simple de pensarlo es esta:

draw() = acción constante
mouse_pressed() = evento puntual
"""