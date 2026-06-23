# Modulo 004 — Librerias y fundamentos de PDI

## Que se estudia en este modulo

Este modulo es la transicion desde py5 hacia el ecosistema cientifico de Python para procesamiento de imagenes. Se introducen las librerias estandar del area y se aplican sobre imagenes reales, incluyendo las capturadas en el modulo 003.

El cambio de herramienta no es solo tecnico: donde py5 trabaja sobre un lienzo en tiempo real, OpenCV y numpy trabajan sobre matrices numericas en memoria. Esa diferencia de paradigma es importante: una imagen deja de ser "lo que se ve en pantalla" y pasa a ser un array multidimensional sobre el que se aplican operaciones matematicas.

## Temas trabajados

### Entorno y librerias

Se configura el entorno de trabajo y se presenta cada libreria con su rol especifico:

- `OpenCV` (cv2): lectura, escritura y procesamiento de imagenes.
- `Pillow` (PIL): operaciones sobre imagenes, modos de color, conversion de formatos.
- `scikit-image` (skimage): algoritmos de procesamiento de nivel mas alto.
- `matplotlib`: visualizacion de imagenes y graficos en notebooks.
- `numpy`: operaciones sobre arrays (la imagen como matriz numerica).

### Imagenes en color y canales

Se trabaja la representacion de imagenes color como arrays de forma `(alto, ancho, 3)`. Se separan los canales R, G y B y se visualizan por separado. Se introduce la diferencia entre el orden de canales en OpenCV (BGR) y en matplotlib/PIL (RGB), y como convertir entre ellos con `cv2.cvtColor`.

Se calculan y visualizan histogramas por canal para analizar la distribucion de intensidades en la imagen.

### Operaciones basicas con OpenCV

Se trabajan las operaciones fundamentales:
- lectura (`cv2.imread`) y escritura (`cv2.imwrite`) de imagenes.
- conversion entre espacios de color: `BGR`, `RGB`, `GRAY`, `HSV`, `LAB`.
- recorte y redimensionado.
- suma, resta y mezcla de imagenes con `cv2.addWeighted`.

### Muestreo y cuantizacion

Se estudian los dos parametros que definen la resolucion de una imagen digital:
- **Muestreo espacial (resolucion):** cuantos pixeles por unidad de area. Al reducirlo, la imagen pierde detalle y aparece el efecto de bloques.
- **Cuantizacion (profundidad de bit):** cuantos niveles de intensidad distintos puede representar cada canal. Al reducirla, la imagen muestra bandas de color visibles (banding o posterizacion).

Se simulan estas degradaciones para observar sus efectos visualmente.

### Segmentacion simple por color

Se aplica segmentacion por rango de color en espacio HSV. La idea es que HSV separa la informacion de color (H) de la de luminosidad (V), lo que permite definir mascaras de color robustas frente a variaciones de iluminacion.

El flujo es:
1. Convertir la imagen a HSV.
2. Definir un rango de valores de H, S y V con `cv2.inRange`.
3. Aplicar la mascara a la imagen original para aislar la region de interes.

### Recuperacion y preprocesamiento de imagenes propias

Se aplican las tecnicas del modulo sobre las imagenes capturadas en la camara oscura. El flujo incluye diagnostico visual, conversion de espacio de color, ajuste de contraste y preparacion para uso en tareas de mayor complejidad.

## Archivos

### Practicas (`002 - PRA`)

| Archivo | Contenido |
|---|---|
| `001 - entorno y librerias.ipynb` | verificacion del entorno, importaciones, primeras operaciones |
| `002 - imagenes en color y canales.ipynb` | RGB, BGR, histogramas, separacion de canales |
| `003 - operaciones basicas con opencv.ipynb` | lectura, conversion, recorte, mezcla |
| `004 - muestreo y cuantizacion.ipynb` | resolucion espacial y profundidad de bit |
| `005 - practica guiada de procesamiento de imagenes.ipynb` | flujo integrado sobre una imagen |
| `006 - laboratorio 2 - segmentacion simple por color.ipynb` | mascaras HSV para segmentar objetos por color |
| `007 - recuperacion y preprocesamiento de imagenes propias.ipynb` | trabajo sobre imagenes propias |
| `008 - actividad integradora - segmentacion por color.ipynb` | actividad final integradora |

### Laboratorio (`003 - LAB`)

| Archivo | Contenido |
|---|---|
| `2026_PDI_RODRIGUEZ_proc_digital.ipynb` | entrega: operaciones basicas de PDI |
| `2026_PDI_RODRIGUEZ_segmentac_color.ipynb` | entrega: segmentacion por color |
| `2026_PDI_RODRIGUEZ_ rec_preproc_imag_propias.ipynb` | entrega: recuperacion de imagenes propias |
| `2026_PDI_RODRIGUEZ_ integrador_segmentacion por color.ipynb` | entrega integradora |

## Librerias y herramientas

| Libreria | Uso en el modulo |
|---|---|
| `opencv-python` (cv2) | lectura, escritura, conversion de espacios, mascaras |
| `Pillow` (PIL) | operaciones de imagen, conversion de formatos |
| `scikit-image` (skimage) | algoritmos de procesamiento |
| `numpy` | arrays, operaciones matematicas sobre imagenes |
| `matplotlib` | visualizacion de imagenes e histogramas en notebook |

## Conexion con otros modulos

Los conceptos de canales, histogramas, espacios de color y segmentacion por mascara son la base directa del modulo 005, donde se extienden con una coleccion mas amplia de tecnicas de vision por computadora clasica.
