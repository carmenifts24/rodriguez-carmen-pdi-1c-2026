# Modulo 001 — Introduccion a py5 y programacion visual

## Que se estudia en este modulo

Este modulo introduce `py5`, un binding de Python para Processing. Processing es un entorno de programacion orientado a la creacion visual: define un loop continuo donde una funcion `setup()` inicializa el lienzo y `draw()` se ejecuta cuadro por cuadro, lo que permite animacion, interaccion y generacion de imagenes en tiempo real.

El foco esta en comprender la imagen como una estructura de datos: una grilla de pixeles donde cada celda almacena valores de color segun el modelo elegido. Ese entendimiento es la base de todo el procesamiento digital de imagenes que viene despues.

## Temas trabajados

### Modelo de color RGB

Cada pixel tiene tres canales: Rojo, Verde y Azul, con valores entre 0 y 255. La combinacion de esos tres valores determina el color percibido. Se trabaja la intuicion de mezcla aditiva: rojo + verde = amarillo, los tres al maximo = blanco, los tres en cero = negro.

### Modelo de color HSV / HSB

Alternativa perceptual a RGB. Tiene tres componentes:
- **H (Hue / Matiz):** el color en si, expresado como angulo (0–360 en Processing, 0–255 en py5 por defecto).
- **S (Saturation / Saturacion):** que tan "puro" o "grisaceo" es el color.
- **V/B (Value / Brightness):** que tan brillante o oscuro es.

Es mas intuitivo para seleccionar colores o segmentar rangos (por ejemplo, "todos los tonos naranjas") porque agrupa visualmente lo que el ojo percibe como similar.

### Carga y visualizacion de imagenes

Se carga una imagen desde disco con `load_image()` y se muestra con `image()`. Desde ese punto la imagen es un objeto con propiedades de ancho, alto y acceso a pixeles individuales.

### Manipulacion de pixeles

Se accede al buffer de pixeles de la imagen o del lienzo con `load_pixels()` / `update_pixels()`. Cada pixel es un entero de 32 bits (canal alfa + RGB). Se trabajan transformaciones directas sobre ese buffer: invertir colores, intercambiar canales, generar gradientes.

### Filtros visuales

Se aplican filtros incorporados de py5 (`filter()`) y filtros manuales implementados con bucles sobre el buffer de pixeles:
- inversion de color
- escala de grises por promedio o por luminancia
- ajuste de brillo multiplicativo

### Interaccion con el mouse

Se usa la posicion del mouse (`mouse_x`, `mouse_y`) para controlar parametros de la imagen o del dibujo en tiempo real. Se implementan efectos que responden al cursor.

### Dibujo generativo

Se construyen composiciones visuales usando primitivas de dibujo (circulos, rectangulos, lineas) combinadas con logica iterativa y aleatoriedad controlada.

## Archivos

| Archivo | Contenido |
|---|---|
| `000_intro_py5.py` | primer sketch, ventana y fondo de color |
| `001_basico.py` | setup y draw basicos, formas primitivas |
| `001b_basico_HSV.py` | mismo sketch con modelo HSV |
| `001c_hsv_gradiente.py` | gradiente usando el matiz H |
| `002_info.py` | lectura de propiedades de una imagen |
| `002b_info_visual.py` | visualizacion de la informacion de imagen |
| `003_RGB.py` | separacion y visualizacion de canales RGB |
| `004_HSV.py` | conversion a HSV y visualizacion por canal |
| `005_upload_img.py` | carga y display de imagen externa |
| `006_pixeles.py` — `007_pixeles.py` | acceso al buffer de pixeles, manipulacion directa |
| `008_filtro.py` | primer filtro manual |
| `009_mouse.py` — `009c_mouse.py` | efectos controlados por mouse |
| `010_filtro.py` — `015_dibujo.py` | filtros progresivos y composiciones generativas |
| `py5_referencia.md` | referencia rapida de funciones de py5 |

### Laboratorio (`003 - LAB`)

- `2026_PDI_RODRIGUEZ_CARMEN.py`: entrega integradora de la unidad.

## Librerias y herramientas

| Libreria | Uso en el modulo |
|---|---|
| `py5` | motor grafico, loop setup/draw, primitivas, pixeles |
| `numpy` | operaciones sobre arrays de pixeles |
| Java (JVM) | requerido por py5 como backend de Processing |

## Prerequisitos de ejecucion

py5 necesita Java instalado en el sistema. Si aparece un error al iniciar el sketch, verificar:

```bash
java -version
```

Si no esta instalado, descargar desde [adoptium.net](https://adoptium.net/).

Para correr un sketch:

```bash
python nombre_archivo.py
```

O desde VS Code con el boton de run, asegurandose de que el entorno virtual del proyecto este activo.
