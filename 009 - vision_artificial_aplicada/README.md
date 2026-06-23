# Modulo 009 — Vision artificial aplicada

## Que se estudia en este modulo

Este modulo trabaja vision artificial en tiempo real con MediaPipe, una libreria de Google que provee pipelines de deteccion y seguimiento de estructuras corporales (cara, manos, cuerpo completo) optimizados para ejecucion en CPU.

El eje del modulo es la cadena completa: capturar video, detectar landmarks, procesar la informacion geometrica y exponer el resultado como una aplicacion interactiva con Gradio. Se pasa de la inferencia aislada a la construccion de herramientas funcionales.

## Conceptos clave

### Landmarks y modelos de MediaPipe

MediaPipe no devuelve una imagen clasificada sino un conjunto de **landmarks**: puntos en coordenadas normalizadas (0.0 a 1.0) que representan estructuras anatomicas especificas. Cada modelo tiene su propio conjunto:

- **Face Mesh:** 478 landmarks que cubren toda la superficie del rostro (cejas, parpados, nariz, labios, contorno facial).
- **Hand Landmarker:** 21 landmarks por mano (falange proximal, media y distal de cada dedo + muneca y nudillos).
- **Pose Landmarker:** 33 landmarks corporales (hombros, codos, munecas, caderas, rodillas, tobillos, orejas, ojos).

Los archivos `.task` (por ejemplo, `face_landmarker.task`, `hand_landmarker.task`) son los modelos preentrenados en formato TFLite que MediaPipe carga en tiempo de ejecucion.

### Geometria de landmarks

Los landmarks son coordenadas en el espacio de la imagen normalizado. Para convertirlos a pixeles se multiplican por el ancho y el alto del frame. A partir de ahi se pueden calcular:

- **Distancias entre puntos:** con norma euclidiana entre coordenadas.
- **Angulos:** usando el producto punto entre vectores formados por tres landmarks.
- **Gestos:** combinaciones de distancias y angulos que corresponden a configuraciones especificas de la mano o el cuerpo.

### Control de volumen por gestos

Se mide la distancia entre los landmarks del pulgar (punta, id=4) y el indice (punta, id=8). Esa distancia se mapea al rango de volumen del sistema operativo usando la API de audio de Windows (`pycaw` + `comtypes`). El loop captura el frame, detecta la mano, calcula la distancia y ajusta el volumen en tiempo real.

### Patron de Skills en Gradio

Se introduce el concepto de **Skill** como una unidad de procesamiento encapsulada: una funcion que toma una imagen, aplica un modelo y devuelve un resultado (imagen anotada, texto, valor). Las Skills se componen en interfaces `gr.Interface` o `gr.Blocks` para construir aplicaciones mas complejas.

`gr.Interface` es la forma mas simple: una funcion, inputs y outputs. `gr.Blocks` permite layouts personalizados, multiples funciones, estados y eventos mas complejos.

### Estimacion de pose y despliegue

Se construye una aplicacion que detecta la pose corporal en tiempo real y se despliega en Hugging Face Spaces. El proceso de deploy con git es:

1. Crear un Space en Hugging Face (tipo Gradio).
2. Clonar el repositorio del Space localmente.
3. Copiar `app.py` y `requirements.txt`.
4. Hacer push al repositorio del Space.
5. HF ejecuta automaticamente la aplicacion.

## Archivos

### Practicas (`002 - PRA`)

| Archivo | Contenido |
|---|---|
| `01_Deteccion_Puntos_Clave_Faciales_original.ipynb` | Face Mesh: 478 landmarks sobre imagen estatica |
| `01_Deteccion_Puntos_Clave_Faciales_grupo.ipynb` | version trabajada en clase |
| `01_Deteccion_Puntos_Clave_Faciales_dos_comentado.ipynb` | version comentada y ampliada |
| `02_Control_Volumen_con_Manos.ipynb` | Hand Landmarker + control de volumen en Windows |
| `03_Integracion_Gradio_y_MediaPipe.ipynb` | Skills, gr.Interface y gr.Blocks con Face Mesh |
| `04_Proyecto_Pose_y_Despliegue.ipynb` | Pose estimation + deploy en Hugging Face Spaces |
| `face_landmarker.task` | modelo preentrenado de Face Mesh (TFLite) |
| `hand_landmarker.task` | modelo preentrenado de Hand Landmarker (TFLite) |

### Laboratorio (`003 - LAB`)

| Archivo/Carpeta | Contenido |
|---|---|
| `Analisis_Avanzado_Landmarks_Faciales.ipynb` | analisis geometrico de landmarks faciales |
| `Integracion_Gradio_MediaPipe.ipynb` | integracion avanzada de modelos con Gradio |
| `Variantes_Control_Volumen.ipynb` | variantes del control de volumen |
| `Pose_Despliegue/` | proyecto de pose listo para despliegue |

## Librerias y herramientas

| Libreria | Uso en el modulo |
|---|---|
| `mediapipe` | deteccion de face mesh, manos y pose |
| `opencv-python` (cv2) | captura de video, dibujado de landmarks sobre frames |
| `gradio` | construccion de interfaces web interactivas |
| `pycaw` + `comtypes` | control de volumen del sistema (solo Windows) |
| `numpy` | operaciones geometricas sobre coordenadas de landmarks |
| `Pillow` (PIL) | conversion de formatos de imagen para Gradio |

## Entorno virtual

Este modulo usa el entorno `.venv_vision_aplicada/` en la raiz del proyecto. Para activarlo en Windows:

```powershell
.\.venv_vision_aplicada\Scripts\Activate.ps1
```

Ver el README de `002 - PRA/` para instrucciones completas de instalacion con `uv`.

## Nota sobre el notebook de control de volumen

`02_Control_Volumen_con_Manos.ipynb` usa la API de audio de Windows. En Linux y macOS el loop de deteccion funciona pero el control de volumen del sistema requiere configuracion adicional.

## Conexion con otros modulos

El patron de despliegue con Gradio + Hugging Face introducido en el modulo 008-parte2 se consolida aqui con aplicaciones de vision en tiempo real. La arquitectura de Skills que se define en este modulo es la base de las aplicaciones desarrolladas en el modulo 011.
