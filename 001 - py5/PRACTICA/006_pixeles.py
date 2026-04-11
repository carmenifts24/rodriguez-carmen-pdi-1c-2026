"""En este archivo se muestra cómo modificar directamente los píxeles del lienzo en py5. En lugar de dibujar figuras como rectángulos 
o círculos, aquí se trabaja sobre el arreglo de píxeles de la ventana para construir una imagen pixel por pixel."""


import py5


def setup():
    py5.size(400, 400)
    py5.load_pixels() #Carga el arreglo de píxeles del lienzo en py5.pixels.
    #Esto permite acceder directamente a cada píxel de la ventana y cambiar su color.

    # Crear un patrón de píxeles
    for x in range(py5.width):
        for y in range(py5.height):
            # Calcular índice en el array de píxeles
            index = x + y * py5.width
            #Calcula la posición del píxel dentro del arreglo lineal py5.pixels.
            #Aunque visualmente el lienzo es bidimensional (x, y), internamente los píxeles se guardan en una lista 
            #de una sola dimensión.

            # Crear patrón de colores
            r = (x * 255) // py5.width #r depende de x, así que aumenta de izquierda a derecha
            g = (y * 255) // py5.height #g depende de y, así que aumenta de arriba hacia abajo
            b = 128
            #Esto genera un degradado donde cambian rojo y verde según la posición, mientras el azul se mantiene constante.

            py5.pixels[index] = py5.color(r, g, b)

    py5.update_pixels()
    #Aplica en pantalla todos los cambios hechos en py5.pixels.
    # Esto es importante: después de modificar los píxeles, hay que llamar a update_pixels() para que el lienzo 
    # se actualice visualmente.


py5.run_sketch()

# Este programa recorre todos los pixeles del lienzo y asigna a cada uno
# un color RGB segun su posicion, creando un patron de degradado.
