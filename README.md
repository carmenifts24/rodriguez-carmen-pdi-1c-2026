# Laboratorio de Fundamentos de Procesamiento Digital de Imágenes

**IFTS N.º 24 - Ciencia de Datos e Inteligencia Artificial**  
**3.er año - 1.er cuatrimestre 2026**

Repositorio personal de trabajo para la cursada de Procesamiento Digital de Imágenes. Reúne apuntes, prácticas, laboratorios y material complementario desarrollado durante la materia.

## Qué contiene este repositorio

El material está organizado por unidades numeradas. En cada unidad se separan, cuando corresponde:

- `001 - TEO`: teoría, presentaciones y material de cátedra
- `002 - PRA`: prácticas, notebooks y ejercicios guiados
- `003 - LAB`: trabajos de laboratorio, actividades integradoras o entregas
- `Extras`: guías de instalación, uso diario y documentación complementaria

Estado actual del recorrido:

- `001 - py5`: introducción a programación visual con `py5`
- `002 - py5`: fundamentos de imagen digital e interacción visual
- `003 - camara_oscura`: registro y material de trabajo asociado a la experiencia de cámara oscura
- `004 - librerias_fundamentos_pdi`: procesamiento con librerías de Python, segmentación y preprocesamiento

## Tecnologías y librerías

Principales librerías usadas en la cursada:

- `numpy`
- `scipy`
- `opencv-python`
- `scikit-image`
- `Pillow`
- `matplotlib`
- `jupyter`
- `ipykernel`
- `py5`

Nota: `py5` requiere Java. Si aparece un error relacionado con Java, conviene revisar la documentación oficial de instalación de `py5`.

## Instalación local

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

Si PowerShell bloquea la activación:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 4. Instalar dependencias

```bash
python -m pip install -r requirements.txt
```

### 5. Verificar librerías principales

```bash
python -c "import cv2, numpy, PIL, matplotlib; print('Librerías principales OK')"
python -c "import py5; print('py5 OK')"
```

## Guías útiles incluidas

En la carpeta `Extras` hay documentación pensada para uso práctico:

- `Extras/instalacion_inicial.md`: puesta en marcha desde cero en otra computadora
- `Extras/referencia_trabajo_diario.md`: comandos de uso frecuente y resolución de problemas comunes
- `Extras/actualizar_github.md`: pasos para subir cambios al repositorio
- `Extras/alternar_github.md`: notas de trabajo con remotos y cuentas GitHub

## Estructura actual del proyecto

```text
rodriguez-carmen-pdi-1c-2026/
|-- README.md
|-- requirements.txt
|-- 001 - py5/
|   |-- 001 - TEO/
|   |-- 002 - PRA/
|   `-- 003 - LAB/
|-- 002 - py5/
|   |-- 001 - TEO/
|   |-- 002 - PRA/
|   `-- 003 - LAB/
|-- 003 - camara_oscura/
|   `-- 003 - LAB/
|-- 004 - librerias_fundamentos_pdi/
|   |-- 001 - TEO/
|   |-- 002 - PRA/
|   `-- 003 - LAB/
`-- Extras/
```

## Resumen por unidad

### 001 - py5

Unidad centrada en la introducción a `py5` y a la programación visual.

Incluye ejercicios de:

- creación de ventanas y sketches básicos
- color en `RGB` y `HSV/HSB`
- carga y visualización de imágenes
- manipulación manual de píxeles
- filtros visuales
- interacción con mouse
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
- `001 - py5/002 - PRA/img/`
- `001 - py5/002 - PRA/save/`

### 002 - py5

Unidad orientada a fundamentos de imagen digital y primera articulación entre teoría, práctica y laboratorio.

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
- diferencia entre teoría en Colab y trabajo local
- exploración de canales de color
- interacción con el mouse sobre imágenes
- zoom o efecto lupa sobre regiones de interés

### 003 - camara_oscura

Unidad destinada al registro de la experiencia de cámara oscura y a la producción de imágenes propias usadas luego en otras actividades.

En `003 - camara_oscura/003 - LAB` hay material de referencia y archivos asociados a la experiencia, incluyendo capturas como:

- `Pequeno - 1.jpeg`
- `Pequeno - 3.jpeg`
- `imagen_preprocesada.png`

Este material se articula especialmente con la unidad `004`, donde se trabaja recuperación, preprocesamiento y segmentación sobre imágenes propias.

### 004 - librerias_fundamentos_pdi

Unidad enfocada en el uso de librerías de procesamiento de imágenes más allá de `py5`.

Notebooks y archivos de práctica en `004 - librerias_fundamentos_pdi/002 - PRA`:

- `001 - entorno y librerias.ipynb`
- `002 - imagenes en color y canales.ipynb`
- `003 - operaciones basicas con opencv.ipynb`
- `004 - muestreo y cuantizacion.ipynb`
- `005 - practica guiada de procesamiento de imagenes.ipynb`
- `006 - laboratorio 2 - segmentacion simple por color.ipynb`
- `007 - recuperacion y preprocesamiento de imagenes propias.ipynb`
- `008 - actividad integradora - segmentacion por color.ipynb`
- `005 - practica guiada de procesamiento carmen.py`

Material de laboratorio desarrollado en `004 - librerias_fundamentos_pdi/003 - LAB`:

- `2026_PDI_RODRIGUEZ_proc_digital.ipynb`
- `2026_PDI_RODRIGUEZ_segmentac_color.ipynb`
- `2026_PDI_RODRIGUEZ_ rec_preproc_imag_propias.ipynb`
- `2026_PDI_RODRIGUEZ_ integrador_segmentacion por color.ipynb`

Imágenes y recursos usados en esta unidad:

- `flowers.jpg`
- `frutos_rojos.png`
- `monedas.png`
- `paisaje.png`
- `texto.png`
- `imagen_preprocesada.png`

Temas trabajados:

- preparación del entorno de trabajo con librerías
- lectura y visualización de imágenes con OpenCV
- análisis de canales e histogramas
- operaciones básicas sobre imágenes
- muestreo y cuantización
- segmentación simple por color
- recuperación y preprocesamiento de imágenes propias
- actividad integradora de segmentación usando `imagen_preprocesada.png`

## Cómo trabajar con el material

### Scripts `.py`

- activar el entorno virtual
- abrir la carpeta completa del proyecto en VS Code
- ejecutar el archivo desde VS Code o desde terminal con `python archivo.py`

### Notebooks `.ipynb`

- abrir el notebook en VS Code o Jupyter
- verificar que el kernel seleccionado sea el del `venv`
- ejecutar las celdas en orden

### Google Colab

Algunos notebooks están preparados para trabajo en Colab, especialmente los que ya lo indican en el nombre o incluyen una celda de setup.

## Problemas frecuentes

### PowerShell no deja activar el entorno virtual

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1
```

### Faltan módulos como `cv2`, `numpy` o `PIL`

```bash
python -m pip install -r requirements.txt
```

### VS Code o Jupyter usan otro intérprete

Seleccionar:

```text
.\venv\Scripts\python.exe
```

### `py5` falla al iniciar

Primero probar:

```bash
python -m pip install glfw
```

Si el error menciona Java, instalar Java y revisar la guía oficial de `py5`.

## Recursos

- OpenCV: <https://docs.opencv.org/>
- NumPy: <https://numpy.org/doc/>
- Matplotlib: <https://matplotlib.org/>
- scikit-image: <https://scikit-image.org/docs/>
- py5: <https://py5coding.org/>
- Instalación de py5: <https://py5coding.org/content/install.html>
- Google Colab: <https://colab.research.google.com/>

## Licencia

Material de uso educativo para la cursada. Si más adelante se define una licencia específica para la materia, conviene agregarla en este archivo.
