import py5


def setup():
    py5.size(600, 200)
    py5.color_mode(py5.RGB, 255)
    py5.no_stroke()


def draw():
    # Canal Rojo
    py5.fill(200, 0, 0)
    py5.rect(0, 0, 200, 200)

    # Canal Verde
    py5.fill(0, 200, 0)
    py5.rect(200, 0, 200, 200)

    # Canal Azul
    py5.fill(0, 0, 200)
    py5.rect(400, 0, 200, 200)


py5.run_sketch()

#El archivo 003_RGB.py presenta un ejemplo básico del uso del modelo de color RGB en py5. Su propósito es mostrar, 
# de manera visual, cómo los tres colores primarios de este sistema pueden representarse dentro de un lienzo dividido 
# en partes iguales. 

# El programa comienza importando la biblioteca py5, necesaria para crear la ventana gráfica y 
# utilizar las funciones de dibujo. 
# 
# Luego define la función setup(), que se ejecuta una sola vez al inicio del sketch. Dentro de esta función se 
# establece el tamaño de la ventana en 600 píxeles de ancho por 200 de alto, generando un formato horizontal 
# adecuado para distribuir el contenido en tres secciones.

#A continuación, se configura el modo de color mediante color_mode(py5.RGB, 255). Esto indica que los colores serán 
# interpretados en el sistema RGB, donde cada canal de color, rojo, verde y azul, puede tomar valores entre 0 y 255.

#También se utiliza no_stroke() para eliminar los bordes de las figuras, de modo que los rectángulos aparezcan 
# únicamente con su color de relleno.

#Después se define la función draw(), encargada de dibujar el contenido visual del sketch. En esta parte se crean 
# tres rectángulos consecutivos. 
    # El primero utiliza fill(200, 0, 0), lo que produce un rojo intenso, y se dibuja en la posición inicial del lienzo. 
    # El segundo usa fill(0, 200, 0), correspondiente al verde, y se ubica en la sección central. 
    # El tercero emplea fill(0, 0, 200), generando azul, y se dibuja en la última parte de la ventana.
#Cada rectángulo ocupa 200 píxeles de ancho por 200 de alto, de manera que los tres juntos llenan completamente la 
# ventana de 600 por 200 píxeles. Con esta disposición, el sketch permite observar con claridad la separación entre los tres canales primarios del modelo RGB.
#Finalmente, la instrucción run_sketch() pone en marcha el programa. En conjunto, este ejemplo funciona como una 
# introducción visual al sistema RGB y ayuda a comprender que los colores en este modelo se construyen a partir de la combinación de intensidades de rojo, verde y azul.

