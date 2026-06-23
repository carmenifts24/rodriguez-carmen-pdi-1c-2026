# Modulo 005 — Vision por computadora clasica (parte 1)

## Que se estudia en este modulo

Este modulo cubre las tecnicas fundamentales de vision por computadora clasica, es decir, aquellas que no usan redes neuronales sino operaciones matematicas definidas explicitamente. El objetivo es dominar el pipeline de procesamiento que precede a cualquier tarea de analisis: mejorar la imagen, extraer regiones de interes, detectar estructuras y describir sus propiedades geometricas.

Todo el trabajo se realiza con OpenCV sobre imagenes estaticas. Los notebooks avanzan de menor a mayor complejidad: primero se entiende la imagen y sus representaciones, luego se la transforma, luego se extraen regiones y finalmente se describen objetos.

## Temas trabajados

### Espacios de color y segmentacion HSV

Se trabajan los principales espacios de color usados en procesamiento:

- **BGR/RGB:** representacion nativa de OpenCV. Cada canal es independiente pero el color y la luminosidad estan mezclados.
- **HSV (Hue, Saturation, Value):** separa el matiz del brillo. Permite definir rangos de color robustos a cambios de iluminacion. Es el espacio preferido para segmentacion por color.
- **LAB (L\*a\*b\*):** separa la luminosidad (L) de los componentes de color (a y b) de forma perceptualmente uniforme. Util para operaciones que deben ser neutras al brillo.
- **Escala de grises:** imagen de un solo canal, util para deteccion de bordes, contornos y umbralizado.

### Formatos de imagen y lectura

Se analizan las diferencias entre formatos sin perdida (PNG, BMP, TIFF) y con compresion (JPEG, WebP): como afecta la compresion a los valores de pixel, como detectar artefactos de compresion y cuando usar cada formato.

### Mejora de imagen y ecualizacion

- **Ajuste lineal de brillo y contraste** con `cv2.convertScaleAbs`: escala los valores de pixel por un factor y desplaza el origen. Rapido pero afecta toda la imagen por igual.
- **Ecualizacion global del histograma** (`cv2.equalizeHist`): redistribuye los niveles de intensidad para maximizar el uso del rango disponible. Aumenta contraste global pero puede amplificar ruido.
- **CLAHE (Contrast Limited Adaptive Histogram Equalization):** ecualizacion local por bloques con limite de amplificacion. Mejora el contraste local sin exagerar las zonas ya contrastadas. Es la tecnica preferida cuando la iluminacion es irregular.

### Transformaciones geometricas

- **Rotacion y traslacion:** matrices de transformacion afin (`cv2.getRotationMatrix2D`, `cv2.warpAffine`).
- **Escala y resize:** `cv2.resize` con interpolaciones distintas (INTER_NEAREST, INTER_LINEAR, INTER_CUBIC).
- **Transformacion de perspectiva:** `cv2.getPerspectiveTransform` + `cv2.warpPerspective`. Permite corregir perspectiva o extraer regiones planas.

### Filtros de suavizado y reduccion de ruido

- **Filtro gaussiano** (`cv2.GaussianBlur`): convoluciona la imagen con un kernel gaussiano. Reduce ruido de alta frecuencia pero desenfoca los bordes.
- **Filtro de mediana** (`cv2.medianBlur`): reemplaza cada pixel por la mediana de su vecindad. Muy efectivo para ruido sal-y-pimienta sin difuminar bordes.
- **Filtro bilateral** (`cv2.bilateralFilter`): suaviza pero preserva bordes por ser sensible a la similitud de intensidad ademas de la proximidad espacial. Mas lento pero de mayor calidad.

### Umbralizacion

- **Umbral global** (`cv2.threshold`): binariza la imagen con un valor fijo. Funciona bien cuando la iluminacion es uniforme.
- **Metodo de Otsu** (`cv2.THRESH_OTSU`): calcula automaticamente el umbral optimo basandose en la distribucion bimodal del histograma.
- **Umbral adaptativo** (`cv2.adaptiveThreshold`): calcula el umbral de forma local por bloques. Robusto ante iluminacion no uniforme.

### Morfologia matematica

Opera sobre imagenes binarias (o en escala de grises) usando un elemento estructurante (kernel):

- **Erosion:** elimina pixeles en los bordes de las regiones blancas. Reduce objetos pequenos.
- **Dilatacion:** expande los bordes de las regiones blancas. Une objetos cercanos.
- **Apertura (opening):** erosion seguida de dilatacion. Elimina ruido pequeno sin cambiar los objetos grandes.
- **Cierre (closing):** dilatacion seguida de erosion. Cierra agujeros pequenos dentro de objetos.

Estas operaciones se usan para limpiar mascaras de segmentacion y preparar binarias para deteccion de contornos.

### Restauracion e inpainting

El inpainting reconstruye zonas danadas de una imagen usando la informacion del contexto circundante. Se trabajan dos algoritmos:

- `cv2.INPAINT_TELEA`: basado en transporte de imagen (rapido, bueno para rayas delgadas).
- `cv2.INPAINT_NS`: basado en ecuaciones de Navier-Stokes (mas suave, mejor para areas grandes).

El resultado depende fuertemente de la calidad de la mascara de dano.

### Deteccion de contornos y propiedades geometricas

- `cv2.Canny`: detector de bordes por gradiente con histeresis. Produce bordes delgados y conectados.
- `cv2.findContours`: extrae los contornos como secuencias de puntos a partir de una imagen binaria.
- Propiedades geometricas: area, perimetro, bounding box, centroide, excentricidad, circularidad, convex hull. Se calculan con `cv2.contourArea`, `cv2.boundingRect`, `cv2.moments`, `cv2.convexHull`.

### Coincidencia por plantilla (template matching)

`cv2.matchTemplate` desliza una imagen de referencia (template) sobre la imagen fuente y calcula la similitud en cada posicion. Se usan metricas como `TM_CCOEFF_NORMED`. Funciona bien para objetos rigidos sin cambio de escala ni rotacion.

### Deteccion de rostros con cascadas Haar

`cv2.CascadeClassifier` carga un clasificador preentrenado con el algoritmo de Viola-Jones. Detecta rostros frontales (u otras estructuras, segun el clasificador) mediante una cascada de filtros rectangulares (caracteristicas Haar) calculados con imagenes integrales. Es rapido y funciona en CPU, pero es sensible a cambios de escala, orientacion e iluminacion.

## Archivos

| Archivo | Contenido |
|---|---|
| `001 - introduccion a opencv y espacios de color.ipynb` | BGR, RGB, HSV, LAB, grises; conversiones |
| `001B - practicas_hsv.ipynb` | segmentacion y mascaras en espacio HSV |
| `001C  - rueda cromatica.ipynb` | visualizacion de la rueda de colores en HSV |
| `002 - formatos de archivos de imagen.ipynb` | PNG, JPEG, TIFF; compresion y artefactos |
| `003 - mejora de imagen y ecualizacion basica.ipynb` | brillo, contraste, ecualizacion global, CLAHE |
| `003B - mejora de imagen y ecualizacion basica img1.ipynb` | misma practica sobre imagen alternativa |
| `004 - comparacion de estrategias de ecualizacion.ipynb` | comparacion sistematica de metodos de ecualizacion |
| `004b - operaciones basicas con imagenes.ipynb` | redimensionado, recorte, mezcla |
| `004C - operaciones basicas con imagenes actividad.ipynb` | actividad sobre operaciones basicas |
| `005 - transformaciones geometricas y cambio de perspectiva.ipynb` | rotacion, afin, perspectiva |
| `006 - operaciones graficas.ipynb` | dibujo sobre imagenes: rectangulos, textos, circulos |
| `006b - filtros de suavizado y reduccion de ruido.ipynb` | Gaussiano, mediana, bilateral |
| `006b2 - umbralizacion global, Otsu y adaptive threshold.ipynb` | los tres metodos de umbralizado comparados |
| `006c - morfologia matematica para limpieza de mascaras.ipynb` | erosion, dilatacion, opening, closing |
| `006d - restauracion y algoritmos de inpainting.ipynb` | inpainting TELEA y NS con mascaras |
| `007 - deteccion de contornos.ipynb` | Canny y findContours |
| `008 - propiedades geometricas de contornos.ipynb` | area, perimetro, centroide, convex hull |
| `009 - coincidencia por plantilla.ipynb` | template matching con matchTemplate |
| `010 - deteccion de rostros con haar.ipynb` | CascadeClassifier para deteccion facial |
| `Utilidades_y_Plantillas.ipynb` | funciones y plantillas reutilizables del modulo |

## Librerias y herramientas

| Libreria | Uso en el modulo |
|---|---|
| `opencv-python` (cv2) | todas las operaciones del modulo |
| `numpy` | manipulacion de arrays, mascaras booleanas |
| `matplotlib` | visualizacion de imagenes y graficos |
| `scikit-image` | algoritmos complementarios |

## Conexion con otros modulos

Las tecnicas de este modulo (especialmente mascaras, morfologia e inpainting) son aplicadas directamente en el TFI 1 (modulo 006). La deteccion de estructuras y la comprension de espacios de color son la base conceptual para las redes neuronales que trabajan con imagenes en los modulos 008 y siguientes.
