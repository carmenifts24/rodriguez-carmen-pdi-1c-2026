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
- `005  - computer_vision_parte_1`: vision por computadora clasica con OpenCV
- `006 - TFI_1`: trabajo final integrador de mejora y restauracion de imagenes
- `006_fotografia_digital`: trabajo practico complementario sobre lenguaje fotografico y composicion visual

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

Nota: `py5` requiere Java. Si aparece un error relacionado con Java, conviene revisar la documentacion oficial de instalacion de `py5`.

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
```

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
|   `-- TFI_1 - mejora y restauracion de imagenes.ipynb
`-- 006_fotografia_digital/
|   |-- README.md
|   |-- De la camara oscura a la imagen intencional.pdf
|   |-- De la camara oscura a la imagen intencional.pptx
|   |-- 001_imagenes/
|   |   |-- originales/
|   |   |-- procesadas/
|   |   `-- descartes/
|   |-- 002_codigo/
|   |   `-- Trabajo Practico 006 - Fotografia Digital.ipynb
|   `-- 003_recursos/
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

### 005  - computer_vision_parte_1

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
- `TFI_1 - mejora y restauracion de imagenes.ipynb`: notebook de resolucion del trabajo.
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

### 006_fotografia_digital

Trabajo practico complementario sobre lenguaje fotografico aplicado. Todas las imagenes fueron capturadas por la estudiante. El trabajo integra teoria fotografica y procesamiento digital en cinco partes:

- **Parte 1 - Camara oscura:** retoma la imagen capturada con camara oscura artesanal. Se aplica rotacion, recorte y ecualizacion del canal `V` en espacio `HSV` para mejorar el contraste sin distorsionar los colores.
- **Parte 2 - Composicion y lenguaje visual:** reencuadre compositivo, conversion a escala de grises, binarizacion con umbral de Otsu y ecualizacion de histograma para analizar como la forma prevalece sobre el color.
- **Parte 3 - Reencuadre y reinterpretacion:** a partir de una unica imagen amplia se generan dos recortes con lecturas intencionalmente distintas (arquitectonica y narrativa), demostrando como el encuadre construye sentido.
- **Parte 4 - Punto de vista:** comparacion de dos fotografias del mismo sujeto desde distintas posiciones para analizar escala, contexto y relacion emocional.
- **Parte 5 - Fotografia basada en la luz:** analisis cuantitativo (luminosidad, contraste, rango, histograma) de cuatro fotografias en distintas condiciones de luz, con seleccion y esquema anotado de direccion de luz.

Archivos principales:

- `002_codigo/Trabajo Practico 006 - Fotografia Digital.ipynb`: notebook de resolucion
- `001_imagenes/originales/`: fotografias propias usadas como insumo
- `001_imagenes/procesadas/`: resultados generados por el notebook
- `De la camara oscura a la imagen intencional.pdf`: presentacion conceptual del recorrido
- `README.md`: documentacion especifica del trabajo

Tecnicas aplicadas:

- conversion `RGB` → `HSV` y ecualizacion selectiva por canal
- umbral de Otsu para binarizacion automatica
- ecualizacion global del histograma en escala de grises
- analisis de metricas de luminosidad y contraste con `numpy` y `pandas`
- visualizacion comparativa y anotacion de mapas de reencuadre con `matplotlib`

## Como trabajar con el material

### Scripts `.py`

- activar el entorno virtual
- abrir la carpeta completa del proyecto en VS Code
- ejecutar el archivo desde VS Code o desde terminal con `python archivo.py`

### Notebooks `.ipynb`

- abrir el notebook en VS Code o Jupyter
- verificar que el kernel seleccionado sea el del `venv`
- ejecutar las celdas en orden

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
