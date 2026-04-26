# Resumen de tecnicas de tratamiento de imagenes del proyecto

Este archivo resume las tecnicas que aparecen aplicadas en los notebooks y laboratorios del repositorio. Si una tecnica se usa varias veces, se lista una sola vez y se aclara cuando fue reutilizada con objetivos diferentes.

## Criterio de lectura

- La tabla prioriza tecnicas efectivamente usadas en el codigo o en las practicas resueltas.
- Se agrupan variantes cercanas cuando forman parte de una misma familia de trabajo.
- El foco esta puesto en como ayudan al analisis de imagen, no solo en la operacion tecnica.

## Tabla resumen

| Tecnica | Para que se utiliza | Como mejora el analisis de la imagen | Cuando conviene usarla |
|---|---|---|---|
| Conversion de espacios de color (`BGR`, `RGB`, `HSV`, `LAB`, gris) | Adaptar la representacion de la imagen al problema: visualizar correctamente, separar luminancia de color o segmentar por tono. La misma conversion se uso con objetivos distintos: pasar de `BGR` a `RGB` para mostrar bien, a gris para bordes/ecualizacion y a `HSV` o `LAB` para segmentacion y mejora de contraste. | Hace mas interpretable la informacion relevante y evita trabajar con un espacio de color poco conveniente para la tarea. | Cuando la imagen se ve bien pero el analisis no funciona bien en el espacio original. |
| Separacion de canales e histogramas | Analizar la distribucion de intensidades y decidir que canal o rango conviene usar. | Permite justificar decisiones de umbral, contraste o segmentacion con evidencia visual y numerica. | Antes de fijar umbrales, comparar metodos de mejora o estudiar bajo contraste. |
| Ajuste lineal de brillo y contraste (`cv2.convertScaleAbs`) | Corregir imagenes oscuras, lavadas o con contraste insuficiente. Tambien se uso para generar versiones de prueba con menos contraste. | Resalta diferencias de intensidad que luego facilitan segmentacion, lectura visual o deteccion de detalles. | Cuando la imagen esta subexpuesta, sobreexpuesta o con rango tonal comprimido. |
| Ecualizacion global del histograma (`cv2.equalizeHist`) | Redistribuir intensidades para aumentar el contraste global. Se aplico en gris, por canal y sobre `V` en `HSV`. | Hace visibles detalles escondidos en zonas con poco contraste, aunque puede exagerar ruido o alterar colores si se usa sin cuidado. | Cuando el contraste global es bajo y se busca una mejora rapida para inspeccion o preprocesamiento. |
| CLAHE (ecualizacion adaptativa) | Mejorar contraste local sin uniformar toda la imagen de la misma manera. | Recupera detalles en regiones oscuras o desparejas con menos riesgo de sobreexagerar toda la escena. | Cuando hay iluminacion no uniforme o interes por detalles locales. |
| Muestreo y cuantizacion | Reducir resolucion espacial o cantidad de niveles tonales para estudiar como cambia la imagen digital. | Ayuda a entender perdida de detalle, aparicion de bandas y relacion entre calidad y representacion. | En practicas de fundamentos o cuando se quiere simplificar la imagen para analisis exploratorio. |
| Recorte de ROI (region de interes) | Aislar una zona puntual de la imagen para observarla o procesarla aparte. | Reduce ruido contextual y concentra el analisis en el objeto o region importante. | Cuando la escena completa distrae o el problema esta localizado en una parte de la imagen. |
| Redimensionado (`resize`) | Cambiar el tamano de una imagen o de un recorte para visualizacion, comparacion o preparacion de datos. | Facilita inspeccion visual y estandariza tamanos de entrada, aunque puede deformar si no se cuida la proporcion. | Cuando hace falta comparar regiones, normalizar dimensiones o adaptar la imagen a una etapa posterior. |
| Volteo y rotacion (`flip`, `warpAffine`) | Cambiar orientacion o generar variantes simples de una escena. | Sirve para entender la geometria de la imagen y preparar ejemplos con distintas orientaciones. | Cuando importa analizar sensibilidad a la orientacion o ejercitar transformaciones basicas. |
| Transformacion de perspectiva (`getPerspectiveTransform`, `warpPerspective`) | Rectificar objetos fotografiados oblicuamente para verlos "de frente". | Corrige distorsion geometrica y vuelve mas comparable un objeto respecto de una forma ideal o frontal. | Cuando el objeto de interes aparece inclinado o deformado por la toma. |
| Deteccion de bordes con Canny | Resaltar contornos por cambios fuertes de intensidad. Se uso para comparar sensibilidad con umbrales distintos. | Simplifica la escena y destaca limites utiles para segmentacion, conteo o descripcion de formas. | Cuando interesan bordes mas que texturas o colores. |
| Suavizado y reduccion de ruido (`blur`, `GaussianBlur`, `medianBlur`, `bilateralFilter`) | Atenuar ruido gaussiano o sal y pimienta. Cada filtro se comparo para objetivos diferentes: suavizar, preservar bordes o limpiar impulsos. | Produce imagenes mas estables para pasos posteriores como umbralado, contornos o visualizacion. | Antes de segmentar o detectar bordes, especialmente si la imagen tiene ruido visible. |
| Umbralizacion global manual (`cv2.threshold`) | Separar fondo y objeto con un unico valor de corte elegido a mano. Se trabajo comparando umbrales bajos, medios y altos para ver como cambia la mascara. | Convierte una imagen continua en una mascara facil de medir y limpiar; ademas permite observar como un umbral demasiado bajo pierde informacion y uno demasiado alto incorpora ruido. | Cuando la iluminacion es pareja y hay buen contraste entre objeto y fondo, por ejemplo texto oscuro sobre papel claro bien iluminado. |
| Umbralizacion automatica con Otsu (`THRESH_OTSU`) | Calcular automaticamente un umbral global a partir del histograma, con y sin suavizado gaussiano previo. | Evita elegir el corte manualmente y da una primera mascara objetiva cuando las intensidades se agrupan en fondo y objeto. | Cuando el histograma sugiere dos grupos principales y se busca una decision global reproducible. |
| Umbralizacion adaptativa (`adaptiveThreshold`) | Calcular umbrales locales por vecindarios para construir mascaras en imagenes con iluminacion desigual. | Mejora la separacion cuando una zona de la imagen esta mas oscura o mas clara que otra, problema donde un unico umbral global puede fallar. | Cuando hay sombras, reflejos, fondos no uniformes o documentos fotografiados con iluminacion irregular. |
| Segmentacion por color con rangos (`inRange`) | Aislar objetos por color en `HSV` o `RGB`. La misma tecnica se uso para globos, cartas, flores y otros ejemplos. | Permite construir mascaras especificas para un objeto cromaticamente distinguible. | Cuando el color del objeto es mas estable que su forma o textura. |
| Operaciones bit a bit (`bitwise_and`, `bitwise_or`) | Aplicar mascaras a la imagen o combinar varias mascaras parciales. | Ayudan a visualizar exactamente que fue segmentado y a unir rangos de color separados, como el rojo en `HSV`. | Despues de construir mascaras, para inspeccion o fusion de resultados. |
| Morfologia matematica (`erode`, `dilate`, apertura, clausura) | Limpiar mascaras, eliminar ruido pequeno o cerrar huecos. La misma familia se uso con fines distintos: suprimir puntos aislados, conectar trazos y mejorar texto o segmentacion por color. | Hace las mascaras mas coherentes y estables para medicion, contornos o clasificacion. | Cuando una mascara tiene agujeros, puntos sueltos o bordes fragmentados. |
| Deteccion de contornos (`findContours`) | Recuperar el borde de regiones binarias para dibujar, filtrar o medir objetos. | Convierte una mascara en estructuras geometricas explotables para conteo y analisis de forma. | Cuando ya existe una mascara razonable del objeto de interes. |
| Propiedades geometricas de contornos (`contourArea`, `boundingRect`, `moments`, `approxPolyDP`, `arcLength`) | Medir area, perimetro, centroide, rectangulo envolvente y aproximacion poligonal. | Permiten pasar de "ver un objeto" a describirlo cuantitativamente. | Cuando se necesita comparar formas, filtrar por tamano o justificar detecciones. |
| Filtrado por area de contorno | Descartar regiones pequenas o irrelevantes despues de segmentar. | Reduce falsos positivos y deja solo objetos compatibles con el tamano esperado. | Cuando la segmentacion genera manchas pequenas o ruido residual. |
| Inpainting (`cv2.inpaint`) | Restaurar zonas danadas o faltantes usando el contexto vecino. | Permite recuperar continuidad visual y comparar metodos de reconstruccion. | Cuando hay rayas, manchas o faltantes localizados y se dispone de una mascara del dano. |
| Coincidencia por plantilla (`matchTemplate`) | Buscar una subimagen dentro de una imagen mayor. | Genera un mapa de similitud que ayuda a localizar patrones concretos. | Cuando el objeto buscado mantiene forma y escala relativamente estables. |
| Deteccion de rostros con cascadas de Haar (`CascadeClassifier`) | Detectar rostros mediante un clasificador clasico entrenado. | Automatiza localizacion de regiones faciales sin tener que segmentar manualmente. | Cuando se necesita una deteccion rapida y clasica de rostros frontales en condiciones razonables. |

## Observaciones generales

- Varias tecnicas aparecen encadenadas como pipeline: conversion de color -> histograma/canales -> suavizado opcional -> umbralizacion o segmentacion -> morfologia -> contornos -> medicion.
- En el repositorio tambien hay operaciones basicas de visualizacion e interaccion en `py5`, pero la tabla se concentra en tratamiento y analisis de imagen ya trabajado con objetivo de PDI.
- Las tecnicas mas reutilizadas con fines diferentes fueron: conversion de espacios de color, ajuste de contraste, ecualizacion, suavizado, umbralizacion, segmentacion por color, morfologia y contornos.
- El cuaderno `006b2 - umbralizacion global, Otsu y adaptive threshold - version simplificada.ipynb` suma una comparacion directa entre umbral global manual, Otsu y umbralizacion adaptativa. Tambien refuerza una idea importante: la binarizacion debe pensarse junto con la limpieza morfologica posterior, porque una mascara binaria suele necesitar correcciones antes de medir o detectar contornos.

## Si despues queres una version mas visual

Se puede convertir este resumen a cualquiera de estas opciones:

1. Un dashboard HTML con filtros por tecnica, unidad y tipo de uso.
2. Una tabla Markdown enriquecida con columna "archivos donde aparece".
3. Un archivo exportable a PDF o a una hoja tipo ficha de estudio.
