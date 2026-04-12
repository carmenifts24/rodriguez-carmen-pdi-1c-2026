# Ejemplo basico del modelo HSV/HSB en py5
# Se muestra una figura coloreada con tono, saturacion y brillo.
# En py5 se usa HSB, que es muy similar a HSV.
# La diferencia principal es que el tercer valor se interpreta como brillo.


import py5


def setup():
    py5.size(400, 400)
    py5.color_mode(py5.HSB, 360, 100, 100)
    # Cambia el sistema de color a HSB:
    # H = tono, de 0 a 360
    # S = saturacion, de 0 a 100
    # B = brillo, de 0 a 100
    py5.no_stroke()


def draw():
    for i in range(360):
        py5.fill(i, 100, 100)
        # Define el color de relleno usando HSB:
        # 120 = tono
        # 80 = saturacion
        # 90 = brillo
        py5.rect(i, 0, 1, py5.height)
        #py5.rect(x, y, ancho, alto)
        #cada parte significa:
            # i: posición horizontal donde empieza el rectángulo
            # 0: posición vertical donde empieza, o sea arriba de todo
            # 1: ancho del rectángulo, en este caso solo 1 píxel
            # py5.height: alto del rectángulo, o sea toda la altura del lienzo
        #dibuja un rectángulo muy angosto, de 1 píxel de ancho, que ocupa toda la altura de la ventana.



py5.run_sketch()
"""
py5.color_mode(...): cambia el sistema de color
py5.HSB: indica que se usará el modelo HSB
360: rango máximo del tono (Hue)
100: rango máximo de la saturación (Saturation)
100: rango máximo del brillo (Brightness)
Qué representa cada canal:

H o Hue: el tono o tipo de color
S o Saturation: qué tan intenso o apagado se ve
B o Brightness: qué tan claro u oscuro se ve"""