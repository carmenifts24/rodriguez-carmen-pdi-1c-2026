# Actualizar el proyecto en GitHub

Esta guia resume que hacer cada vez que quieras guardar cambios del proyecto en tu repositorio de GitHub.

## Antes de empezar

Trabaja siempre desde la carpeta raiz del proyecto:

```powershell
cd "C:\Users\carme\OneDrive\Documents\Procesamiento de imágenes\rodriguez-carmen-pdi-1c-2026"
```

Si usas entorno virtual:

```powershell
.\venv\Scripts\Activate.ps1
```

## Paso 1. Revisar que repo estas usando

```powershell
git remote -v
```

Deberias ver:

- `origin` apuntando a tu GitHub
- `upstream` apuntando al repo original de la materia

## Paso 2. Ver que cambios hiciste

```powershell
git status
```

Aca revisas:

- que estes en la rama correcta
- que los archivos modificados sean los que esperabas
- que no haya algo que no quieras subir

## Paso 3. Preparar los cambios

Si queres subir todo lo que cambiaste:

```powershell
git add .
```

Si queres subir solo algunos archivos, en vez de eso usa:

```powershell
git add "ruta\\del\\archivo"
```

## Paso 4. Confirmar los cambios

```powershell
git commit -m "Escribe aqui un mensaje corto y claro"
```

Ejemplos:

- `git commit -m "Actualiza README y guias de Extras"`
- `git commit -m "Agrega ejercicios de py5 y reorganiza carpetas"`

## Paso 5. Subir a GitHub

Si trabajas en la rama `master`:

```powershell
git push
```

Si alguna vez Git te pide explicitar destino:

```powershell
git push -u origin master
```

## Paso 6. Verificar en GitHub

Despues del `push`, entra a tu repositorio en GitHub y revisa:

- que aparezca el ultimo commit
- que los archivos esten actualizados
- que la rama visible sea la correcta

## Flujo corto de todos los dias

```powershell
git status
git add .
git commit -m "Describe brevemente tus cambios"
git push
```

## Si algo sale raro

### Quiero ver a que repo estoy subiendo

```powershell
git remote -v
```

### Quiero ver en que rama estoy

```powershell
git branch --show-current
```

### Quiero revisar que voy a subir antes del commit

```powershell
git status
```

### Hice cambios pero todavia no hice `git add`

Todavia no estan preparados para el commit. Revisalos con:

```powershell
git status
```

### Ya hice `git add` y quiero revisar antes de confirmar

```powershell
git status
```

Si algo no deberia subirse, frená antes del `commit`.

## Idea practica

Pensalo asi:

- `git status`: que cambio
- `git add`: que quiero guardar
- `git commit`: dejar registro
- `git push`: mandarlo a GitHub
