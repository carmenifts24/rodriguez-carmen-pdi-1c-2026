# Instalacion inicial en otra computadora

Esta guia sirve para dejar el proyecto listo desde cero en una PC nueva. Para el uso diario, consultar `referencia_trabajo_diario.md`.

## 1. Abrir PowerShell en la carpeta del proyecto

```powershell
cd "C:\Proyectos\rodriguez-carmen-pdi-1c-2026"
```

## 2. Crear el entorno virtual

```powershell
python -m venv venv
```

Si `python` no funciona, probar:

```powershell
py -m venv venv
```

## 3. Habilitar scripts de PowerShell

Esto normalmente se hace una sola vez por usuario en Windows.

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

## 4. Activar el entorno virtual

```powershell
.\venv\Scripts\Activate.ps1
```

Si salio bien, la terminal muestra `(venv)` al principio.

## 5. Instalar las dependencias del proyecto

```powershell
python -m pip install -r requirements.txt
```

## 6. Verificar librerias principales

```powershell
python -c "import cv2, numpy, PIL, matplotlib, pandas; print('Librerias principales OK')"
```

## 7. Verificar librerias de redes neuronales

```powershell
python -c "import tensorflow, sklearn, gradio; print('Redes neuronales basicas OK')"
```

Para notebooks con modelos preentrenados de la unidad 009, tambien puede verificarse:

```powershell
python -c "import torch, torchvision, transformers; print('Modelos preentrenados OK')"
```

Nota: TensorFlow, PyTorch y Transformers son paquetes grandes. La instalacion puede tardar varios minutos y algunos notebooks descargan datasets o pesos desde internet.

## 8. Verificar `py5`

```powershell
python -c "import py5; print('py5 OK')"
```

## 9. Si `py5` falla por Java

```powershell
python -m pip install install-jdk
python -c "import jdk; print('Java installed to', jdk.install('17'))"
```

Esto instala Java 17 para el usuario actual.

## 10. Si `py5` sigue fallando al abrir ventana

```powershell
python -m pip install glfw
```

## 11. Abrir VS Code en la carpeta del proyecto

```powershell
code .
```

## 12. Elegir el interprete o kernel correcto

En VS Code, seleccionar:

```text
.\venv\Scripts\python.exe
```

Si usas notebooks, despues de instalar paquetes conviene reiniciar el kernel.

## 13. Cerrar el entorno al terminar

```powershell
deactivate
```

## Resumen rapido

```powershell
cd "C:\Proyectos\rodriguez-carmen-pdi-1c-2026"
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -c "import cv2, numpy, PIL, matplotlib, pandas; print('Librerias principales OK')"
python -c "import tensorflow, sklearn, gradio; print('Redes neuronales basicas OK')"
python -c "import py5; print('py5 OK')"
```
