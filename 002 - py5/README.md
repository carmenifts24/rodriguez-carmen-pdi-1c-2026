# Modulo 002 — Fundamentos de imagen digital

## Que se estudia en este modulo

Este modulo profundiza en la imagen digital como estructura de datos y extiende el trabajo con py5 hacia el analisis y la manipulacion basada en canales de color e interaccion espacial.

Una imagen digital es una matriz bidimensional donde cada posicion (x, y) contiene un valor de color. Ese valor puede descomponerse en canales independientes: en RGB son tres matrices (R, G, B); en escala de grises, una sola. Entender esa estructura es fundamental para cualquier operacion posterior de procesamiento.

## Temas trabajados

### Imagen digital: pixeles, resolucion y canales

Se trabaja la relacion entre resolucion espacial (cantidad de pixeles) y la informacion que contiene una imagen. Se visualiza que cada canal de color es, por si mismo, una imagen en escala de grises donde el brillo indica la intensidad de ese canal en cada punto.

### Separacion y visualizacion de canales

Se aislan los canales R, G y B de una imagen color para observarlos por separado. Esta operacion revela como cada canal contribuye a la apariencia final y es el paso previo a cualquier operacion que necesite actuar sobre un solo componente del color.

### Interaccion con el mouse sobre imagenes

Se implementa un sketch que lee los valores de color del pixel bajo el cursor en tiempo real. Al mover el mouse sobre la imagen, se muestran los valores R, G y B del punto senalado. Esta tecnica es util para diagnosticar imagenes y entender la distribucion del color.

Archivo: `canal_mouse.py` / `2026_PDI_RODRIGUEZ_canal_mouse.py`

### Efecto lupa

Se implementa un efecto de ampliacion sobre una region de interes definida por la posicion del mouse. La zona bajo el cursor se escala y se renderiza ampliada en otro sector del lienzo. Esto introduce el concepto de ventana deslizante (sliding window) sobre una imagen.

Archivo: `lupa.py` / `2026_PDI_RODRIGUEZ_lupa.py`

### Diferencia entre entorno local y Colab

Se trabaja la misma practica en dos contextos distintos:
- **Local:** ejecucion directa con py5 y acceso a recursos del sistema.
- **Colab:** version adaptada para entorno web sin GUI nativa; se usan alternativas de visualizacion con `matplotlib`.

## Archivos

| Archivo | Contenido |
|---|---|
| `00_setup_colab.ipynb` | configuracion inicial para correr el material en Google Colab |
| `02a_fundamentos_teoria_colab.ipynb` | fundamentos de imagen digital, version Colab |
| `02a_fundamentos_teoria_local.ipynb` | mismos fundamentos, version local con py5 |
| `02b_fundamentos_practica_local.ipynb` | ejercicios practicos locales sobre canales y pixeles |
| `02c_laboratorio_fundamentos.ipynb` | actividad integradora del modulo |
| `canal_mouse.py` | lectura de valores RGB bajo el cursor |
| `lupa.py` | efecto zoom sobre region de interes |

### Laboratorio (`003 - LAB`)

- `2026_PDI_RODRIGUEZ_canal_mouse.py`: entrega de la actividad de lectura de canales.
- `2026_PDI_RODRIGUEZ_lupa.py`: entrega de la actividad de lupa.

## Librerias y herramientas

| Libreria | Uso en el modulo |
|---|---|
| `py5` | loop grafico, acceso a pixeles, renderizado |
| `numpy` | manipulacion de arrays de pixeles |
| `matplotlib` | visualizacion en Colab (alternativa a la ventana de py5) |
| Java (JVM) | backend requerido por py5 |

## Conexion con otros modulos

La comprension de la imagen como matriz de pixeles y canales separables es la base directa del modulo 004, donde se retoman estas operaciones con librerias especializadas como OpenCV y scikit-image, con mayor control y precision sobre cada canal.
