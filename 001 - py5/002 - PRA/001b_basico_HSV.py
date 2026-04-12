import py5


def setup():
    py5.size(400, 400)
    py5.color_mode(py5.HSB, 360, 100, 100)
    #Cambia la forma en que py5 interpreta los colores. En vez de usar RGB, le dices que use HSB:
    # H = Hue, tono
    # S = Saturation, saturación
    # B = Brightness, brillo
    # Además defines los rangos:
    # tono de 0 a 360
    # saturación de 0 a 100
    # brillo de 0 a 100

    py5.background(200)
    print("py5 funcionando correctamente")


def draw():
    py5.fill(235, 40, 30)
    py5.rect(150, 150, 100, 100)


py5.run_sketch()
