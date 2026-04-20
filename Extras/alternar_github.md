# Alternar GitHub entre la materia y mi repositorio

Esta guia sirve para trabajar con dos referencias sin confundirme:

- `upstream`: repositorio original del profesor
- `origin`: mi repositorio personal en GitHub

La idea es usar siempre el mismo procedimiento antes de traer material nuevo, antes de trabajar y antes de subir cambios.

## Esquema mental

Pensarlo asi:

- `upstream` = de donde viene el material de la materia
- `origin` = a donde subo mis trabajos

Regla de seguridad:

- traer cambios desde `upstream`
- subir cambios a `origin`
- no hacer `push` a `upstream`

## Procedimiento de trabajo paso a paso

## Paso 1. Entrar a la carpeta correcta

```powershell
cd "C:\Proyectos\rodriguez-carmen-pdi-1c-2026"
```

Comentario:
Este paso asegura que estoy trabajando en el proyecto correcto y no en otra carpeta parecida.

## Paso 2. Activar el entorno virtual si lo necesito

```powershell
.\venv\Scripts\Activate.ps1
```

Comentario:
No es obligatorio para Git, pero si voy a probar notebooks, scripts o dependencias, conviene activarlo.

## Paso 3. Confirmar adonde apunta cada remoto

```powershell
git remote -v
```

Deberia ver algo asi:

```text
origin    https://github.com/carmenifts24/rodriguez-carmen-pdi-1c-2026.git
upstream  https://github.com/mattbarreto/ifts24-lab-pdi-2026.git
```

Comentario:
Este es el control mas importante.
Si `origin` no apunta a mi GitHub, no sigo hasta corregirlo.

## Paso 4. Confirmar en que rama estoy

```powershell
git branch --show-current
```

Comentario:
Esto me deja ver si estoy en `master` o en otra rama.
Antes de subir cambios, conviene saberlo.

## Paso 5. Ver el estado real del proyecto

```powershell
git status
```

Comentario:
Esto muestra:

- archivos modificados
- archivos nuevos
- archivos borrados
- si hay algo preparado para commit

Si veo archivos raros o cambios que no esperaba, freno y reviso antes de seguir.

## Escenario A. Quiero traer o incorporar material nuevo de la materia

## Paso 6A. Revisar primero que no haya trabajo mio sin guardar

```powershell
git status
```

Comentario:
Si tengo cambios importantes sin commit, no conviene mezclar enseguida material nuevo con trabajo propio.

## Paso 7A. Incorporar el material nuevo del profesor

Esto puede pasar de dos formas:

- copiando manualmente archivos nuevos a mi carpeta local
- trayendo cambios desde el repo del profesor

Si copio archivos manualmente:

- los pego dentro de la carpeta del proyecto
- despues reviso con `git status`

Si voy a usar Git para traer desde `upstream`, primero confirmo que estoy lista para mezclar esos cambios.

Comentario:
La idea es no perder de vista que el material del profesor entra al proyecto local, pero mis subidas siguen yendo a `origin`.

## Paso 8A. Revisar como quedaron los cambios

```powershell
git status
```

Comentario:
Aca verifico que lo nuevo que agregue sea realmente lo que esperaba.

## Escenario B. Quiero trabajar en ejercicios o reorganizar el repo

## Paso 6B. Hacer mis cambios normalmente

Comentario:
Puedo crear carpetas, mover archivos, modificar notebooks, actualizar `README.md` o sumar material en `Extras`.

## Paso 7B. Verificar que Git interpreta bien mis cambios

```powershell
git status
```

Comentario:
Si movi archivos, Git puede mostrarlos como:

- `deleted`
- `new file`
- `renamed`

Eso no siempre significa un problema.
Solo tengo que confirmar que esos movimientos fueron intencionales.

## Escenario C. Quiero subir mis avances a mi GitHub

## Paso 6C. Confirmar otra vez los remotos

```powershell
git remote -v
```

Comentario:
Lo repito aunque ya lo haya visto antes.
Es mi ultimo control para no subir por error al lugar equivocado.

## Paso 7C. Revisar exactamente que va a entrar

```powershell
git status
```

Comentario:
Si algo no deberia subirse, este es el momento de detectarlo.

## Paso 8C. Preparar los cambios

```powershell
git add .
```

Comentario:
Esto agrega todos los cambios actuales al proximo commit.

Si quiero preparar solo un archivo:

```powershell
git add "ruta\\del\\archivo"
```

## Paso 9C. Revisar otra vez

```powershell
git status
```

Comentario:
Ahora deberia aparecer la seccion `Changes to be committed`.
Esto me muestra exactamente lo que estoy por guardar.

## Paso 10C. Hacer el commit

```powershell
git commit -m "Escribir aqui un mensaje claro"
```

Ejemplos:

- `git commit -m "Agrega practica de lupa y canal por mouse"`
- `git commit -m "Reorganiza unidades y actualiza documentacion"`
- `git commit -m "Agrega material nuevo de teoria y practica"`

Comentario:
El commit no lo sube todavia a GitHub.
Solo deja guardado el avance en mi repositorio local.

## Paso 11C. Subir a mi GitHub

```powershell
git push
```

Comentario:
Este comando deberia empujar a `origin`, o sea, a mi repositorio.

Si alguna vez Git pide explicitar el destino:

```powershell
git push -u origin master
```

## Paso 12C. Verificar en GitHub

Comentario:
Entro a mi repo en GitHub y reviso:

- si aparece el commit nuevo
- si se ven las carpetas y archivos actualizados
- si estoy mirando la rama correcta

## Validaciones cortas que conviene repetir siempre

## Antes de empezar a trabajar

```powershell
git remote -v
git branch --show-current
git status
```

Comentario:
Con estas tres lineas ya se resuelven la mayoria de las dudas:

- adonde estoy conectada
- en que rama estoy
- que cambios tengo

## Antes de hacer `git push`

```powershell
git remote -v
git status
```

Comentario:
Estas son las dos verificaciones minimas para no empujar al repo equivocado ni subir cambios inesperados.

## Senales de alerta

- Si `origin` no apunta a mi GitHub, me detengo.
- Si `git status` muestra archivos que no reconozco, me detengo.
- Si no recuerdo en que rama estoy, la reviso antes de subir.
- Si tengo dudas, no hago `push` hasta entender que estoy enviando.

## Flujo resumido para todos los dias

```powershell
cd "C:\Proyectos\rodriguez-carmen-pdi-1c-2026"
.\venv\Scripts\Activate.ps1
git remote -v
git branch --show-current
git status
git add .
git status
git commit -m "Describe brevemente tus cambios"
git push
```

## Idea final

La secuencia mas segura es esta:

1. primero verificar
2. despues trabajar
3. despues revisar
4. recien al final subir

Si mantengo siempre ese orden, es mucho mas dificil equivocarme de repositorio o subir cambios que no queria.
