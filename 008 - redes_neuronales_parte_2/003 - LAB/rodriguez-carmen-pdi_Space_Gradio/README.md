---
title: Clasificador de Imagenes ViT
emoji: 🖼️
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 6.19.0
app_file: app.py
pinned: false
license: mit
---

# Clasificador de Imágenes con Vision Transformer (ViT)

Aplicación web interactiva que clasifica imágenes en tiempo real usando el modelo `google/vit-base-patch16-224` desplegada en Hugging Face Spaces.

**Demo en vivo:** https://huggingface.co/spaces/carmenmarylin/clasificador-imagenes-vit

**Tecnicatura Superior en Ciencias de Datos e IA · IFTS24**
Materia: Procesamiento Digital de Imágenes

---

## ¿Qué hace esta aplicación?

Recibe una imagen cargada por el usuario y devuelve las **5 categorías más probables de ImageNet** con su nivel de confianza (score), expresado como un valor entre 0 y 1 (equivalente a porcentaje de certeza del modelo).

El proceso completo es:

```
Imagen (PIL.Image)
    → Preprocesamiento: resize 224×224 + normalización ImageNet
    → Inferencia: ViT-Base con 86M parámetros
    → Postprocesamiento: top-5 logits → softmax → probabilidades
    → Salida: dict {clase: float} renderizado en gr.Label
```

---

## Modelo: Vision Transformer (ViT)

El modelo utilizado es [`google/vit-base-patch16-224`](https://huggingface.co/google/vit-base-patch16-224), una arquitectura Transformer aplicada a visión por computadora.

### ¿Cómo funciona ViT?

A diferencia de las CNN tradicionales (que aplican filtros convolucionales), ViT divide la imagen en **parches de 16×16 píxeles** y los procesa como una secuencia de tokens, igual que BERT procesa palabras en NLP:

```
Imagen 224×224 px
    → 196 parches de 16×16 px
    → Cada parche se aplana en un vector de 768 dimensiones
    → Se agrega un token [CLS] para la clasificación global
    → Los 197 tokens pasan por 12 bloques de Multi-Head Self-Attention
    → El token [CLS] final se proyecta a 1000 clases de ImageNet
```

### Especificaciones técnicas

| Parámetro | Valor |
|---|---|
| Arquitectura | Vision Transformer (ViT-Base) |
| Parámetros totales | ~86 millones |
| Tamaño de parche | 16×16 px |
| Resolución de entrada | 224×224 px |
| Pre-entrenamiento | ImageNet-21k (21M imágenes, 21 000 clases) |
| Fine-tuning | ImageNet-1k (1.28M imágenes, 1 000 clases) |
| Precisión top-1 | ~81.8% en ImageNet-1k |
| Precisión top-5 | ~96.1% en ImageNet-1k |

---

## Cómo interpretar la salida

La aplicación devuelve un gráfico de barras con las 5 predicciones principales. Cada barra representa:

- **Etiqueta (label):** nombre de la categoría de ImageNet (en inglés, ej. `tabby cat`, `school bus`)
- **Score:** probabilidad normalizada entre 0 y 1 (resultado de aplicar softmax sobre los logits del modelo)

### Ejemplo de salida

```python
{
    'tabby cat':     0.912,   # 91.2% de confianza → predicción dominante
    'tiger cat':     0.043,   # 4.3%  → clase visualmente similar
    'Egyptian cat':  0.031,   # 3.1%  → otra variante felina
    'Persian cat':   0.008,   # 0.8%  → baja probabilidad
    'lynx':          0.003    # 0.3%  → morfología distante
}
```

**Criterio top-5:** Es el estándar de evaluación de ImageNet. Una predicción se considera correcta si la clase verdadera aparece entre las 5 con mayor probabilidad, sin importar si es la número 1.

### Casos donde el modelo puede fallar

- Imágenes fuera de distribución (dibujos, imágenes médicas, documentos)
- Clases no representadas en ImageNet-1k (ej. razas de perros locales o marcas específicas)
- Imágenes con múltiples objetos prominentes: el modelo devuelve la categoría dominante global
- Baja resolución: al redimensionar a 224×224, la información de detalle se puede perder

---

## Arquitectura del código: 3 capas

El código sigue un patrón de separación de responsabilidades:

```
┌─────────────────────────────────────────────────────────────┐
│  PRESENTATION LAYER  (Gradio UI)                           │
│  gr.Blocks → gr.Image (entrada) + gr.Label (salida)        │
├─────────────────────────────────────────────────────────────┤
│  BUSINESS LOGIC LAYER  (Python)                            │
│  procesar_y_clasificar() → validación + formateo           │
├─────────────────────────────────────────────────────────────┤
│  DATA LAYER  (HuggingFace Transformers + PyTorch)          │
│  pipeline('image-classification') → inferencia ViT         │
└─────────────────────────────────────────────────────────────┘
```

La carga del modelo (`pipeline()`) ocurre una sola vez al iniciar el servidor, fuera de cualquier función, para evitar re-descargar los pesos (~350 MB) en cada consulta del usuario.

---

## Stack tecnológico

| Componente | Tecnología | Versión mínima |
|---|---|---|
| Interfaz web | Gradio | `>=4.0.0` |
| Modelo e inferencia | HuggingFace Transformers | `>=4.35.0` |
| Backend de cómputo | PyTorch | `>=2.0.0` |
| Manipulación de imágenes | Pillow (PIL) | `>=9.0.0` |
| Hosting | HuggingFace Spaces (CPU Basic) | — |

---

## Estructura del repositorio

```
.
├── app.py              # Punto de entrada obligatorio para HF Spaces
├── requirements.txt    # Dependencias del entorno de ejecución
├── README.md           # Este archivo + metadatos YAML del Space
└── .gitignore          # Excluye .venv/, __pycache__, .env, etc.
```

---

## Ejecución local

```bash
# 1. Clonar el repositorio
git clone https://huggingface.co/spaces/carmenmarylin/clasificador-imagenes-vit
cd clasificador-imagenes-vit

# 2. Crear entorno virtual e instalar dependencias
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/macOS

pip install -r requirements.txt

# 3. Ejecutar la aplicación
python app.py
# → Gradio levanta el servidor en http://localhost:7860
```

La primera ejecución descarga los pesos del modelo (~350 MB) y los cachea en `~/.cache/huggingface/`. Las ejecuciones siguientes los reutilizan desde disco.

---

## Despliegue en Hugging Face Spaces

HuggingFace Spaces construye automáticamente el entorno al detectar cambios en la rama `main`. El proceso de CI/CD es:

```
git push → HF detecta cambio → pip install -r requirements.txt → python app.py
```

```bash
# Conectar el repositorio local al Space remoto
git remote add origin https://huggingface.co/spaces/carmenmarylin/clasificador-imagenes-vit

# Publicar cambios
git add app.py requirements.txt README.md
git commit -m "feat: descripción del cambio"
git push origin main
```

> **Nota:** Si una dependencia no está en `requirements.txt`, el contenedor no la instalará y la aplicación lanzará `ModuleNotFoundError` al arrancar. Siempre verificar que todas las importaciones del código tengan su entrada correspondiente en ese archivo.
