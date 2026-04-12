import py5 #biblioteca para crear la ventana, dibujar formas, usar color y guardar imágenes.


def setup():#Se usa para preparar el sketch, por ejemplo definir el tamaño de la ventana, colores iniciales o cargar recursos.
    py5.size(500, 500)
    py5.fill("#00D92F")
    py5.rect(150, 150, 200, 200)
    py5.save("/img/testing/000_intro_py5.png")#ruta donde se guarda el archivo generado


py5.run_sketch()#Esta línea inicia el sketch. Es la que hace que py5 arranque y llame a setup().
