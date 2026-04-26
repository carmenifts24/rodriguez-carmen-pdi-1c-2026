# TFI 1: Mejora y restauracion de imagenes

Este trabajo integra tecnicas de procesamiento digital de imagenes para diagnosticar, comparar y justificar mejoras sobre tres casos distintos:

1. una imagen obtenida mediante camara oscura;
2. una imagen de medio grafico color;
3. una imagen de medio grafico blanco/negro.

El objetivo no fue aplicar filtros de manera acumulativa, sino construir pipelines breves y razonados. En cada caso se partio de un problema visual concreto, se probaron dos estrategias comparables y se eligio una version final con una justificacion tecnica.

## Archivos principales

- `TFI_1 - mejora y restauracion de imagenes.ipynb`: notebook de desarrollo del trabajo.
- `TFI_1_Consigna_y_Rubrica.md`: consigna, restricciones y criterios de evaluacion.
- `imagenes_tfi1/`: imagenes originales seleccionadas.
- `salidas_tfi1/`: resultados finales procesados.
- `dashboard_tfi1_tecnicas.html`: resumen visual de tecnicas usadas y referencias dentro del proyecto.

## Imagenes trabajadas

| Caso | Imagen original | Salida final |
|---|---|---|
| Camara oscura | `imagenes_tfi1/CajaOscura 7.png` | `salidas_tfi1/camara_oscura_final.png` |
| Medio grafico color | `imagenes_tfi1/UDO sola.jpeg` | `salidas_tfi1/medio_grafico_color_final.png` |
| Medio grafico blanco/negro | `imagenes_tfi1/DreamTeam ByN.jpeg` | `salidas_tfi1/medio_grafico_bn_final.png` |

## Caso 1: Camara oscura

**Diagnostico:** imagen muy oscura, bajo contraste, iluminacion despareja, poca nitidez, posible orientacion invertida y zonas con poca informacion util.

**Estrategia 1:** orientacion, recorte y ajuste lineal de brillo/contraste.

Esta estrategia busco corregir primero la lectura espacial de la imagen y despues mejorar la visibilidad general con `cv2.convertScaleAbs`. Fue util como prueba simple, pero al actuar de forma global podia saturar zonas claras o no resolver bien la iluminacion irregular.

**Estrategia 2:** orientacion, recorte, `CLAHE` en el canal de luminosidad y suavizado leve.

Esta fue la estrategia elegida porque mejoro el contraste local y conservo mejor la separacion entre zonas oscuras y claras. Su limite principal es que no puede recuperar nitidez ni informacion perdida en la captura original.

## Caso 2: Medio grafico color

**Diagnostico:** colores apagados, bajo contraste, iluminacion irregular, ruido y baja saturacion.

**Estrategia 1:** ajuste global de brillo/contraste y aumento de saturacion en `HSV`.

Esta estrategia permitio recuperar visibilidad y color de manera simple. Su limite fue que el ajuste global podia lavar zonas claras o producir una mejora menos controlada.

**Estrategia 2:** `CLAHE` sobre el canal `L` en `LAB`, ajuste moderado de saturacion y denoise leve con filtro bilateral.

Esta fue la estrategia elegida porque separa mejor los problemas: contraste local, color y ruido. Mejora la escena sin forzar toda la imagen del mismo modo, aunque no elimina completamente el deterioro del soporte ni reconstruye detalles perdidos.

## Caso 3: Medio grafico blanco/negro

**Diagnostico:** bajo contraste, imagen lavada, manchas, rayas, suciedad y zonas claras con poca textura.

**Estrategia 1:** suavizado leve y ecualizacion global del histograma.

Esta estrategia aumento el contraste general despues de reducir un poco el grano. Fue util como base de comparacion, pero la ecualizacion global tambien podia aumentar la visibilidad de manchas y rayas.

**Estrategia 2:** `CLAHE`, mascara conservadora de danos claros con morfologia e `inpainting` puntual.

Esta fue la estrategia elegida porque combina mejora local de contraste con restauracion localizada. El limite principal es que el `inpainting` depende de la calidad de la mascara: si toma zonas reales de la imagen, puede modificar informacion importante.

## Tecnicas utilizadas

| Tecnica | Uso en el TFI |
|---|---|
| Carga en `RGB` y gris | Permite trabajar correctamente imagenes color y blanco/negro. |
| Histogramas | Ayudan a diagnosticar bajo contraste y distribucion tonal. |
| Separacion de canales | Permite observar color, luminancia y saturacion antes de intervenir. |
| Rotacion y recorte | Corrigen orientacion y eliminan zonas que no aportan informacion. |
| Ajuste lineal de brillo/contraste | Mejora rapida y global de visibilidad. |
| `LAB` y `HSV` | Separan luminosidad y color para intervenir con mas control. |
| `CLAHE` | Mejora contraste local en imagenes con iluminacion irregular. |
| Suavizado gaussiano | Reduce ruido leve sin cambiar demasiado la estructura. |
| Filtro bilateral | Reduce ruido preservando mejor los bordes. |
| Ecualizacion global | Aumenta contraste general en imagenes blanco/negro. |
| Morfologia matematica | Ayuda a construir y limpiar mascaras de danos. |
| `inpainting` | Restaura rayas o marcas localizadas usando contexto cercano. |

## Comparacion general

La decision final dependio del tipo de degradacion. En la camara oscura convino una mejora local porque la iluminacion no era uniforme. En el medio grafico color fue importante separar luminancia y saturacion para no alterar toda la imagen de la misma manera. En el medio grafico blanco/negro, la mejora tonal no alcanzaba por si sola, por eso se sumo restauracion puntual sobre una mascara.

La conclusion principal es que no hay una tecnica universal. La mejora depende del diagnostico: contraste global, contraste local, color apagado, ruido o dano localizado requieren operaciones distintas y parametros moderados.

## Limites del trabajo

- No se recupera informacion que no esta presente en la imagen original.
- Una imagen muy desenfocada no puede volverse nitida solo con filtros basicos.
- Aumentar contraste puede hacer mas visibles manchas y ruido.
- El `inpainting` puede alterar contenido real si la mascara no esta bien controlada.
- Los parametros fueron elegidos por comparacion visual, por lo que una segunda iteracion podria incorporar metricas o mascaras mas precisas.
