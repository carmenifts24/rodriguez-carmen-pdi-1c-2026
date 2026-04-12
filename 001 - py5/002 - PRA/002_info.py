#Este código muestra cómo obtener información básica del lienzo en `py5`. Primero se importa la biblioteca `py5`,
# que permite trabajar con sketches visuales en Python. Luego se define la función `setup()`, que se ejecuta una 
# # sola vez al iniciar el programa.
#Dentro de `setup()`, se establece el tamaño de la ventana con `py5.size(800, 600)`, creando un lienzo de 800 
# píxeles de ancho por 600 píxeles de alto. Después, con `py5.background(0)`, se asigna un fondo negro a la ventana.
# Una vez definido el lienzo, el programa imprime en consola tres datos importantes: el ancho (`py5.width`), el alto 
# (`py5.height`) y la cantidad total de píxeles, calculada multiplicando ambas dimensiones.
#Finalmente, `py5.run_sketch()` pone en marcha el sketch. En conjunto, este ejemplo sirve para entender cómo se 
# configura una ventana en `py5` y cómo consultar propiedades automáticas del lienzo, lo cual resulta útil como 
# base para ejercicios posteriores de dibujo, color y procesamiento de imágenes.*/

import py5


def setup():
    # Diferentes resoluciones
    py5.size(800, 600)  # HD 4:3
    py5.background(0)
   

    # Mostrar información de la ventana
    print(f"Ancho: {py5.width} píxeles")#ancho del lienzo
    print(f"Alto: {py5.height} píxeles")#alto del lienzo
    print(f"Total píxeles: {py5.width * py5.height}")


py5.run_sketch()
