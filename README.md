# Laboratorio de Fundamentos de Procesamiento Digital de Imagenes

**IFTS N 24 - Ciencia de Datos e Inteligencia Artificial**  
**3er ano - 1er cuatrimestre 2026**

Repositorio de trabajo para la cursada de Procesamiento Digital de Imagenes, Vision por Computadora y primeras practicas con herramientas visuales en Python.

## Que contiene este repositorio

El material esta organizado por unidades numeradas. En cada unidad se separan, cuando corresponde:

- `TEORIA`: presentaciones, apuntes y material de catedra
- `PRACTICA`: notebooks, scripts y ejercicios para trabajar
- `LABORATORIO`: actividades integradoras o entregas de laboratorio
- `Extras`: guias de instalacion, uso diario y material complementario

Hasta el estado actual del proyecto, el recorrido incluye:

- `001 - py5`: introduccion a programacion visual con `py5`
- `002 - py5`: fundamentos de imagen digital con notebooks y scripts interactivos
- `003 - librerias_fundamentos_pdi`: primeras practicas con OpenCV, canales, muestreo, segmentacion y preprocesamiento

## Tecnologias y librerias

Principales librerias usadas en la cursada:

- `numpy`
- `scipy`
- `opencv-python`
- `scikit-image`
- `Pillow`
- `matplotlib`
- `jupyter`
- `ipykernel`
- `py5`

Nota: `py5` requiere Java. Si aparece un error relacionado con Java, revisar la documentacion oficial de instalacion de `py5`.

## Instalacion local

### 1. Clonar el repositorio

```bash
git clone https://github.com/mattbarreto/ifts24-lab-pdi-2026.git
cd ifts24-lab-pdi-2026
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
python -c "import cv2, numpy, PIL, matplotlib; print('Librerias principales OK')"
python -c "import py5; print('py5 OK')"
```

## Guias utiles incluidas

En la carpeta `Extras` hay documentacion pensada para uso practico:

- `Extras/instalacion_inicial.md`: puesta en marcha desde cero en otra computadora
- `Extras/referencia_trabajo_diario.md`: comandos de todos los dias y problemas frecuentes

## Estructura actual del proyecto

```text
rodriguez-carmen-pdi-1c-2026/
|-- README.md
|-- requirements.txt
|-- 001 - py5/
|   |-- TEORIA/
|   |-- PRACTICA/
|   `-- LABORATORIO/
|-- 002 - py5/
|   |-- TEORIA/
|   |-- PRACTICA/
|   `-- LABORATORIO/
|-- 003 - librerias_fundamentos_pdi/
|   `-- PRACTICA/
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

Archivos destacados en `001 - py5/PRACTICA`:

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

Material complementario:

- `001 - py5/PRACTICA/README.md`
- `001 - py5/PRACTICA/py5_referencia.md`
- `001 - py5/PRACTICA/img/`
- `001 - py5/PRACTICA/save/`

### 002 - py5

Unidad orientada a fundamentos de imagen digital y primera articulacion entre teoria, practica y laboratorio.

En `002 - py5/PRACTICA` hay:

- `00_setup_colab.ipynb`
- `02a_fundamentos_teoria_colab.ipynb`
- `02a_fundamentos_teoria_local.ipynb`
- `02b_fundamentos_practica_local.ipynb`
- `02c_laboratorio_fundamentos.ipynb`
- `canal_mouse.py`
- `lupa.py`

Temas trabajados:

- lectura inicial de imagen digital
- diferencia entre teoria en Colab y trabajo local
- exploracion de canales de color
- interaccion con el mouse sobre imagenes
- zoom o efecto lupa sobre regiones de interes

### 003 - librerias_fundamentos_pdi

Unidad enfocada en el uso de librerias de procesamiento de imagenes mas alla de `py5`.

Notebooks y archivos actuales en `003 - librerias_fundamentos_pdi/PRACTICA`:

- `001 - entorno y librerias.ipynb`
- `002 - imagenes en color y canales.ipynb`
- `003 - operaciones basicas con opencv.ipynb`
- `004 - muestreo y cuantizacion.ipynb`
- `005 - practica guiada de procesamiento de imagenes.ipynb`
- `005 - practica guiada de procesamiento carmen.py`
- `006 - laboratorio 2 - segmentacion simple por color.ipynb`
- `007 - recuperacion y preprocesamiento de imagenes propias.ipynb`
- `008 - actividad integradora - segmentacion por color.ipynb`

Temas trabajados:

- preparacion del entorno
- lectura y visualizacion de imagenes con librerias de Python
- canales de color
- operaciones basicas con OpenCV
- muestreo y cuantizacion
- segmentacion simple por color
- recuperacion y preprocesamiento

## Como trabajar con el material

### Scripts `.py`

- Activar el entorno virtual
- Abrir la carpeta completa del proyecto en VS Code
- Ejecutar el archivo desde VS Code o desde terminal con `python archivo.py`

### Notebooks `.ipynb`

- Abrir el notebook en VS Code o Jupyter
- Verificar que el kernel seleccionado sea el del `venv`
- Ejecutar las celdas en orden

### Google Colab

Algunos notebooks estan preparados para trabajo en Colab, especialmente los que ya lo indican en el nombre o incluyen una celda de setup.

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

## Recursos

- OpenCV: <https://docs.opencv.org/>
- NumPy: <https://numpy.org/doc/>
- Matplotlib: <https://matplotlib.org/>
- scikit-image: <https://scikit-image.org/docs/>
- py5: <https://py5coding.org/>
- Instalacion de py5: <https://py5coding.org/content/install.html>
- Google Colab: <https://colab.research.google.com/>

## Licencia

Material de uso educativo para la cursada. Si mas adelante se define una licencia especifica para la materia, conviene agregarla en este archivo.
