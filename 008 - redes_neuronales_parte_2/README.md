# Modulo 008 — Redes neuronales (parte 2)

## Que se estudia en este modulo

Este modulo profundiza en redes neuronales aplicadas a imagenes. Retoma los conceptos base de la parte 1 con mayor detalle y los extiende hacia modelos preentrenados, transferencia de aprendizaje, el ecosistema de Hugging Face y el despliegue de aplicaciones con Gradio.

El eje central es pasar de entrenar modelos desde cero a aprovechar modelos ya entrenados en datasets masivos, adaptarlos a tareas propias con transfer learning y publicarlos como aplicaciones interactivas. Se trabaja tambien OCR como caso de investigacion critica: no solo como tecnica sino como ejercicio de validacion de fuentes y evaluacion de limitaciones.

## Temas trabajados

### Comparacion MLP vs CNN

Se repasan las diferencias estructurales entre redes densas (MLP) y redes convolucionales (CNN):

- Un MLP trata la imagen como un vector plano: destruye la estructura espacial.
- Una CNN aplica filtros convolucionales que preservan la disposicion espacial de los pixeles, lo que la hace mucho mas efectiva para imagenes.

Se comparan resultados en el mismo dataset para cuantificar la diferencia.

### Visualizacion de filtros y activaciones

Se extraen los filtros aprendidos de las primeras capas convolucionales y se visualizan. Tambien se calculan los mapas de activacion (feature maps): lo que "ve" la red en cada capa al procesar una imagen.

Esta visualizacion tiene valor pedagogico y diagnostico: permite entender que patrones aprendio la red y si los aprendio correctamente.

### Modelos preentrenados: ResNet18

ResNet18 es una red convolucional de 18 capas entrenada en ImageNet (1.2 millones de imagenes, 1000 clases). La arquitectura introduce conexiones residuales (skip connections) que permiten entrenar redes profundas sin el problema de gradientes que desaparecen.

Se usa el modelo en modo inferencia pura: se carga con pesos preentrenados y se clasifica imagenes nuevas sin reentrenar nada.

### Transferencia de aprendizaje con MobileNetV2

Transfer learning es la tecnica de tomar un modelo preentrenado y adaptarlo a una tarea nueva. El procedimiento es:

1. Cargar el modelo base (MobileNetV2) con pesos de ImageNet, **sin** la cabeza de clasificacion final.
2. Congelar las capas convolucionales (sus pesos no se actualizan durante el entrenamiento).
3. Agregar una nueva cabeza de clasificacion con las clases propias del problema.
4. Entrenar solo la nueva cabeza sobre el dataset propio.

Las capas convolucionales ya saben extraer caracteristicas generales de imagenes; solo hay que ensenale a la red a clasificar en las categorias nuevas.

### Modelos de Hugging Face: ViT, CLIP y DETR

Se trabajan tres arquitecturas distintas del ecosistema Hugging Face Transformers:

- **ViT (Vision Transformer):** aplica el mecanismo de atencion de los Transformers a imagenes divididas en patches. Se usa para clasificacion.
- **CLIP (Contrastive Language-Image Pretraining):** modelo multimodal entrenado con pares imagen-texto. Permite clasificacion zero-shot: clasificar sin haber visto ejemplos de la clase, solo con descripciones en texto natural.
- **DETR (Detection Transformer):** usa Transformers para deteccion de objetos. A diferencia de YOLO o Faster R-CNN, no necesita anchors ni NMS: predice un conjunto fijo de bounding boxes con un mecanismo de atencion.

Se usan con la API `pipeline` de Hugging Face, que abstrae la carga del modelo, el preprocesamiento y la inferencia en una sola linea.

### Construccion de demos con Gradio y Hugging Face Spaces

Se construye una interfaz web interactiva con Gradio para exponer un modelo como aplicacion. El flujo es:

1. Definir la funcion de inferencia.
2. Crear la interfaz con `gr.Interface` o `gr.Blocks`.
3. Publicar en Hugging Face Spaces con git (un repositorio especial que ejecuta el `app.py` automaticamente).

El proyecto publicado esta en `003 - LAB/rodriguez-carmen-pdi_Space_Gradio/`.

### OCR como investigacion critica

Se trabaja OCR (Optical Character Recognition) no solo como tecnica sino como objeto de analisis:

- Se prueban herramientas de OCR sobre distintos tipos de texto.
- Se evaluan los resultados con metricas de precision.
- Se investigan las condiciones en que falla (tipografia, orientacion, calidad de imagen, idioma).
- Se revisan las fuentes tecnicas (papers, documentacion) para entender las limitaciones declaradas por los propios autores.

## Archivos

### Practicas (`002 - PRA`)

| Archivo | Contenido |
|---|---|
| `01_Fundamentos_Red_Neuronal_Simple_colab.ipynb` | fundamentos en Colab |
| `01_Fundamentos_Red_Neuronal_Simple_visual.ipynb` | misma practica con visualizaciones locales |
| `02_Clasificacion_Letras_MLP.ipynb` | clasificacion con red densa (MLP) |
| `03_Clasificacion_Letras_CNN.ipynb` | clasificacion con red convolucional (CNN) |
| `04_Visualizacion_Filtros_y_Activaciones_CNN.ipynb` | extraccion y visualizacion de filtros y feature maps |
| `05_Clasificacion_Preentrenados_ResNet18.ipynb` | inferencia con ResNet18 preentrenado |
| `06_Transfer_Learning_MobileNetV2.ipynb` | fine-tuning de MobileNetV2 |
| `07_Modelos_Preentrenados_HuggingFace.ipynb` | ViT, CLIP zero-shot y DETR con pipeline de HF |

### Laboratorio (`003 - LAB`)

| Archivo/Carpeta | Contenido |
|---|---|
| `09_Laboratorio_Integrador_Redes.ipynb` | integracion de los conceptos del modulo |
| `10_Laboratorio_OCR_Investigacion_Critica.ipynb` | OCR con evaluacion critica de resultados y fuentes |
| `rodriguez-carmen-pdi_Space_Gradio/` | proyecto Gradio desplegado en Hugging Face Spaces |
| `rodriguez-carmen-pdi_Space_Gradio/app.py` | codigo de la aplicacion |
| `rodriguez-carmen-pdi_Space_Gradio/requirements.txt` | dependencias del Space |

## Librerias y herramientas

| Libreria | Uso en el modulo |
|---|---|
| `tensorflow` / `keras` | entrenamiento de MLP y CNN, transfer learning |
| `torch` / `torchvision` | inferencia con ResNet18 |
| `transformers` (Hugging Face) | ViT, CLIP, DETR con `pipeline` |
| `gradio` | interfaz web interactiva |
| `numpy` | operaciones sobre arrays |
| `matplotlib` | visualizacion de resultados y activaciones |
| `scikit-learn` | metricas de evaluacion (confusion matrix, accuracy) |
| `Pillow` (PIL) | carga y preprocesamiento de imagenes |

## Conexion con otros modulos

Las tecnicas de inferencia con modelos preentrenados y el patron de despliegue con Gradio se retoman en el modulo 009, donde se integran con MediaPipe para aplicaciones de vision en tiempo real.
