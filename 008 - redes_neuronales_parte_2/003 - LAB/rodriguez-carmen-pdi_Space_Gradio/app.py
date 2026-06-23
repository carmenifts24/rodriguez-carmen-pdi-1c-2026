import os

# Debe ejecutarse ANTES de importar gradio: Gradio cachea GRADIO_HOT_RELOAD
# en el momento del import. Si está presente, launch() devuelve inmediatamente
# (no-bloqueante) y Python sale antes de que el servidor pueda recibir tráfico.
os.environ.pop('GRADIO_HOT_RELOAD', None)

import gradio as gr
from transformers import pipeline
from PIL import Image

print('✦ Configurando las capas de la aplicación...')

# =====================================================================
# 1. DATA LAYER: Carga de Modelos e Inferencia
# =====================================================================
print('✦ [Data Layer] Cargando modelo preentrenado...')
clasificador_modelo = pipeline(
    'image-classification',
    model='google/vit-base-patch16-224'
)
print('✓ [Data Layer] Modelo cargado con éxito en memoria.')


# =====================================================================
# 2. BUSINESS LOGIC LAYER: Validaciones y Control
# =====================================================================
def procesar_y_clasificar(imagen):
    """Lógica de control. Valida los datos y ejecuta el flujo."""
    if imagen is None:
        print('✗ [Business Layer] Intento de clasificación sin datos de imagen.')
        return {'Error': 'Por favor, carguen una imagen válida en el visor.'}

    print('✦ [Business Layer] Muestra recibida. Ejecutando inferencia...')

    try:
        resultados = clasificador_modelo(imagen)

        # gr.Label requiere valores float() nativos, no numpy.float32
        salida_diccionario = {}
        for res in resultados[:5]:
            salida_diccionario[res['label']] = float(res['score'])

        print('✓ [Business Layer] Procesamiento y estimación completados.')
        return salida_diccionario

    except Exception as error:
        print(f'✗ [Business Layer] Falla en ejecución del pipeline: {error}')
        return {'Error de Inferencia': str(error)}


# =====================================================================
# 3. PRESENTATION LAYER: Interfaz de Gradio (Blocks)
# =====================================================================
print('✦ [Presentation Layer] Construyendo interfaz web...')

with gr.Blocks() as interfaz_app:
    gr.Markdown('# ✦ Clasificador de Imágenes con ViT')
    gr.Markdown('Carguen una imagen en la columna izquierda y hagan clic en **Clasificar muestra**.')

    with gr.Row():
        with gr.Column():
            imagen_input = gr.Image(type='pil', label='Muestra Visual (Entrada)')
            boton_ejecutar = gr.Button('Clasificar muestra', variant='primary')

        with gr.Column():
            etiqueta_output = gr.Label(num_top_classes=5, label='Estimaciones de Confianza (Salida)')

    boton_ejecutar.click(
        fn=procesar_y_clasificar,
        inputs=imagen_input,
        outputs=etiqueta_output
    )

print('✓ [Presentation Layer] UI inicializada correctamente.')

interfaz_app.launch(ssr_mode=False)
