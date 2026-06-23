# Modulo 007 — Fotografia digital

## Que se estudia en este modulo

Este modulo integra teoria fotografica con procesamiento digital de imagenes. Todas las fotografias son de produccion propia: el trabajo parte del acto fotografico (encuadre, punto de vista, luz) y aplica procesamiento para analizar, reforzar o reinterpretar lo capturado.

El objetivo es desarrollar una lectura tecnica e intencional de la imagen fotografica: entender como las decisiones al momento de la captura determinan las posibilidades de procesamiento posterior, y como el procesamiento puede revelar o construir significado en una imagen.

La presentacion conceptual del recorrido esta en `De la camara oscura a la imagen intencional.pdf`.

## Partes del trabajo

### Parte 1 — Camara oscura

Se retoma la imagen capturada con camara oscura artesanal en el modulo 003. Se aplica:

- Rotacion y recorte para corregir orientacion y composicion.
- Conversion al espacio HSV y ecualizacion del canal V para mejorar el contraste general sin alterar la tonalidad.

El canal V (Value/Brightness) concentra la informacion de luminosidad, por lo que ecualizarlo mejora el contraste sin afectar los colores. Esta es la diferencia clave respecto a ecualizar directamente en RGB.

### Parte 2 — Composicion y lenguaje visual

Se trabaja una imagen de composicion intencional para analizar como la estructura visual prevalece sobre el color:

- Reencuadre compositivo para aislar el elemento principal.
- Conversion a escala de grises para eliminar el color como elemento de distraccion.
- Binarizacion con umbral de Otsu para reducir la imagen a forma pura.
- Ecualizacion del histograma para maximizar el rango tonal.

### Parte 3 — Reencuadre y reinterpretacion

A partir de una unica imagen amplia se producen dos recortes con lecturas intencionalmente distintas:

- **Lectura arquitectonica:** enfocada en la estructura, la geometria y la composicion formal.
- **Lectura narrativa:** enfocada en el sujeto, el contexto y la relacion emocional.

Se demuestra que el encuadre no es una operacion neutral: construye sentido al incluir o excluir informacion visual.

### Parte 4 — Punto de vista

Se comparan dos fotografias del mismo sujeto tomadas desde posiciones distintas (por encima, al nivel, por debajo). El analisis se centra en:

- Cambio de escala percibida del sujeto.
- Cantidad de contexto visible en cada plano.
- Relacion emocional que transmite cada encuadre.

### Parte 5 — Fotografia basada en la luz

Se analizan cuatro fotografias del mismo sujeto o escena en condiciones de luz distintas. Para cada imagen se calculan metricas cuantitativas:

- **Luminosidad media:** valor promedio del canal de brillo.
- **Contraste:** desviacion estandar de los valores de intensidad.
- **Rango dinamico:** diferencia entre el valor maximo y minimo efectivo.
- **Histograma de luminosidad:** distribucion de los niveles de brillo.

A partir del analisis se selecciona la fotografia con mejor comportamiento luminico y se documenta visualmente la direccion de la luz.

## Archivos

| Archivo | Contenido |
|---|---|
| `002_codigo/Trabajo Practico 006 - Fotografia Digital.ipynb` | notebook de resolucion completo |
| `De la camara oscura a la imagen intencional.pdf` | presentacion del recorrido conceptual |
| `De la camara oscura a la imagen intencional.pptx` | version editable de la presentacion |
| `003_recursos/` | imagenes propias usadas en el trabajo |

## Tecnicas aplicadas

| Tecnica | Donde se usa |
|---|---|
| `cv2.cvtColor(img, BGR2HSV)` | conversion al espacio HSV para trabajar sobre V |
| `cv2.equalizeHist` | ecualizacion del canal V y de imagenes en grises |
| `cv2.threshold` con `THRESH_OTSU` | binarizacion automatica para analisis de forma |
| Recorte con slicing numpy | reencuadre y composicion programatica |
| `np.mean`, `np.std`, `np.max`, `np.min` | metricas de luminosidad y contraste |
| `matplotlib.pyplot.hist` | visualizacion de histogramas de luminosidad |
| Anotaciones con `matplotlib.patches` | mapas de encuadre y esquemas de luz anotados |

## Librerias y herramientas

| Libreria | Uso en el modulo |
|---|---|
| `opencv-python` (cv2) | conversion de espacios, ecualizacion, umbralizado |
| `numpy` | metricas numericas sobre arrays de imagen |
| `matplotlib` | visualizacion comparativa, histogramas, anotaciones |
| `pandas` | tabla comparativa de metricas por imagen |

## Conexion con otros modulos

Este modulo cierra el ciclo de vision clasica antes de pasar a redes neuronales. Las decisiones de captura (luz, encuadre, punto de vista) que se analizan aqui tienen impacto directo en la calidad del dataset cuando se trabaja con modelos de clasificacion o deteccion en los modulos 008 y 009.
