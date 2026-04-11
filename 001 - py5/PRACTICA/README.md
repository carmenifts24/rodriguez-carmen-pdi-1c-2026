# Proyecto de actividades con py5

Esta carpeta reúne ejercicios y prácticas de `py5` orientados al dibujo generativo, el manejo del color, la carga y transformación de imágenes, la manipulación de píxeles y la interacción con el mouse. El trabajo muestra un recorrido progresivo: desde sketches muy básicos hasta pequeñas herramientas interactivas de dibujo.

## Objetivo general

El proyecto explora cómo usar `py5` para:

- crear ventanas y sketches básicos;
- dibujar formas y trabajar con coordenadas;
- comprender modelos de color como `RGB` y `HSB/HSV`;
- cargar, mostrar y transformar imágenes;
- modificar píxeles de forma manual;
- aplicar filtros visuales;
- incorporar interacción con el mouse y el teclado;
- construir una aplicación sencilla de dibujo tipo paint.

## Resumen de actividades

### 1. Introducción a py5

- `000_intro_py5.py`: primer sketch; crea una ventana, dibuja un rectángulo y guarda una imagen generada.
- `001_basico.py`: prueba básica del entorno con fondo, figura simple y uso de `draw()`.
- `002_info.py`: consulta dimensiones del lienzo y cantidad total de píxeles.
- `002b_info_visual.py`: presenta la información del lienzo de forma visual dentro de la ventana.

### 2. Color y representación visual

- `001b_basico_HSV.py`: introducción al modo de color `HSB`, equivalente conceptual a `HSV`.
- `001c_hsv_gradiente.py`: crea un gradiente horizontal de tonos para comparar colores en HSB.
- `003_RGB.py`: muestra los tres canales básicos del modelo RGB mediante rectángulos de color.
- `004_HSV.py`: genera una visualización continua del rango de tonos en HSB.

### 3. Carga y visualización de imágenes

- `005_upload_img.py`: carga una imagen desde la carpeta `img`, la muestra en tamaño original y también redimensionada.

### 4. Trabajo directo con píxeles

- `006_pixeles.py`: modifica píxeles del lienzo para construir un patrón de color desde cero.
- `007_pixeles.py`: recorre los píxeles de una imagen, invierte sus colores y permite guardarla procesada.

### 5. Filtros y procesamiento de imagen

- `008_filtro.py`: genera una imagen de prueba y compara la imagen original con versiones teñidas por canal.
- `010_filtro.py`: aplica un filtro `THRESHOLD`.
- `011_filtro.py`: aplica un filtro en escala de grises (`GRAY`).
- `012_filtro.py`: aplica un filtro de inversión (`INVERT`).
- `013_filtro.py`: aplica un desenfoque (`BLUR`).
- `014_filtro.py`: aplica un filtro de dilatación (`DILATE`).

### 6. Interacción con el mouse

- `009b_mouse.py`: dibuja un círculo que sigue al cursor mientras está dentro de la ventana.
- `009c_mouse.py`: dibuja solo cuando el botón del mouse está presionado.
- `009_mouse.py`: deja una huella de cuadrados y cambia el color con cada clic.

### 7. Dibujo generativo e interacción ampliada

- `015_dibujo.py`: experimento visual con generación de formas a partir de ruido y posición del mouse.
- `2026_PDI_RODRIGUEZ_CARMEN.py`: herramienta de dibujo tipo paint con pincel, borrador, paleta de colores, figuras, cambio de grosor y guardado de capturas.

## Archivos y recursos complementarios

- `img/`: imágenes usadas como entrada para pruebas de carga, filtros y procesamiento.
- `save/`: carpeta destinada al guardado de resultados generados.
- `jupyter/py5_on_Colab_demo.ipynb`: cuaderno de apoyo para experimentar con py5 en Colab.
- `py5_referencia.md`: apuntes o material de referencia sobre funciones y conceptos de py5.
- `info.txt`: notas breves de apoyo.

## En conjunto

La carpeta documenta un proceso de aprendizaje práctico en procesamiento de imágenes y gráficos interactivos con Python y `py5`. Las actividades avanzan desde conceptos fundamentales hasta aplicaciones más completas, combinando programación visual, teoría del color, manipulación de imágenes e interacción en tiempo real.
