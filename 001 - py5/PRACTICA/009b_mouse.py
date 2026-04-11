"""interacción básica con el mouse: dibuja un círculo rojo que sigue la posición del cursor, 
pero solo mientras el mouse está dentro de la ventana.
Qué hace en general:
crea una ventana blanca
limpia el fondo en cada frame
verifica si el mouse está dentro del área visible
dibuja un círculo rojo en la posición del cursor"""


# Verificar instalación
import py5


def setup():
    py5.size(400, 300)
    py5.background(255)
    print("py5 funcionando correctamente")


def draw():
    py5.background(255)  # Limpiar el fondo en cada frame

    # Solo dibujar el círculo si el mouse está dentro de la ventana
    if 0 <= py5.mouse_x <= py5.width and 0 <= py5.mouse_y <= py5.height:
        py5.fill(255, 0, 0)
        py5.circle(py5.mouse_x, py5.mouse_y, 20)


py5.run_sketch()

# Este programa dibuja un circulo rojo que sigue al mouse
# mientras el cursor se encuentra dentro de la ventana.
