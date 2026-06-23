# Modulo 003 — Camara oscura

## Que se estudia en este modulo

Este modulo es de naturaleza experimental y analogica. Se construye y se usa una camara oscura (pinhole camera) para capturar imagenes sin lente, usando solo la proyeccion de luz a traves de un agujero pequeno sobre una superficie fotosensible o una pantalla.

El objetivo no es programar sino entender el origen fisico de la imagen: como la luz viaja en linea recta, como la apertura controla la cantidad de luz y la nitidez, y por que la imagen proyectada aparece invertida. Esa comprension es el punto de partida para cualquier trabajo posterior con imagenes digitales.

## Conceptos trabajados

### Principio de la camara oscura

Una camara oscura es una caja cerrada con un agujero (apertura) en una cara. La luz que entra por ese agujero proyecta en la cara opuesta una imagen del exterior, invertida tanto horizontal como verticalmente. A menor apertura, mayor nitidez pero menor brillo. A mayor apertura, mas luz pero imagen mas borrosa.

Este principio es identico al de cualquier sistema optico: la apertura del objetivo de una camara fotografica cumple el mismo rol que el agujero de la camara oscura.

### Relacion entre apertura, nitidez y exposicion

- **Apertura pequena:** cada punto del exterior proyecta un haz de luz estrecho, lo que produce bordes bien definidos. La imagen es nitida pero oscura.
- **Apertura grande:** el haz se ensancha, los puntos se superponen y la imagen pierde definicion (blur). La imagen es mas brillante pero borrosa.

Esta es la base del concepto de profundidad de campo y de la relacion apertura–nitidez en fotografia.

### Imagen analogica como punto de partida digital

Las imagenes capturadas en este modulo (en papel fotografico o a traves de una pantalla) se digitalizan y se usan en los modulos siguientes como material de trabajo real. En particular, la imagen de camara oscura es uno de los tres casos del TFI 1 (modulo 006) y aparece tambien en el modulo 007.

## Archivos

El material de este modulo incluye:

- Imagenes capturadas con la camara oscura (varios tamanos y encuadres).
- `PROCESAMIENTO DE IMAGENES DIGITALES.pdf`: material de catedra de referencia.
- Archivos fotograficos ordenados por tamano: `Pequeno`, `Intermedio`, `Grande`.

No hay notebooks de codigo en este modulo. El procesamiento de estas imagenes ocurre en modulos posteriores.

## Conexion con otros modulos

| Modulo | Relacion |
|---|---|
| 004 - librerias_fundamentos_pdi | se usan imagenes propias en la actividad de recuperacion y preprocesamiento |
| 006 - TFI_1 | la imagen de camara oscura es uno de los tres casos del trabajo integrador |
| 007 - fotografia_digital | la imagen de camara oscura reaparece en la Parte 1 del trabajo fotografico |
