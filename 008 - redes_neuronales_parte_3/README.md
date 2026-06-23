# Modulo 008 — Redes neuronales (parte 3)

## Que se estudia en este modulo

Este modulo cierra el bloque de redes neuronales con un foco en experimentacion y comprension profunda. Se entrena una CNN propia para clasificacion de frutas, se comparan arquitecturas y estrategias, y se abre la "caja negra" para observar que ocurre dentro de una red convolucional durante el procesamiento de una imagen.

El objetivo es que la red deje de ser una herramienta opaca: entender como los filtros convolucionales se activan ante distintos estimulos visuales y por que ciertas arquitecturas funcionan mejor que otras en un problema concreto.

## Temas trabajados

### Preparacion de datasets por carpeta

Se trabaja el flujo estandar de preparacion de datasets para clasificacion de imagenes:

- Estructura de carpetas por clase (`naranjas/`, `manzanas/`).
- Carga con `ImageDataGenerator` de Keras o `DataLoader` de PyTorch.
- Division en train, validation y test.
- Aumentacion de datos (data augmentation): rotaciones, flips, zoom, cambios de brillo. El objetivo es aumentar la variedad del dataset sin capturar nuevas imagenes, reduciendo el sobreajuste.

### Entrenamiento y evaluacion de CNN propia

Se define una arquitectura CNN desde cero:

- Capas convolucionales con activacion ReLU.
- Capas de pooling (max pooling) para reducir la dimensionalidad espacial.
- Dropout para regularizacion.
- Capas densas de clasificacion final con softmax.

Se entrena sobre el dataset de frutas y se evalua con matriz de confusion, accuracy y curvas de entrenamiento (loss y accuracy por epoca).

### Comparacion de modelos y arquitecturas

Se comparan distintas configuraciones:

- Variaciones en la profundidad de la red (mas o menos capas).
- Diferentes tamanios de kernel.
- Con y sin data augmentation.
- CNN propia vs modelo preentrenado fine-tuneado.

Se analiza el tradeoff entre complejidad del modelo, tiempo de entrenamiento y capacidad de generalizacion.

### Inspeccion de filtros y activaciones

Se extraen los pesos de los filtros de la primera capa convolucional y se visualizan como imagenes. Se observa que los filtros aprendidos tienen patrones reconocibles: detectores de bordes en distintas orientaciones, detectores de frecuencia, detectores de color.

Se calculan los feature maps (mapas de activacion) de cada capa para una imagen de entrada:

- Las primeras capas producen feature maps con patrones de bajo nivel (bordes, texturas).
- Las capas mas profundas producen activaciones mas abstractas y selectivas.

Se trabajan dos versiones:
- **Filtros aleatorios:** se visualiza lo que hace una red sin entrenar. Las activaciones no tienen estructura coherente.
- **Filtros entrenados:** se compara con los filtros aprendidos tras el entrenamiento. La diferencia es visible: los filtros entrenados tienen estructura y responden a patrones especificos.

### Inferencia con camara web

Se integra la CNN entrenada con captura de video en tiempo real desde la camara web (en Colab). Se muestra el frame capturado junto con la prediccion del modelo y la confianza.

## Archivos

| Archivo | Contenido |
|---|---|
| `clasificador_frutas_extended.ipynb` | entrenamiento extendido de CNN para naranjas y manzanas |
| `comparacion_modelos.ipynb` | comparacion de arquitecturas, estrategias y metricas |
| `crea_tu_propio_modelo_cnn.ipynb` | plantilla configurable para definir y entrenar una CNN propia |
| `probamos_el_modelo_con_camweb.ipynb` | inferencia en tiempo real con camara web en Colab |
| `prueba_colab_desde_folder.ipynb` | flujo completo de entrenamiento y validacion desde carpeta |
| `una_convolucion_por_dentro_random.ipynb` | visualizacion de filtros y feature maps en red sin entrenar |
| `una_convolucion_por_dentro_train.ipynb` | visualizacion de filtros y feature maps en red entrenada |
| `arq/` | diagramas de arquitecturas CNN |
| `funcionamento_calsificador_naranjasymanzanas.mp4` | video de demostracion del clasificador con camara |

## Librerias y herramientas

| Libreria | Uso en el modulo |
|---|---|
| `tensorflow` / `keras` | definicion de arquitecturas, entrenamiento, evaluacion |
| `torch` / `torchvision` | alternativa PyTorch para algunos notebooks |
| `numpy` | manipulacion de arrays, preprocesamiento |
| `matplotlib` | visualizacion de filtros, activaciones y curvas de entrenamiento |
| `scikit-learn` | metricas: matriz de confusion, classification report |
| `Pillow` (PIL) | carga y redimensionado de imagenes del dataset |
| `opencv-python` (cv2) | captura de video, preprocesamiento para inferencia |

## Recomendaciones

El entrenamiento de las CNNs puede ser lento en CPU local. Se recomienda:
- Usar los notebooks marcados `_colab` en Google Colab con GPU T4 para entrenamientos de mas de 10 epocas.
- Los notebooks de visualizacion de filtros pueden ejecutarse localmente sin inconvenientes, ya que no requieren entrenamiento largo.

## Conexion con otros modulos

La comprension del funcionamiento interno de una CNN que se desarrolla aqui es directamente complementaria a los modelos preentrenados del modulo 008-parte2 y a los modelos de difusion del modulo 010, que tambien usan arquitecturas convolucionales y de atencion como bloques base.
