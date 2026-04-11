# py5: definición, configuración y usos

## ¿Qué es py5?

`py5` es una biblioteca de *creative coding* para Python inspirada en **Processing** y construida sobre las bibliotecas centrales de ese entorno. Su objetivo es facilitar la creación de programas visuales, animaciones, experiencias interactivas y proyectos artísticos usando la sintaxis y el ecosistema de Python.

En términos prácticos, `py5` permite escribir sketches similares a los de Processing, pero con las ventajas del lenguaje Python. Esto lo vuelve especialmente útil en contextos educativos, artísticos y experimentales, así como en proyectos donde se combinan imagen, interacción, datos y prototipado visual.

Una de sus características más relevantes es que actúa como un puente entre el mundo de Processing y el ecosistema de Python. Internamente utiliza librerías de Processing escritas en Java, pero ofrece al usuario una experiencia de programación centrada en Python.

## ¿Para qué se utiliza?

`py5` se utiliza principalmente para:

- desarrollar sketches visuales y animaciones en tiempo real;
- trabajar con dibujo generativo y arte computacional;
- crear interfaces visuales simples e interactivas;
- manipular imágenes y píxeles;
- enseñar fundamentos de programación mediante resultados visuales inmediatos;
- integrar programación creativa con bibliotecas de Python orientadas a ciencia de datos, visión por computadora o aprendizaje automático.

Por esta combinación, `py5` resulta especialmente valioso en cursos y proyectos de procesamiento de imágenes, visualización y diseño interactivo.

## Cómo se configura

La configuración de `py5` requiere preparar un entorno de Python y asegurar también la disponibilidad de Java, ya que Processing depende de la máquina virtual de Java.

### Requisitos generales

De acuerdo con la documentación oficial consultada el **25 de marzo de 2026**, los requisitos base indicados son:

- **Python 3.10 o superior**
- **Java 17 o superior**, con preferencia por **Java 21 o superior**

La documentación también recomienda evitar una instalación "headless" de Java, ya que `py5` necesita acceso a capacidades gráficas para abrir ventanas y ejecutar sketches.

### Instalación básica

La forma más directa de instalar `py5` es mediante `pip`:

```bash
pip install py5
```

Si además se desea trabajar con cuadernos Jupyter, puede utilizarse:

```bash
pip install py5[jupyter]
```

En proyectos más completos, también es habitual trabajar en un entorno virtual o en un entorno de Conda para aislar dependencias y facilitar la reproducibilidad del proyecto.

### Verificación de Java

Antes de ejecutar `py5`, conviene comprobar qué versión de Java está disponible:

```bash
java -version
```

Si el sistema no encuentra Java o la versión es inferior a la requerida, `py5` no podrá inicializar correctamente el entorno gráfico.

### Estructura mínima de un sketch

Una configuración funcional puede comprobarse con un sketch mínimo como el siguiente:

```python
import py5

def setup():
    py5.size(200, 200)

def draw():
    py5.background(240)
    py5.circle(py5.mouse_x, py5.mouse_y, 20)

py5.run_sketch()
```

En este esquema:

- `setup()` se ejecuta una sola vez al iniciar;
- `draw()` se ejecuta continuamente, cuadro a cuadro;
- `run_sketch()` inicia el programa.

Esta estructura retoma el modelo clásico de Processing, pero expresado en Python.

## Relación con Processing

`py5` puede entenderse como una adaptación moderna del enfoque de Processing para usuarios de Python. Ambos entornos comparten una lógica de trabajo similar: una ventana gráfica, funciones de inicialización, actualización continua del dibujo y una API orientada a la producción visual rápida.

La diferencia principal es que `py5` permite integrar ese modelo con herramientas habituales del ecosistema Python, por ejemplo:

- `numpy` para cálculo numérico;
- `pillow` para imágenes;
- `matplotlib` para visualización;
- bibliotecas de análisis de datos o aprendizaje automático.

Esto amplía mucho las posibilidades de trabajo en comparación con un entorno exclusivamente orientado al sketch visual.

## Aplicaciones en procesamiento de imágenes

En el área de procesamiento de imágenes, `py5` es útil para:

- cargar y mostrar imágenes;
- recorrer y modificar píxeles;
- aplicar filtros;
- visualizar transformaciones;
- experimentar con color en espacios como RGB o HSV;
- construir herramientas interactivas para explorar resultados visuales.

Por eso, en un proyecto de aprendizaje, `py5` funciona muy bien como entorno de exploración: permite ver rápidamente el efecto de una operación sobre una imagen y vincular teoría con percepción visual.

## Ventajas de py5

Entre sus principales ventajas pueden destacarse las siguientes:

- sintaxis accesible para principiantes;
- resultados visuales inmediatos;
- cercanía conceptual con Processing, muy usado en arte y diseño;
- integración con bibliotecas científicas y de análisis de datos de Python;
- utilidad tanto para aprendizaje como para prototipado rápido.

## Limitaciones y consideraciones

Aunque `py5` es muy potente para docencia, prototipado y proyectos creativos, también presenta algunas consideraciones prácticas:

- depende de una instalación correcta de Java;
- algunos problemas de configuración pueden surgir por incompatibilidades entre versiones de Python, Java y dependencias;
- no reemplaza por completo a bibliotecas especializadas en interfaces complejas o gráficos de alto rendimiento;
- en proyectos grandes conviene organizar bien el código y separar la lógica visual de la lógica de procesamiento.

Por ello, `py5` suele ser especialmente recomendable cuando el objetivo principal es aprender, experimentar o construir prototipos visuales con rapidez.

## Conclusión

`py5` es una herramienta que combina la tradición de Processing con la flexibilidad de Python. Su valor radica en hacer accesible la programación visual e interactiva sin renunciar al amplio ecosistema de bibliotecas disponibles en Python. En contextos de arte generativo, enseñanza y procesamiento de imágenes, constituye una plataforma especialmente adecuada para explorar ideas, visualizar algoritmos y desarrollar proyectos creativos de forma progresiva.

## Referencias

Las siguientes fuentes fueron consultadas el **25 de marzo de 2026**:

1. py5 community. *What is py5?* Documentación oficial de py5. Disponible en: <https://py5coding.org/content/about.html>
2. py5 community. *Install py5*. Documentación oficial de py5. Disponible en: <https://py5coding.org/content/install.html>
3. py5 community. *Importing py5 Code*. Documentación oficial de py5. Disponible en: <https://py5coding.org/content/importing_py5_code.html>

## Forma breve de cita sugerida

Si luego quieres usar este material en una bibliografía o webgrafía, una forma breve de citarlo podría ser:

> py5 community. *py5 documentation*. Disponible en: https://py5coding.org/ . Consulta: 25 de marzo de 2026.
