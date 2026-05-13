# Trabajo Practico 006 - Fotografia Digital

**IFTS N. 24 - Ciencia de Datos e Inteligencia Artificial**  
**3.er ano - 1.er cuatrimestre 2026**

Trabajo practico complementario orientado a aplicar conceptos de lenguaje fotografico y procesamiento de imagenes sobre material capturado por la estudiante. El eje central es comprender como las decisiones visuales —encuadre, punto de vista, luz, composicion— construyen sentido en una imagen, y como el procesamiento digital puede amplificar o analizar esas decisiones.

---

## Estructura de la carpeta

```text
006_fotografia_digital/
|-- README.md
|-- De la camara oscura a la imagen intencional.pdf
|-- De la camara oscura a la imagen intencional.pptx
|-- 001_imagenes/
|   |-- originales/          (imagenes capturadas por la estudiante)
|   |-- procesadas/          (resultados generados por el notebook)
|   `-- descartes/           (imagenes descartadas durante la seleccion)
|-- 002_codigo/
|   `-- Trabajo Practico 006 - Fotografia Digital.ipynb
`-- 003_recursos/
    |-- Trabajo Practico 006 - Fotografia Digital.docx
    `-- Guia de referentes fotograficos.docx
```

---

## Imagenes originales

Todas las fotografias fueron capturadas especificamente para este trabajo. Se organizan por tema:

| Archivo | Descripcion |
|---|---|
| `Mickey_000.png` | Captura realizada con camara oscura artesanal |
| `Simplif.jpg` / `Simpli.jpg` | Composicion para trabajar simplificacion y lenguaje visual |
| `Ree.jpg` | Paisaje urbano con rio, seleccionado para reencuadre y reinterpretacion |
| `Reenc.jpg` | Interior arquitectonico trabajado con reencuadre compositivo |
| `Punt_.jpg` / `Punt_v.jpg` | Mismo sujeto fotografiado desde dos puntos de vista distintos |
| `Luz.jpg` / `Luz_.jpg` / `Luz_d.jpg` / `Luz_t.jpg` | Serie de cuatro fotografias que exploran la luz como elemento compositivo |

---

## Partes del trabajo

### Parte 1 - Captura con camara oscura y ecualizacion HSV

Se retoma la imagen obtenida con la camara oscura artesanal trabajada en la unidad 003. El procesamiento incluye:

- Rotacion de 180 grados para corregir la inversion optica natural de la camara oscura
- Recorte selectivo para eliminar los bordes oscuros del soporte
- Conversion del espacio de color `RGB` a `HSV` para acceder a los canales de manera independiente
- Ecualizacion del canal `V` (brillo/valor) sin modificar `H` (tono) ni `S` (saturacion)
- Analisis comparativo de ecualizaciones sobre `H` y `S` para comprender sus efectos

**Conclusion:** La ecualizacion del canal `V` mejora el contraste sin distorsionar los colores percibidos. Las limitaciones opticas de la camara oscura artesanal no pueden eliminarse solo con procesamiento.

Imagen de entrada: `001_imagenes/originales/Mickey_000.png`  
Salidas: `caso1_camara_oscura_recortada.png`, `caso1_eq_canal_H.png`, `caso1_eq_canal_S.png`, `caso1_eq_canal_V.png`

---

### Parte 2 - Composicion y lenguaje visual

Se trabaja sobre una imagen con elementos geometricos claros para analizar como el reencuadre y la conversion a escala de grises refuerzan la composicion.

Operaciones aplicadas:

- Reencuadre compositivo para eliminar elementos distractores
- Conversion a escala de grises
- Binarizacion automatica con umbral de Otsu
- Ecualizacion del histograma en escala de grises

**Conclusion:** El reencuadre concentra la atencion en la forma. La escala de grises elimina el color como distractor y refuerza la lectura estructural de la imagen.

Imagen seleccionada: `001_imagenes/originales/Simplif.jpg`  
Salidas: `simplif_blanco_y_negro.png`, `simplif_escala_de_grises.png`, `simplif_reencuadre_escala_grises.png` (y equivalentes para `Simpli.jpg`)

---

### Parte 3 - Reencuadre y reinterpretacion

Se parte de una unica imagen amplia de paisaje urbano y se generan dos reencuadres con lecturas intencionalmente distintas:

- **Reencuadre 1:** zona de edificio oscuro → lectura arquitectonica y abstracta
- **Reencuadre 2:** zona de puente y skyline → lectura narrativa y urbana

Sobre cada recorte se produce un mapa anotado que señala los elementos compositivos seleccionados y el sentido que construyen.

**Conclusion:** El encuadre no es neutral. Un recorte puede transformar radicalmente la narrativa de una imagen sin modificar ningun pixel: cambia el contexto, aísla o conecta elementos, y dirige la atencion del espectador.

Imagen seleccionada: `001_imagenes/originales/Ree.jpg`  
Salidas: `ree_reencuadre_mapa_1.png`, `ree_reencuadre_mapa_2.png` (y equivalentes sobre `Reenc.jpg`)

---

### Parte 4 - Punto de vista y construccion narrativa

Se comparan dos fotografias del mismo sujeto tomadas desde posiciones distintas para analizar como el punto de vista modifica escala, contexto y relacion emocional.

- `Punt_.jpg`: vista cenital o de nivel bajo, que achica al sujeto en el espacio
- `Punt_v.jpg`: vista frontal o natural, que le devuelve presencia y escala

La imagen final seleccionada es `Punt_v.jpg`, con justificacion compositiva.

**Conclusion:** La posicion de la camara respecto al sujeto determina la jerarquia visual y la lectura emocional. No es solo estetica: es una decision narrativa.

Salidas: `punt_vista_a.png`, `punt_vista_b.png`, `punt_imagen_final.png`

---

### Parte 5 - Fotografia basada en la luz

Se analiza una serie de cuatro fotografias de la misma escena en distintas condiciones de luz. Para cada una se calculan:

- Luminosidad promedio (media del canal de brillo)
- Contraste (desviacion estandar de intensidades)
- Rango de valores (min y max de pixeles)
- Histograma de distribucion de intensidades

La imagen seleccionada es `Luz_t.jpg` (hora azul, contraluz, reflejos en superficie), acompanada de un esquema visual anotado con la direccion de la luz natural y la fuente artificial.

**Conclusion:** La luz estructura la composicion antes que el encuadre. Su direccion, dureza y temperatura determinan la atmosfera, el volumen y el sentido dramatico de la imagen.

Imagenes analizadas: `Luz.jpg`, `Luz_.jpg`, `Luz_d.jpg`, `Luz_t.jpg`  
Salidas: `luz_fotografia_final.png`, `luz_esquema_direccion.png`

---

## Tecnologias utilizadas

| Libreria | Uso principal |
|---|---|
| `opencv-python` | Lectura, conversion de espacios de color, escritura de imagenes |
| `numpy` | Operaciones sobre arreglos de pixeles |
| `scikit-image` | Ecualizacion de histograma, umbral de Otsu |
| `matplotlib` | Visualizacion de imagenes e histogramas |
| `pandas` | Tablas comparativas de metricas |
| `Pillow` | Manipulacion auxiliar de imagenes |

**Funciones auxiliares definidas en el notebook:**

- `cargar_rgb()` / `cargar_gris()` — lectura de imagenes en distintos espacios de color
- `mostrar_imagen()` / `mostrar_comparacion()` — visualizacion simple y lado a lado
- `mostrar_histograma_gris()` / `mostrar_canales_rgb()` — analisis de distribucion de intensidades
- `guardar_rgb()` / `guardar_gris()` — escritura de imagenes procesadas en disco

---

## Como reproducir el trabajo

1. Activar el entorno virtual del proyecto

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. Abrir el notebook en VS Code o Jupyter

   ```text
   006_fotografia_digital/002_codigo/Trabajo Practico 006 - Fotografia Digital.ipynb
   ```

3. Verificar que el kernel seleccionado sea el del `venv`

4. Ejecutar las celdas en orden

Las rutas dentro del notebook son relativas a la ubicacion del archivo `.ipynb`. No es necesario mover archivos ni cambiar configuracion adicional.

---

## Relacion con el resto del proyecto

Este trabajo es posterior al TFI_1 y retoma imagenes capturadas desde la unidad 003. Mientras que el TFI_1 se centra en mejora y restauracion tecnica, este trabajo pone el foco en la interpretacion visual: como se construye sentido a partir de decisiones fotograficas, y como el procesamiento digital puede utilizarse para analizar o amplificar esas decisiones.

La presentacion `De la camara oscura a la imagen intencional` (disponible en `.pdf` y `.pptx`) sintetiza el recorrido conceptual del trabajo.
