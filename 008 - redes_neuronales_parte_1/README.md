# Redes neuronales - Parte 1

Esta carpeta introduce redes neuronales desde problemas simples hasta clasificacion de imagenes con CNNs e interfaces de prueba con Gradio.

## Notebooks

| Archivo | Tema principal |
|---|---|
| `001_Red_Neuronal.ipynb` | Primera red neuronal: relacion Celsius -> Fahrenheit, pesos, sesgo y perdida. |
| `002_Clasificacion.ipynb` | Clasificacion multiclase de letras manuscritas con una red densa. |
| `003_CNNs_Full.ipynb` | Redes convolucionales sobre MNIST y `cats_vs_dogs`; comparacion entre imagenes controladas e imagenes reales. |
| `004_Teachable_Machine_Dataset_Propio_Gradio.ipynb` | Diseno de dataset propio, exportacion desde Teachable Machine e interfaz Gradio. |

## Datos incluidos

- `datos/celsius.csv`: tabla simple para el primer ejemplo de regresion.

Otros datasets, como MNIST, EMNIST o `cats_vs_dogs`, se descargan desde las librerias usadas por cada notebook.

## Dependencias principales

Las dependencias estan centralizadas en el `requirements.txt` del proyecto. Para esta unidad se usan especialmente:

- `tensorflow`
- `tensorflow-datasets`
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `Pillow`
- `gradio`

## Recomendaciones de ejecucion

1. Activar el entorno virtual del proyecto.
2. Instalar dependencias con `python -m pip install -r requirements.txt`.
3. Abrir los notebooks desde la raiz del repositorio o desde VS Code con el kernel del entorno virtual.
4. Ejecutar las celdas en orden.

Algunas celdas descargan datasets o abren interfaces web. Si el equipo local tarda demasiado, conviene usar Google Colab para los notebooks con entrenamiento de CNNs o Gradio.

## Lectura pedagogica

La secuencia propone avanzar de menor a mayor complejidad:

1. Una neurona aprende una relacion numerica.
2. Una red densa clasifica letras a partir de pixeles.
3. Una CNN aprovecha la estructura espacial de la imagen.
4. Un modelo exportado se prueba con imagenes nuevas mediante una interfaz.

La idea central es no mirar solo la precision final: tambien importan los errores, el sesgo del dataset, la normalizacion de entradas y la interpretacion de las predicciones.
