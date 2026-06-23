# Modulo 011 — Clase magistral: desarrollo y despliegue

## Que se estudia en este modulo

Este modulo cubre el ciclo completo de desarrollo y despliegue de aplicaciones de vision artificial: desde la gestion del entorno de desarrollo hasta la publicacion de una aplicacion publica accesible desde cualquier navegador.

Se trabajan dos paradigmas de entorno (virtual environments vs contenedores Docker), se integran las herramientas de los modulos anteriores (MediaPipe, Gradio, Hugging Face) y se establece el flujo profesional de despliegue con git.

## Temas trabajados

### Entornos virtuales vs Docker

La primera pregunta de cualquier proyecto de software es como gestionar las dependencias. Se comparan dos enfoques:

**Entornos virtuales (`venv`, `uv`):**
- Aislan las dependencias de Python a nivel de directorio.
- Rapidos de crear y modificar.
- Dependen del Python instalado en el sistema.
- Son la herramienta correcta para desarrollo individual y notebooks interactivos.

**Contenedores Docker:**
- Empaquetan el sistema operativo, Python, las dependencias y el codigo en una unidad reproducible (imagen).
- Garantizan que el entorno es identico en cualquier maquina que corra el contenedor.
- Implican un overhead de setup inicial mayor.
- Son la herramienta correcta para despliegue y para garantizar reproducibilidad en equipo.

La regla general: entorno virtual para desarrollar, Docker para desplegar (o para garantizar reproducibilidad en entornos compartidos).

### Docker y docker-compose

El modulo provee un entorno Docker listo para usar con JupyterLab:

```bash
# Primera vez: construye la imagen (descarga torch, ~10 min)
docker compose up --build

# Siguientes veces: levanta el contenedor existente
docker compose up
```

Acceder en `http://localhost:8888` con token `clase`.

El `Dockerfile` define la imagen: imagen base de Python, instalacion de dependencias, configuracion de JupyterLab. El `docker-compose.yml` define como levantar el servicio: puertos, volumenes montados, variables de entorno.

### MediaPipe en profundidad

Se trabajan los tres modelos principales de MediaPipe en el contexto de aplicaciones integradas:

- **Hand Landmarker:** 21 landmarks de mano para gestos y control.
- **Face Mesh:** 478 landmarks faciales para analisis de expresion y filtros AR.
- **Pose Landmarker:** 33 landmarks corporales para analisis de movimiento.

Se profundiza en el ciclo de vida de los modelos: inicializacion con el archivo `.task`, configuracion de opciones (modo imagen vs video, numero de manos detectadas, umbrales de confianza), procesamiento de frames y acceso estructurado a los resultados.

### Modelos de Hugging Face con pipeline

Se retoman ViT, CLIP y DETR del modulo 008-parte2 y se integran en el contexto de aplicaciones Gradio con Skills:

- `pipeline("image-classification")` con ViT para clasificacion.
- `pipeline("zero-shot-image-classification")` con CLIP para clasificacion sin ejemplos.
- `pipeline("object-detection")` con DETR para deteccion con bounding boxes.

### Construccion de interfaces con gr.Blocks

Se trabaja la arquitectura de tres capas para aplicaciones Gradio:

1. **Capa de modelo:** funcion Python que toma inputs y devuelve outputs. Es independiente de la interfaz.
2. **Capa de Skills:** funciones que encapsulan la logica de negocio (procesar una imagen con MediaPipe, clasificar con un modelo de HF).
3. **Capa de interfaz:** layout de Gradio que conecta componentes visuales con las Skills.

Esta separacion hace las aplicaciones mantenibles y permite reusar Skills en distintas interfaces.

### Despliegue en Hugging Face Spaces

El flujo completo de despliegue:

1. Crear un Space en huggingface.co (tipo Gradio, visibilidad publica o privada).
2. HF provee un repositorio git para el Space.
3. Clonar el repositorio del Space localmente.
4. Escribir `app.py` (la aplicacion Gradio) y `requirements.txt`.
5. `git add`, `git commit`, `git push` al repositorio del Space.
6. HF ejecuta automaticamente `app.py` y sirve la aplicacion.

Para usar el mismo repositorio de GitHub como fuente de codigo y el Space de HF como plataforma de despliegue, se configura doble remote:

```bash
git remote add origin https://github.com/usuario/repo.git
git remote add space https://huggingface.co/spaces/usuario/space-name
```

## Archivos

### Practicas (`002 - PRA`)

| Archivo/Carpeta | Contenido |
|---|---|
| `Dockerfile` | imagen Docker con JupyterLab y todas las dependencias |
| `docker-compose.yml` | configuracion del servicio: puerto 8888, volumen montado |
| `requirements.txt` | dependencias del contenedor |
| `notebooks/01_Entornos_de_Desarrollo.ipynb` | venv vs Docker, criterios de eleccion |
| `notebooks/02_Control_Volumen_con_Manos.ipynb` | Hand Landmarker + control de volumen |
| `notebooks/03_Integracion_Gradio_y_MediaPipe.ipynb` | Skills, gr.Interface, gr.Blocks, Face Mesh |
| `notebooks/04_Proyecto_Pose_y_Despliegue.ipynb` | Pose + deploy completo en HF Spaces |
| `notebooks/05_Modelos_Preentrenados_HuggingFace.ipynb` | ViT, CLIP zero-shot, DETR con pipeline |
| `notebooks/06_Cheatsheet_Desarrollo_Space.ipynb` | referencia rapida: git, Gradio, 3 capas |
| `notebooks/hand_landmarker.task` | modelo Hand Landmarker (TFLite) |
| `notebooks/mi-pose-app/` | proyecto de pose generado para despliegue |

## Librerias y herramientas

| Libreria/Herramienta | Uso en el modulo |
|---|---|
| `mediapipe` | Hand Landmarker, Face Mesh, Pose Landmarker |
| `gradio` | interfaces web con gr.Interface y gr.Blocks |
| `transformers` (Hugging Face) | ViT, CLIP, DETR con pipeline |
| `torch` (CPU) | backend para modelos de HF |
| `opencv-python-headless` | procesamiento de imagen en el contenedor (sin GUI) |
| Docker + docker-compose | contenerizacion del entorno de desarrollo |
| git | control de versiones y despliegue a HF Spaces |

## Diferencia entre opencv-python y opencv-python-headless

En el contenedor Docker se usa `opencv-python-headless` en lugar de `opencv-python`. La version headless no incluye las dependencias de GUI (Qt, GTK), lo que la hace mas liviana y apta para entornos sin pantalla. En un notebook de Jupyter o en un servidor, no se necesita abrir ventanas: la visualizacion ocurre en las celdas del notebook o en la interfaz de Gradio.

## Nota sobre el notebook 02 en Docker

El notebook de control de volumen usa la API de audio del sistema operativo del host. Dentro del contenedor Docker, el audio del host no esta disponible por defecto. Para ese notebook se recomienda usar la Opcion B (entorno virtual local) descrita en el `README.md` de `002 - PRA/`.

## Conexion con otros modulos

Este modulo integra y consolida los patrones de todos los modulos anteriores: MediaPipe (009), Gradio y HF (008-parte2), y los extiende con el ciclo profesional de desarrollo y despliegue. Representa el cierre del recorrido de la materia.
