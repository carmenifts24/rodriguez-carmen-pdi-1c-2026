# Modulo 010 — Modelos de difusion

## Que se estudia en este modulo

Este modulo introduce los modelos generativos de difusion: una familia de modelos de deep learning capaces de generar imagenes de alta calidad a partir de ruido aleatorio o de descripciones en texto natural. Son la base tecnologica de herramientas como Stable Diffusion, DALL-E y Midjourney.

El recorrido va desde los fundamentos matematicos hasta la aplicacion practica, incluyendo tecnicas de aceleracion que permiten generar imagenes en un solo paso en lugar de los cientos de pasos originales.

> **Nota de hardware:** estos modelos son computacionalmente muy exigentes. Los notebooks estan optimizados para ejecutarse en **Google Colab con GPU T4** (gratuita). La ejecucion local requiere una GPU con al menos 4-8 GB de VRAM y hasta 15 GB de espacio en disco para los modelos en cache.

## Conceptos clave

### Proceso de difusion forward y reverse

Un modelo de difusion aprende a revertir un proceso de degradacion:

- **Proceso forward (difusion):** se agrega ruido gaussiano a una imagen en T pasos sucesivos hasta que la imagen original queda completamente destruida y solo queda ruido blanco. Este proceso es fijo y matematicamente definido (no se aprende).
- **Proceso reverse (denoising):** la red neuronal aprende a predecir el ruido presente en cada paso y a eliminarlo gradualmente. Al aplicar el proceso reverse sobre ruido puro, la red genera una imagen nueva.

La red que realiza el denoising es tipicamente una **U-Net** con capas de atencion (attention layers) para capturar dependencias de largo alcance en la imagen.

### DDPM y schedulers

- **DDPM (Denoising Diffusion Probabilistic Models):** el modelo original. Requiere T=1000 pasos de denoising para generar una imagen. Es de alta calidad pero lento.
- **DDIM (Denoising Diffusion Implicit Models):** permite usar muchos menos pasos (20-50) produciendo resultados similares. Los **schedulers** (PNDMScheduler, DPMSolverScheduler, etc.) son los algoritmos que deciden cuantos pasos usar y como interpolar entre ellos.

### Condicionamiento por texto (text-to-image)

Los modelos text-to-image como Stable Diffusion agregan un componente de condicionamiento: el proceso de denoising se guia por un embedding de texto. El flujo es:

1. El prompt de texto se codifica con un **text encoder** (CLIP u otro modelo de lenguaje).
2. El embedding de texto se inyecta en la U-Net via cross-attention en cada capa.
3. La U-Net genera una imagen que "maximiza" la coherencia con el embedding del texto.

La imagen no se genera en el espacio de pixeles sino en un **espacio latente** comprimido (de ahi el nombre Latent Diffusion Model): el **VAE encoder** comprime la imagen a un espacio de menor dimension y el **VAE decoder** la reconstruye al final.

### SDXL Turbo

Stable Diffusion XL Turbo es una variante que utiliza destilacion adversarial (ADD — Adversarial Diffusion Distillation) para generar imagenes de 1024x1024 en un solo paso de denoising. Reduce el tiempo de generacion de minutos a segundos.

### SDXS (CPU-friendly)

SDXS es una variante comprimida de SDXL disenada para ejecucion en CPU con baja latencia. Usa quantizacion y destilacion para reducir el tamano del modelo manteniendo calidad aceptable.

### LCM-LoRA (Latent Consistency Models + Low-Rank Adaptation)

- **LCM (Latent Consistency Models):** reformula el proceso de difusion como un problema de consistencia que converge en pocos pasos (2-4 pasos vs los 20-50 de DDIM).
- **LoRA (Low-Rank Adaptation):** tecnica de fine-tuning eficiente que agrega matrices de bajo rango a los pesos originales del modelo. Solo se entrenan esos pesos adicionales (tipicamente menos del 1% del total), lo que hace el proceso rapido y el resultado pequeno.

Combinados, LCM-LoRA permite acelerar cualquier modelo de Stable Diffusion existente sin reentrenarlo completamente.

### Aplicaciones: inpainting y super-resolution

- **Inpainting:** se provee una imagen y una mascara. El modelo rellena la zona enmascarada con contenido coherente con el resto de la imagen y con el prompt de texto. A diferencia del inpainting clasico (modulo 005), aqui el modelo puede generar contenido nuevo, no solo interpolarlo.
- **Super-resolution:** se provee una imagen de baja resolucion y el modelo genera una version de mayor resolucion con detalles generados. Usa pipelines de image-to-image.

## Archivos

| Archivo | Contenido |
|---|---|
| `01_Introduccion_Conceptual_Difusion.ipynb` | forward process, reverse process, visualizacion de T pasos |
| `02_Paradigmas_y_Modelos_Difusion.ipynb` | de la vision clasica a los modelos generativos, historia y primer demo |
| `03_Aplicaciones_Practicas_Difusion.ipynb` | inpainting, super-resolution e image-to-image con diffusers |
| `04_Text_to_Image_SDXL_Turbo.ipynb` | generacion en un paso con SDXL Turbo |
| `05_Text_to_Image_SDXS_CPU.ipynb` | generacion text-to-image optimizada para CPU |
| `06_Aceleracion_LCM_LoRA.ipynb` | aceleracion con LCM-LoRA en 2-4 pasos |

## Librerias y herramientas

| Libreria | Uso en el modulo |
|---|---|
| `diffusers` (Hugging Face) | pipelines de difusion: text-to-image, inpainting, image-to-image |
| `transformers` (Hugging Face) | text encoders (CLIP) y otros componentes de los pipelines |
| `torch` | backend de inferencia y entrenamiento |
| `accelerate` | optimizaciones de memoria y ejecucion (model CPU offload, etc.) |
| `Pillow` (PIL) | carga y manipulacion de imagenes |
| `numpy` | operaciones sobre arrays |
| `matplotlib` | visualizacion de resultados |

## Optimizaciones de memoria para GPU con poca VRAM

Si la GPU tiene menos de 8 GB de VRAM:

```python
# Offload automatico entre GPU y CPU segun necesidad
pipe.enable_model_cpu_offload()

# Procesa el VAE por tiles para reducir el pico de memoria
pipe.enable_vae_tiling()

# Atencion con menor consumo de memoria (si xformers esta instalado)
pipe.enable_xformers_memory_efficient_attention()
```

## Como ejecutar en Colab

1. Abrir el notebook desde el boton "Open in Colab" o subir el archivo.
2. En el menu: `Entorno de ejecucion` → `Cambiar tipo de entorno de ejecucion` → seleccionar **GPU T4**.
3. Ejecutar la primera celda de instalacion de dependencias.
4. Ejecutar las celdas en orden. La primera generacion puede tardar varios minutos por la descarga del modelo.

## Conexion con otros modulos

Los modelos de difusion usan arquitecturas que combinan U-Net convolucional (vista en modulo 008-parte3) con mecanismos de atencion de los Transformers. El condicionamiento por texto conecta con los modelos multimodales como CLIP trabajados en el modulo 008-parte2. El despliegue de aplicaciones generativas puede integrarse con Gradio como se vio en los modulos 008 y 009.
