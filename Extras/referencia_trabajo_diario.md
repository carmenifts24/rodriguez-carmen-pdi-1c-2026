# Referencia rapida de trabajo

Esta guia resume el uso diario del proyecto y los problemas mas comunes. Para preparar una PC nueva desde cero, consultar `instalacion_inicial.md`.

## Flujo normal de trabajo

```powershell
cd "C:\Proyectos\rodriguez-carmen-pdi-1c-2026"
.\venv\Scripts\Activate.ps1
```

Si hace falta reinstalar dependencias:

```powershell
python -m pip install -r requirements.txt
```

Cuando termines:

```powershell
deactivate
```

## VS Code y notebooks

- Abrir la carpeta completa del proyecto, no un archivo suelto.
- Seleccionar el interprete `.\venv\Scripts\python.exe`.
- En notebooks, usar ese mismo kernel.
- Si el notebook no detecta paquetes recien instalados, reiniciar el kernel.

Si hace falta soporte para notebooks:

```powershell
python -m pip install ipykernel
```

## Comandos utiles

```powershell
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -c "import cv2, numpy, PIL, matplotlib; print('Librerias principales OK')"
python -c "import py5; print('py5 OK')"
git status
git pull
deactivate
```

## Problemas frecuentes

### PowerShell no deja activar `venv`

Si aparece un error con `Activate.ps1`:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1
```

### Faltan librerias aunque exista `venv`

Si aparece `No module named ...`:

```powershell
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Verificacion:

```powershell
python -c "import cv2, numpy, PIL, matplotlib; print('Librerias principales OK')"
```

### `python` no se reconoce

Opciones:

- usar `py` en lugar de `python`
- reinstalar Python marcando `Add Python to PATH`

Ejemplo:

```powershell
py -m venv venv
py -m pip install -r requirements.txt
```

### VS Code o Jupyter usan otro Python

Si en la terminal funciona pero en VS Code no:

- volver a seleccionar `.\venv\Scripts\python.exe`
- revisar que el notebook use ese mismo kernel

### `py5` falla al iniciar

Primero probar:

```powershell
python -m pip install glfw
python -c "import py5; print('py5 OK')"
```

Si el error menciona Java:

```powershell
python -m pip install install-jdk
python -c "import jdk; print('Java installed to', jdk.install('17'))"
```

Despues cerrar y abrir de nuevo la terminal, reactivar `venv` y volver a probar.

### Las imagenes no cargan

Revisar:

- que el archivo exista en la carpeta esperada
- que el script se ejecute desde la carpeta correcta
- que la ruta sea relativa y no absoluta

Ejemplo:

```python
img = cv2.imread("img/imagen.jpg")
```

### `git pull` falla por cambios locales

Primero revisar:

```powershell
git status
```

Despues decidir si esos cambios hay que guardarlos, moverlos o hacer commit antes de actualizar.
