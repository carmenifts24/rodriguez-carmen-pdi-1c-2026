# Laboratorio de Fundamentos de Procesamiento Digital de Imagenes

**IFTS N. 24 - Ciencia de Datos e Inteligencia Artificial**  
**3.er ano - 1.er cuatrimestre 2026**

Repositorio personal de trabajo para la cursada de Procesamiento Digital de Imagenes. Reune apuntes, practicas, laboratorios y material complementario desarrollado durante la materia.

## Que contiene este repositorio

El material esta organizado por unidades numeradas. En cada unidad se separan, cuando corresponde:

- `001 - TEO`: teoria, presentaciones y material de catedra
- `002 - PRA`: practicas, notebooks y ejercicios guiados
- `003 - LAB`: trabajos de laboratorio, actividades integradoras o entregas
- `Extras`: guias de instalacion, uso diario y documentacion complementaria

Estado actual del recorrido:

- `001 - py5`: introduccion a programacion visual con `py5`
- `002 - py5`: fundamentos de imagen digital e interaccion visual
- `003 - camara_oscura`: registro y material de trabajo asociado a la experiencia de camara oscura
- `004 - librerias_fundamentos_pdi`: procesamiento con librerias de Python, segmentacion y preprocesamiento
- `005 - computer_vision_parte_1`: vision por computadora clasica con OpenCV
- `006 - TFI_1`: trabajo final integrador de mejora y restauracion de imagenes
- `007 - fotografia_digital`: trabajo practico complementario sobre lenguaje fotografico y composicion visual
- `008 - redes_neuronales_parte_1`: primera introduccion a redes neuronales, clasificacion de imagenes y CNNs
- `008 - redes_neuronales_parte_2`: modelos preentrenados, transferencia de aprendizaje, Hugging Face, Spaces y OCR
- `008 - redes_neuronales_parte_3`: entrenamiento y comparacion de CNNs propias, visualizacion de convoluciones
- `009 - vision_artificial_aplicada`: deteccion de puntos clave con MediaPipe, control gestual e integracion con Gradio
- `010 - modelos_difusion`: modelos generativos de difusion, text-to-image y aceleracion con LCM-LoRA
- `011 - clase magistral_dev_despliegue`: entornos de desarrollo, Docker, despliegue en Hugging Face Spaces

## Tecnologias y librerias

Principales librerias usadas en la cursada:

- `numpy`
- `scipy`
- `opencv-python`
- `scikit-image`
- `Pillow`
- `matplotlib`
- `pandas`
- `jupyter`
- `ipykernel`
- `py5`
- `tensorflow`
- `tensorflow-datasets`
- `scikit-learn`
- `seaborn`
- `torch`
- `torchvision`
- `transformers`
- `gradio`
- `gdown`
- `mediapipe`
- `diffusers`

Nota: `py5` requiere Java. Si aparece un error relacionado con Java, conviene revisar la documentacion oficial de instalacion de `py5`.

Nota sobre redes neuronales: las unidades `008`, `009` y `010` pueden descargar datasets o pesos preentrenados desde internet. Para entrenamientos pesados, inferencia con modelos grandes o acceso a camara/webcam, Google Colab puede ser mas comodo que la ejecucion local.

Nota sobre modelos de difusion: la unidad `010` es especialmente exigente en hardware. Se recomienda ejecutar en Google Colab con GPU T4 o superior.

## Instalacion local

### 1. Clonar el repositorio

```bash
git clone https://github.com/carmenifts24/rodriguez-carmen-pdi-1c-2026.git
cd rodriguez-carmen-pdi-1c-2026
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
```

En Windows, si `python` no funciona, probar:

```bash
py -m venv venv
```

### 3. Activar el entorno

PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

CMD:

```bat
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

Si PowerShell bloquea la activacion:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 4. Instalar dependencias

```bash
python -m pip install -r requirements.txt
```

### 5. Verificar librerias principales

```bash
python -c "import cv2, numpy, PIL, matplotlib, pandas; print('Librerias principales OK')"
python -c "import py5; print('py5 OK')"
python -c "import tensorflow, sklearn, gradio; print('Redes neuronales basicas OK')"
```

### Entornos por unidad

Las unidades mas recientes (`009`, `010`, `011`) usan entornos virtuales propios dentro de su carpeta. Cada una incluye un `README.md` con instrucciones especificas. Los entornos activos en el proyecto son:

| Entorno | Uso |
|---|---|
| `venv/` | entorno general, unidades 001–008 |
| `venv312/` | Python 3.12, TensorFlow y variantes |
| `venv_tf/` | TensorFlow especifico |
| `.venv_teachable/` | Teachable Machine + Gradio |
| `.venv_pytorch_resnet18/` | PyTorch + ResNet18 |
| `.venv_pytorch_huggingface_vision/` | PyTorch + HuggingFace Vision |
| `.venv_vision_aplicada/` | unidad 009 — MediaPipe + Gradio |

## Guias utiles incluidas

En la carpeta `Extras` hay documentacion pensada para uso practico:

- `Extras/instalacion_inicial.md`: puesta en marcha desde cero en otra computadora
- `Extras/referencia_trabajo_diario.md`: comandos de uso frecuente y resolucion de problemas comunes
- `Extras/actualizar_github.md`: pasos para subir cambios al repositorio
- `Extras/alternar_github.md`: notas de trabajo con remotos y cuentas GitHub

## Estructura actual del proyecto

```text
rodriguez-carmen-pdi-1c-2026/
|-- README.md
|-- requirements.txt
|-- tools/
|-- 001 - py5/
|   |-- 001 - TEO/
|   |-- 002 - PRA/
|   `-- 003 - LAB/
|-- 002 - py5/
|   |-- 001 - TEO/
|   |-- 002 - PRA/
|   `-- 003 - LAB/
|-- 003 - camara_oscura/
|   |-- 001 - TEO/
|   |-- 002 - PRA/
|   `-- 003 - LAB/
|-- 004 - librerias_fundamentos_pdi/
|   |-- 001 - TEO/
|   |-- 002 - PRA/
|   `-- 003 - LAB/
|-- 005  - computer_vision_parte_1/
|   `-- 002 - PRA/
|-- 006 - TFI_1/
|   |-- imagenes_tfi1/
|   |-- salidas_tfi1/
|   |-- README.md
|   |-- dashboard_tfi1_tecnicas.html
|   |-- TFI_1_Consigna_y_Rubrica.md
|   `-- TFI_1_Mejora y restauracion de imagenes.ipynb
|-- 007 - fotografia_digital/
|   |-- README.md
|   |-- De la camara oscura a la imagen intencional.pdf
|   |-- 002_codigo/
|   `-- 003_recursos/
|-- 008 - redes_neuronales_parte_1/
|   |-- README.md
|   |-- 001 - TEO/
|   |-- 002 - PRA/
|   `-- 003 - LAB/
|-- 008 - redes_neuronales_parte_2/
|   |-- 001 - TEO/
|   |-- 002 - PRA/
|   `-- 003 - LAB/
|       |-- 09_Laboratorio_Integrador_Redes.ipynb
|       |-- 10_Laboratorio_OCR_Investigacion_Critica.ipynb
|       `-- rodriguez-carmen-pdi_Space_Gradio/
|-- 008 - redes_neuronales_parte_3/
|   |-- 001 - TEO/
|   |-- 002 - PRA/
|   `-- 003 - LAB/
|-- 009 - vision_artificial_aplicada/
|   |-- 001 - TEO/
|   |-- 002 - PRA/
|   `-- 003 - LAB/
|-- 010 - modelos_difusion/
|   |-- 001 - TEO/
|   |-- 002 - PRA/
|   `-- 003 - LAB/
|-- 011 - clase magistral_dev_despliegue/
|   |-- 001 - TEO/
|   |-- 002 - PRA/
|   `-- 003 - LAB/
`-- Extras/
```

## Resumen por unidad

### 001 - py5

Unidad centrada en la introduccion a `py5` y a la programacion visual.

Incluye ejercicios de:

- creacion de ventanas y sketches basicos
- color en `RGB` y `HSV/HSB`
- carga y visualizacion de imagenes
- manipulacion manual de pixeles
- filtros visuales
- interaccion con mouse
- dibujo generativo

Archivos destacados en `001 - py5/002 - PRA`:

- `000_intro_py5.py`
- `001_basico.py`
- `001b_basico_HSV.py`
- `001c_hsv_gradiente.py`
- `002_info.py`
- `002b_info_visual.py`
- `003_RGB.py`
- `004_HSV.py`
- `005_upload_img.py`
- `006_pixeles.py`
- `007_pixeles.py`
- `008_filtro.py`
- `009_mouse.py`
- `009b_mouse.py`
- `009c_mouse.py`
- `010_filtro.py`
- `011_filtro.py`
- `012_filtro.py`
- `013_filtro.py`
- `014_filtro.py`
- `015_dibujo.py`

En `001 - py5/003 - LAB` se encuentra:

- `2026_PDI_RODRIGUEZ_CARMEN.py`

Material complementario:

- `001 - py5/002 - PRA/README.md`
- `001 - py5/002 - PRA/py5_referencia.md`
- `001 - py5/002 - PRA/jupyter/`

### 002 - py5

Unidad orientada a fundamentos de imagen digital y primera articulacion entre teoria, practica y laboratorio.

En `002 - py5/002 - PRA` hay:

- `00_setup_colab.ipynb`
- `02a_fundamentos_teoria_colab.ipynb`
- `02a_fundamentos_teoria_local.ipynb`
- `02b_fundamentos_practica_local.ipynb`
- `02c_laboratorio_fundamentos.ipynb`
- `canal_mouse.py`
- `lupa.py`

En `002 - py5/003 - LAB` se encuentran:

- `2026_PDI_RODRIGUEZ_canal_mouse.py`
- `2026_PDI_RODRIGUEZ_lupa.py`

Temas trabajados:

- lectura inicial de imagen digital
- diferencia entre teoria en Colab y trabajo local
- exploracion de canales de color
- interaccion con el mouse sobre imagenes
- zoom o efecto lupa sobre regiones de interes

### 003 - camara_oscura

Unidad destinada al registro de la experiencia de camara oscura y a la produccion de imagenes propias usadas luego en otras actividades.

En `003 - camara_oscura/003 - LAB` hay material de referencia y archivos asociados a la experiencia.

Este material se articula especialmente con la unidad `004`, donde se trabaja recuperacion, preprocesamiento y segmentacion sobre imagenes propias.

### 004 - librerias_fundamentos_pdi

Unidad enfocada en el uso de librerias de procesamiento de imagenes mas alla de `py5`.

Notebooks y archivos de practica en `004 - librerias_fundamentos_pdi/002 - PRA`:

- `001 - entorno y librerias.ipynb`
- `002 - imagenes en color y canales.ipynb`
- `003 - operaciones basicas con opencv.ipynb`
- `004 - muestreo y cuantizacion.ipynb`
- `005 - practica guiada de procesamiento de imagenes.ipynb`
- `006 - laboratorio 2 - segmentacion simple por color.ipynb`
- `007 - recuperacion y preprocesamiento de imagenes propias.ipynb`
- `008 - actividad integradora - segmentacion por color.ipynb`

Material de laboratorio desarrollado en `004 - librerias_fundamentos_pdi/003 - LAB`:

- `2026_PDI_RODRIGUEZ_proc_digital.ipynb`
- `2026_PDI_RODRIGUEZ_segmentac_color.ipynb`
- `2026_PDI_RODRIGUEZ_ rec_preproc_imag_propias.ipynb`
- `2026_PDI_RODRIGUEZ_ integrador_segmentacion por color.ipynb`

Temas trabajados:

- preparacion del entorno de trabajo con librerias
- lectura y visualizacion de imagenes con OpenCV
- analisis de canales e histogramas
- operaciones basicas sobre imagenes
- muestreo y cuantizacion
- segmentacion simple por color
- recuperacion y preprocesamiento de imagenes propias

### 005 - computer_vision_parte_1

Unidad enfocada en herramientas clasicas de vision por computadora sobre imagenes reales y sinteticas.

Notebooks de practica en `005  - computer_vision_parte_1/002 - PRA`:

- `001 - introduccion a opencv y espacios de color.ipynb`
- `001B - practicas_hsv.ipynb`
- `001C  - rueda cromatica.ipynb`
- `002 - formatos de archivos de imagen.ipynb`
- `003 - mejora de imagen y ecualizacion basica.ipynb`
- `003B - mejora de imagen y ecualizacion basica img1.ipynb`
- `004 - comparacion de estrategias de ecualizacion.ipynb`
- `004b - operaciones basicas con imagenes.ipynb`
- `004C - operaciones basicas con imagenes actividad.ipynb`
- `005 - transformaciones geometricas y cambio de perspectiva.ipynb`
- `006 - operaciones graficas.ipynb`
- `006b - filtros de suavizado y reduccion de ruido.ipynb`
- `006c - morfologia matematica para limpieza de mascaras.ipynb`
- `006d - restauracion y algoritmos de inpainting.ipynb`
- `007 - deteccion de contornos.ipynb`
- `008 - propiedades geometricas de contornos.ipynb`
- `009 - coincidencia por plantilla.ipynb`
- `010 - deteccion de rostros con haar.ipynb`
- `Utilidades_y_Plantillas.ipynb`

Tambien hay recursos de apoyo:

- carpeta `Imagenes/`
- carpeta `exploratorios/`
- versiones auxiliares `*_error.ipynb` creadas durante ajustes locales

Temas trabajados:

- espacios de color y segmentacion HSV
- formatos de imagen
- mejora de imagen y ecualizacion
- operaciones basicas y geometricas
- suavizado y reduccion de ruido
- morfologia matematica
- inpainting
- deteccion y medicion de contornos
- coincidencia por plantilla
- deteccion de rostros con cascadas Haar

### 006 - TFI_1

Unidad de integracion y cierre parcial del recorrido. El trabajo consiste en construir tres pipelines acotados de mejora y restauracion, comparar estrategias y justificar la decision final para cada tipo de imagen.

Archivos principales:

- `TFI_1_Consigna_y_Rubrica.md`: consigna, restricciones, entregables y rubrica de evaluacion.
- `TFI_1_Mejora y restauracion de imagenes.ipynb`: notebook de resolucion del trabajo.
- `README.md`: resumen especifico del TFI, casos trabajados, tecnicas usadas y limites.
- `dashboard_tfi1_tecnicas.html`: tablero visual con tecnicas aplicadas, explicacion de uso y referencias de busqueda dentro del proyecto.
- `imagenes_tfi1/`: imagenes originales seleccionadas.
- `salidas_tfi1/`: resultados finales procesados.
- `imagenes seleccionadas.pptx`: apoyo visual usado para comparar imagenes candidatas.

Casos resueltos:

- Camara oscura: `CajaOscura 7.png`
- Medio grafico color: `UDO sola.jpeg`
- Medio grafico blanco/negro: `DreamTeam ByN.jpeg`

Tecnicas integradas:

- diagnostico por observacion, canales e histogramas
- rotacion, recorte y comparacion visual
- ajuste lineal de brillo y contraste
- conversion entre `RGB`, `HSV`, `LAB` y gris
- `CLAHE` para contraste local
- suavizado gaussiano y filtro bilateral
- ecualizacion global del histograma
- morfologia matematica para mascaras de dano
- `inpainting` puntual
- guardado de salidas finales y tabla comparativa con `pandas`

### 007 - fotografia_digital

Trabajo practico complementario sobre lenguaje fotografico aplicado. Todas las imagenes fueron capturadas por la estudiante. El trabajo integra teoria fotografica y procesamiento digital en cinco partes:

- **Parte 1 - Camara oscura:** retoma la imagen capturada con camara oscura artesanal. Se aplica rotacion, recorte y ecualizacion del canal `V` en espacio `HSV` para mejorar el contraste sin distorsionar los colores.
- **Parte 2 - Composicion y lenguaje visual:** reencuadre compositivo, conversion a escala de grises, binarizacion con umbral de Otsu y ecualizacion de histograma para analizar como la forma prevalece sobre el color.
- **Parte 3 - Reencuadre y reinterpretacion:** a partir de una unica imagen amplia se generan dos recortes con lecturas intencionalmente distintas (arquitectonica y narrativa), demostrando como el encuadre construye sentido.
- **Parte 4 - Punto de vista:** comparacion de dos fotografias del mismo sujeto desde distintas posiciones para analizar escala, contexto y relacion emocional.
- **Parte 5 - Fotografia basada en la luz:** analisis cuantitativo (luminosidad, contraste, rango, histograma) de cuatro fotografias en distintas condiciones de luz, con seleccion y esquema anotado de direccion de luz.

Archivos principales:

- `002_codigo/Trabajo Practico 006 - Fotografia Digital.ipynb`: notebook de resolucion
- carpetas de recursos fotograficos y documentos en `003_recursos/`
- `De la camara oscura a la imagen intencional.pdf`: presentacion conceptual del recorrido
- `README.md`: documentacion especifica del trabajo

Tecnicas aplicadas:

- conversion `RGB` → `HSV` y ecualizacion selectiva por canal
- umbral de Otsu para binarizacion automatica
- ecualizacion global del histograma en escala de grises
- analisis de metricas de luminosidad y contraste con `numpy` y `pandas`
- visualizacion comparativa y anotacion de mapas de reencuadre con `matplotlib`

### 008 - redes_neuronales_parte_1

Unidad de entrada a redes neuronales con foco didactico. Parte de una regresion simple de Celsius a Fahrenheit, avanza hacia clasificacion de letras y culmina con CNNs para imagenes y una actividad con Teachable Machine + Gradio.

Notebooks en `008 - redes_neuronales_parte_1/002 - PRA`:

- `001_Red_Neuronal.ipynb`: primera red neuronal y lectura de pesos aprendidos.
- `002_Clasificacion.ipynb`: clasificacion multiclase de letras manuscritas.
- `003_CNNs_Full_colab.ipynb`: CNNs sobre MNIST y `cats_vs_dogs` en Colab.
- `003_CNNs_Full_visual.ipynb`: version con visualizaciones locales.

Temas trabajados:

- normalizacion de datos y separacion entrenamiento/prueba
- redes densas y redes convolucionales
- matrices de confusion e interpretacion de errores
- sesgo de dataset, fondos, iluminacion y variacion de encuadre
- despliegue didactico de clasificadores con Gradio

### 008 - redes_neuronales_parte_2

Unidad de profundizacion en redes neuronales para imagenes. Suma modelos preentrenados, transferencia de aprendizaje, Hugging Face, Spaces, Gradio y OCR con investigacion critica.

Notebooks en `008 - redes_neuronales_parte_2/002 - PRA`:

- `01_Fundamentos_Red_Neuronal_Simple_colab.ipynb`
- `01_Fundamentos_Red_Neuronal_Simple_visual.ipynb`
- `02_Clasificacion_Letras_MLP.ipynb`
- `03_Clasificacion_Letras_CNN.ipynb`
- `04_Visualizacion_Filtros_y_Activaciones_CNN.ipynb`
- `05_Clasificacion_Preentrenados_ResNet18.ipynb`
- `06_Transfer_Learning_MobileNetV2.ipynb`
- `07_Modelos_Preentrenados_HuggingFace.ipynb`

Laboratorios en `008 - redes_neuronales_parte_2/003 - LAB`:

- `09_Laboratorio_Integrador_Redes.ipynb`
- `10_Laboratorio_OCR_Investigacion_Critica.ipynb`
- `rodriguez-carmen-pdi_Space_Gradio/`: proyecto Gradio desplegado en Hugging Face Spaces.

Temas trabajados:

- comparacion MLP vs CNN
- visualizacion de filtros y activaciones
- inferencia con ResNet18, ViT, CLIP y DETR
- transferencia de aprendizaje con MobileNetV2
- construccion de demos con Gradio y Hugging Face Spaces
- OCR como caso de investigacion tecnica y validacion de fuentes

### 008 - redes_neuronales_parte_3

Unidad orientada a experimentacion con CNNs propias para clasificacion de frutas y comprension interna de las convoluciones. Incluye notebooks de entrenamiento, comparacion de arquitecturas, prueba con camara y visualizacion de filtros reales o aleatorios.

Archivos en `008 - redes_neuronales_parte_3/002 - PRA`:

- `clasificador_frutas_extended.ipynb`: entrenamiento extendido de CNN para naranjas y manzanas.
- `comparacion_modelos.ipynb`: comparacion de modelos y estrategias.
- `crea_tu_propio_modelo_cnn.ipynb`: plantilla configurable para construir una CNN propia.
- `probamos_el_modelo_con_camweb.ipynb`: prueba interactiva con camara en Colab.
- `prueba_colab_desde_folder.ipynb`: flujo de entrenamiento/validacion desde carpeta.
- `una_convolucion_por_dentro_random.ipynb`: visualizacion pedagogica de filtros aleatorios.
- `una_convolucion_por_dentro_train.ipynb`: visualizacion de filtros aprendidos por un modelo entrenado.

Temas trabajados:

- preparacion de datasets de imagenes por carpeta
- entrenamiento y evaluacion de CNNs propias
- comparacion de arquitecturas y metricas
- inspeccion de filtros, activaciones y max pooling
- prueba de inferencia con imagenes reales o camara web

### 009 - vision_artificial_aplicada

Unidad centrada en vision artificial en tiempo real con MediaPipe. Trabaja deteccion de puntos clave faciales, control gestual con las manos, estimacion de pose e integracion de modelos de vision con interfaces web.

Notebooks en `009 - vision_artificial_aplicada/002 - PRA`:

- `01_Deteccion_Puntos_Clave_Faciales_original.ipynb`: Face Mesh con 478 landmarks sobre imagen estatica.
- `01_Deteccion_Puntos_Clave_Faciales_grupo.ipynb`: version trabajada en clase.
- `01_Deteccion_Puntos_Clave_Faciales_dos_comentado.ipynb`: version comentada y ampliada.
- `02_Control_Volumen_con_Manos.ipynb`: Hand Landmarker para control de volumen en tiempo real.
- `03_Integracion_Gradio_y_MediaPipe.ipynb`: concepto de Skills, `gr.Interface` y `gr.Blocks` con MediaPipe.
- `04_Proyecto_Pose_y_Despliegue.ipynb`: estimacion de pose + deploy en Hugging Face Spaces.

Laboratorios en `009 - vision_artificial_aplicada/003 - LAB`:

- `Analisis_Avanzado_Landmarks_Faciales.ipynb`
- `Integracion_Gradio_MediaPipe.ipynb`
- `Variantes_Control_Volumen.ipynb`
- `Pose_Despliegue/`: proyecto de pose para despliegue.

Temas trabajados:

- deteccion de landmarks faciales, de manos y de pose con MediaPipe
- control de volumen del sistema mediante gestos (Windows)
- construccion de Skills como unidades de procesamiento reutilizables
- integracion de MediaPipe con `gr.Interface` y `gr.Blocks`
- despliegue de aplicaciones de vision en Hugging Face Spaces

Entorno: `.venv_vision_aplicada/`. Ver `002 - PRA/README.md` para instrucciones de instalacion con `uv`.

### 010 - modelos_difusion

Unidad sobre modelos generativos de difusion. Cubre desde los fundamentos teoricos hasta la aceleracion mediante LCM-LoRA y la generacion text-to-image optimizada para CPU y GPU. Los notebooks estan disenados para ejecutarse en Google Colab con GPU T4.

Notebooks en `010 - modelos_difusion/002 - PRA`:

- `01_Introduccion_Conceptual_Difusion.ipynb`: fundamentos y visualizacion del proceso forward/reverse.
- `02_Paradigmas_y_Modelos_Difusion.ipynb`: del paradigma tradicional al generativo, historia y primer demo.
- `03_Aplicaciones_Practicas_Difusion.ipynb`: inpainting, super-resolution e image-to-image.
- `04_Text_to_Image_SDXL_Turbo.ipynb`: inferencia ultra-rapida de 1024x1024 en un solo paso.
- `05_Text_to_Image_SDXS_CPU.ipynb`: generacion text-to-image de baja latencia optimizada para CPU.
- `06_Aceleracion_LCM_LoRA.ipynb`: Latent Consistency Models y adaptacion de bajo rango (LoRA).

Temas trabajados:

- proceso de difusion forward y reverse
- DDPM, DDIM y schedulers
- pipelines de `diffusers` para text-to-image, inpainting y super-resolution
- SDXL Turbo, SDXS y LCM-LoRA para inferencia rapida
- optimizaciones de memoria para GPU con poca VRAM y ejecucion en CPU

Nota: la instalacion local requiere descargar modelos de 1 a 7 GB. Ver `002 - PRA/README.md` para instrucciones.

### 011 - clase magistral_dev_despliegue

Clase magistral sobre entornos de desarrollo, contenerizacion con Docker y despliegue de aplicaciones de vision artificial. Integra MediaPipe, Gradio y modelos de Hugging Face en un flujo completo de desarrollo y despliegue.

Notebooks en `011 - clase magistral_dev_despliegue/002 - PRA/notebooks`:

- `01_Entornos_de_Desarrollo.ipynb`: entornos virtuales vs Docker, cuando usar cada uno.
- `02_Control_Volumen_con_Manos.ipynb`: Hand Landmarker + control de volumen en tiempo real.
- `03_Integracion_Gradio_y_MediaPipe.ipynb`: Skills, `gr.Interface`, `gr.Blocks` y Face Mesh en Gradio.
- `04_Proyecto_Pose_y_Despliegue.ipynb`: MediaPipe Pose + deploy en Hugging Face Spaces.
- `05_Modelos_Preentrenados_HuggingFace.ipynb`: ViT, CLIP (zero-shot) y DETR con `pipeline` de HF.
- `06_Cheatsheet_Desarrollo_Space.ipynb`: referencia rapida de git, Gradio, Transformers y arquitectura 3 capas.

Infraestructura en `011 - clase magistral_dev_despliegue/002 - PRA`:

- `Dockerfile` + `docker-compose.yml`: entorno JupyterLab listo para levantar con `docker compose up`.
- `requirements.txt`: dependencias del contenedor.
- `mi-pose-app/`: proyecto de pose para despliegue.

Temas trabajados:

- gestion de entornos virtuales y contenerizacion con Docker
- deteccion de landmarks de manos, cara y pose con MediaPipe
- construccion de interfaces con `gr.Interface` y `gr.Blocks`
- inferencia con modelos ViT, CLIP y DETR desde Hugging Face
- despliegue en Hugging Face Spaces con git y doble remote (GitHub + HF)

## Como trabajar con el material

### Scripts `.py`

- activar el entorno virtual
- abrir la carpeta completa del proyecto en VS Code
- ejecutar el archivo desde VS Code o desde terminal con `python archivo.py`

### Notebooks `.ipynb`

- abrir el notebook en VS Code o Jupyter
- verificar que el kernel seleccionado sea el del `venv` correspondiente a la unidad
- ejecutar las celdas en orden

### Google Colab

Algunos notebooks estan preparados para trabajo en Colab, especialmente los que ya lo indican en el nombre o incluyen una celda de setup. La unidad `010 - modelos_difusion` esta disenada exclusivamente para Colab con GPU.

### Docker (unidad 011)

```bash
# Primera vez — construye la imagen (~10 min por torch)
docker compose up --build

# Las siguientes veces
docker compose up
```

Abre http://localhost:8888 — token: `clase`

## Problemas frecuentes

### PowerShell no deja activar el entorno virtual

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1
```

### Faltan modulos como `cv2`, `numpy` o `PIL`

```bash
python -m pip install -r requirements.txt
```

### VS Code o Jupyter usan otro interprete

Seleccionar:

```text
.\venv\Scripts\python.exe
```

### `py5` falla al iniciar

Primero probar:

```bash
python -m pip install glfw
```

Si el error menciona Java, instalar Java y revisar la guia oficial de `py5`.

### MediaPipe no encuentra la camara

Verificar que el entorno activo sea `.venv_vision_aplicada` y que los archivos `.task` de MediaPipe esten en la misma carpeta que el notebook.

## Recursos

- OpenCV: <https://docs.opencv.org/>
- NumPy: <https://numpy.org/doc/>
- Matplotlib: <https://matplotlib.org/>
- scikit-image: <https://scikit-image.org/docs/>
- py5: <https://py5coding.org/>
- Instalacion de py5: <https://py5coding.org/content/install.html>
- MediaPipe: <https://ai.google.dev/edge/mediapipe/solutions/guide>
- Diffusers: <https://huggingface.co/docs/diffusers/>
- Hugging Face: <https://huggingface.co/docs>
- Google Colab: <https://colab.research.google.com/>

## Licencia

Material de uso educativo para la cursada. Si mas adelante se define una licencia especifica para la materia, conviene agregarla en este archivo.
