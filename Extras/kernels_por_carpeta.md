# Kernels recomendados por carpeta

## PDI - Entorno General

Entorno base del proyecto. Contiene OpenCV, NumPy, Matplotlib, PIL, py5 y librerías generales de procesamiento de imágenes.

**Carpetas y archivos:**

- **001 - py5** → `002 - PRA/jupyter/py5_on_Colab_demo.ipynb`
- **002 - py5** → todos los notebooks de `002 - PRA`
- **004 - librerias_fundamentos_pdi** → todos los notebooks de `002 - PRA` y `003 - LAB`
- **005 - computer_vision_parte_1** → todos los notebooks de `002 - PRA` y `003 - LAB`
- **006 - TFI_1** → `TFI_1_Mejora y restauracion de imagenes.ipynb`
- **007 - fotografia_digital** → todos los notebooks de `003 - LAB`

---

## TF - TensorFlow 2.17

Entorno con TensorFlow 2.17. Usado para los notebooks introductorios de redes neuronales.

**Archivos:**

- **008 - redes_neuronales_parte_1** / `002 - PRA`:
  - `001_Red_Neuronal.ipynb`
  - `002_Clasificacion.ipynb`
  - `003_CNNs_Full_visual.ipynb`

---

## TF - TensorFlow General

Entorno con TensorFlow 2.21 y Python 3.12 (venv312). Incluye los parches de compatibilidad para cargar modelos Keras 2.x. Usado para todos los notebooks de redes neuronales que corren localmente con datasets propios.

**Archivos:**

- **008 - redes_neuronales_parte_1** / `003 - LAB`:
  - `Teachable_Machine_Dataset_Propio_Gradio.ipynb`
- **008 - redes_neuronales_parte_2** / `002 - PRA`:
  - `01_Fundamentos_Red_Neuronal_Simple_visual.ipynb`
  - `02_Clasificacion_Letras_MLP.ipynb`
  - `03_Clasificacion_Letras_CNN.ipynb`
  - `04_Visualizacion_Filtros_y_Activaciones_CNN.ipynb`
  - `06_Transfer_Learning_MobileNetV2.ipynb`
- **008 - redes_neuronales_parte_2** / `003 - LAB`:
  - `08_Laboratorio_Desarrollo_Space_Gradio.ipynb`
  - `09_Laboratorio_Integrador_Redes.ipynb`
  - `10_Laboratorio_OCR_Investigacion_Critica.ipynb`
- **008 - redes_neuronales_parte_3** / `002 - PRA`:
  - `clasificador_frutas_extended.ipynb`
  - `comparacion_modelos.ipynb`
  - `crea_tu_propio_modelo_cnn.ipynb`
  - `probamos_el_modelo_con_camweb.ipynb`
  - `una_convolucion_por_dentro_random.ipynb`
  - `una_convolucion_por_dentro_train.ipynb`

---

## TF - Teachable Machine

Entorno dedicado para cargar y ejecutar modelos exportados desde Google Teachable Machine (formato `.h5` Keras 2.x). Usa `tf_keras` para mantener compatibilidad.

**Archivos:**

- **008 - redes_neuronales_parte_1** / `003 - LAB` / `notebook`:
  - `004_Teachable_Machine_Dataset_Propio_Gradio.ipynb`

---

## Vision Artificial Aplicada

Entorno con Python 3.12, MediaPipe 0.10.35 (Tasks API), OpenCV, Gradio, pycaw y comtypes. Creado para la unidad 009 porque MediaPipe eliminó `mp.solutions` en 0.10.13+ y los notebooks fueron reescritos para usar la Tasks API.

**Carpetas y archivos:**

- **009 - vision_artificial_aplicada** / `002 - PRA`:
  - `01_Detección_Puntos_Clave_Faciales.ipynb`
  - `02_Control_Volumen_con_Manos.ipynb`
  - `03_Integración_Gradio_y_MediaPipe.ipynb`
  - `04_Proyecto_Pose_y_Despliegue.ipynb`

> Nota: los notebooks 01 y 04 descargan automáticamente un archivo `.task` (~5-6 MB) la primera vez que se ejecuta la celda del detector (`face_landmarker.task` y `pose_landmarker_full.task`).

---

## PyTorch - ResNet18

Entorno con PyTorch y ResNet18 preentrenado.

**Archivos:**

- **008 - redes_neuronales_parte_2** / `002 - PRA`:
  - `05_Clasificacion_Preentrenados_ResNet18.ipynb`

---

## PyTorch - HuggingFace Vision

Entorno con PyTorch, Transformers y Diffusers de HuggingFace. Usado para modelos preentrenados de visión y modelos de difusión.

**Archivos:**

- **008 - redes_neuronales_parte_2** / `002 - PRA`:
  - `07_Modelos_Preentrenados_HuggingFace.ipynb`
- **010 - modelos_difusion** / `002 - PRA`:
  - `01_Introduccion_Conceptual_Difusion.ipynb`
  - `02_Paradigmas_y_Modelos_Difusion.ipynb`
  - `03_Aplicaciones_Practicas_Difusion.ipynb`
  - `04_Text_to_Image_SDXL_Turbo.ipynb`
  - `05_Text_to_Image_SDXS_CPU.ipynb`
  - `06_Aceleracion_LCM_LoRA.ipynb`
- **011 - clase magistral_dev_despliegue** / `002 - PRA` / `notebooks`:
  - `05_Modelos_Preentrenados_HuggingFace.ipynb`

---

## Notebooks diseñados para Google Colab

Estos archivos están pensados para ejecutarse en Colab, no localmente. Si se abren en VS Code, el kernel no importa porque el código no va a funcionar sin el entorno de Colab.

- **001 - py5** / `002 - PRA` / `jupyter`: `py5_on_Colab_demo.ipynb`
- **002 - py5** / `002 - PRA`: `00_setup_colab.ipynb`, `02a_fundamentos_teoria_colab.ipynb`, `02c_laboratorio_fundamentos.ipynb`
- **008 - redes_neuronales_parte_1** / `002 - PRA`: `003_CNNs_Full_colab.ipynb`
- **008 - redes_neuronales_parte_2** / `002 - PRA`: `01_Fundamentos_Red_Neuronal_Simple_colab.ipynb`
- **008 - redes_neuronales_parte_3** / `002 - PRA`: `prueba_colab_desde_folder.ipynb`

### 010 - modelos_difusion: notebooks que requieren GPU

Este equipo no tiene GPU (CUDA no disponible). Los siguientes notebooks de la unidad 010 se pueden abrir con `PyTorch - HuggingFace Vision` pero corren a velocidad impráctica en CPU — se recomienda usar los botones **Open in Colab** del README de la carpeta:

- `02_Paradigmas_y_Modelos_Difusion.ipynb` — carga SD-Turbo (~4 GB), lento en CPU
- `03_Aplicaciones_Practicas_Difusion.ipynb` — inpainting y upscaler, muy lento en CPU
- `04_Text_to_Image_SDXL_Turbo.ipynb` — SDXL 1024×1024, requiere 8 GB VRAM
- `06_Aceleracion_LCM_LoRA.ipynb` — SDXL + LCM-LoRA, requiere 6 GB VRAM

Los notebooks `01_Introduccion_Conceptual_Difusion.ipynb` (solo visualizaciones matemáticas) y `05_Text_to_Image_SDXS_CPU.ipynb` (diseñado explícitamente para CPU) funcionan bien de forma local con `PyTorch - HuggingFace Vision`.
