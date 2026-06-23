# app.py -- Detector de Pose con MediaPipe (Tasks API)
# Estructura: 3 capas (Data Layer / Business Logic / Presentation Layer)

import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision as mp_vision
import gradio as gr
import numpy as np
import cv2
import os
import urllib.request


# -------------------------------------------------------------------------
# CAPA 1 -- DATA LAYER
# El modelo se descarga y carga una sola vez cuando arranca la aplicacion.
# Si lo cargaramos dentro de la funcion, cada request esperaria la carga.
# -------------------------------------------------------------------------

MODELO_PATH = "pose_landmarker_full.task"
MODELO_URL  = (
    "https://storage.googleapis.com/mediapipe-models/"
    "pose_landmarker/pose_landmarker_full/float16/1/pose_landmarker_full.task"
)

if not os.path.exists(MODELO_PATH):
    urllib.request.urlretrieve(MODELO_URL, MODELO_PATH)

POSE_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,7),(0,4),(4,5),(5,6),(6,8),
    (9,10),(11,12),
    (11,13),(13,15),(15,17),(15,19),(15,21),(17,19),
    (12,14),(14,16),(16,18),(16,20),(16,22),(18,20),
    (11,23),(12,24),(23,24),
    (23,25),(25,27),(27,29),(27,31),(29,31),
    (24,26),(26,28),(28,30),(28,32),(30,32),
]

# 0.5 equilibra sensibilidad y precision para uso general.
detector_pose = mp_vision.PoseLandmarker.create_from_options(
    mp_vision.PoseLandmarkerOptions(
        base_options=mp_python.BaseOptions(model_asset_path=MODELO_PATH),
        num_poses=1,
        min_pose_detection_confidence=0.5,
    )
)


# -------------------------------------------------------------------------
# CAPA 2 -- BUSINESS LOGIC
# Toda la logica de procesamiento vive aca, desacoplada de la interfaz.
# -------------------------------------------------------------------------

def detectar_pose(imagen_entrada):
    alto, ancho = imagen_entrada.shape[:2]

    imagen_mp  = mp.Image(image_format=mp.ImageFormat.SRGB, data=imagen_entrada)
    resultado  = detector_pose.detect(imagen_mp)
    imagen_anotada = imagen_entrada.copy()

    if not resultado.pose_landmarks:
        return imagen_anotada, "No se detecto ninguna figura humana en la imagen."

    lista_landmarks = resultado.pose_landmarks[0]

    for idx_a, idx_b in POSE_CONNECTIONS:
        lm_a = lista_landmarks[idx_a]
        lm_b = lista_landmarks[idx_b]
        if lm_a.visibility > 0.3 and lm_b.visibility > 0.3:
            xa, ya = int(lm_a.x * ancho), int(lm_a.y * alto)
            xb, yb = int(lm_b.x * ancho), int(lm_b.y * alto)
            cv2.line(imagen_anotada, (xa, ya), (xb, yb), (0, 200, 0), 2)

    for punto in lista_landmarks:
        if punto.visibility > 0.3:
            cv2.circle(imagen_anotada, (int(punto.x * ancho), int(punto.y * alto)), 4, (255, 50, 50), -1)

    punto_hombro_derecho   = lista_landmarks[12]
    punto_hombro_izquierdo = lista_landmarks[11]
    punto_cadera_derecha   = lista_landmarks[24]
    punto_rodilla_derecha  = lista_landmarks[26]
    punto_tobillo_derecho  = lista_landmarks[28]
    # Consigna 1 — puntos adicionales: muñecas (extremos distales de los brazos).
    punto_muneca_izquierda = lista_landmarks[15]   # índice 15: muñeca izquierda
    punto_muneca_derecha   = lista_landmarks[16]   # índice 16: muñeca derecha

    distancia_hombros   = round(abs(punto_hombro_derecho.x - punto_hombro_izquierdo.x), 3)
    inclinacion_hombros = round(punto_hombro_izquierdo.y - punto_hombro_derecho.y, 3)

    # Consigna 1 — métrica propia: apertura de brazos.
    # Distancia horizontal normalizada entre muñecas.
    #   < 0.2   → brazos juntos / cruzados
    #   0.3–0.5 → posición neutral
    #   > 0.6   → brazos extendidos lateralmente
    if punto_muneca_izquierda.visibility > 0.3 and punto_muneca_derecha.visibility > 0.3:
        apertura_brazos = round(abs(punto_muneca_derecha.x - punto_muneca_izquierda.x), 3)
        linea_apertura  = f"Apertura de brazos (norm.): {apertura_brazos}"
    else:
        linea_apertura = "Apertura de brazos: muñecas no visibles"

    lineas = [
        f"Distancia entre hombros (norm.): {distancia_hombros}",
        f"Visibilidad hombro derecho: {round(punto_hombro_derecho.visibility, 2)}",
        f"Cadera derecha y={round(punto_cadera_derecha.y, 3)}",
        f"Rodilla derecha y={round(punto_rodilla_derecha.y, 3)}",
        f"Tobillo derecho y={round(punto_tobillo_derecho.y, 3)}",
        f"Inclinacion lateral hombros: {inclinacion_hombros:+.3f}",
        linea_apertura,
    ]
    texto_info = "\n".join(lineas)

    return imagen_anotada, texto_info


# -------------------------------------------------------------------------
# CAPA 3 -- PRESENTATION LAYER
# -------------------------------------------------------------------------

with gr.Blocks(title="Detector de Pose") as aplicacion:

    gr.Markdown("## Detector de Pose corporal -- MediaPipe")
    gr.Markdown(
        "Subi una imagen de una persona y el modelo va a detectar "
        "los 33 puntos clave del esqueleto corporal."
    )

    with gr.Row():
        entrada_imagen = gr.Image(label="Fotografia", type="numpy")

    with gr.Row():
        salida_imagen = gr.Image(label="Pose detectada")
        salida_texto  = gr.Textbox(label="Informacion de puntos clave")

    boton_analizar = gr.Button("Analizar pose", variant="primary")

    boton_analizar.click(
        fn=detectar_pose,
        inputs=entrada_imagen,
        outputs=[salida_imagen, salida_texto],
    )


if __name__ == "__main__":
    aplicacion.launch()
