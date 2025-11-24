# 🥟 Detector de Empanadas

Esta es una aplicación simple construida con [Streamlit](https://streamlit.io/) para detectar empanadas en imágenes utilizando un modelo YOLOv11 entrenado previamente.

## 📋 Requisitos Previos

- **Python 3.8+** instalado.
- **uv** (opcional, pero recomendado para una instalación rápida). El script de instalación intentará instalarlo si no lo tienes.
- El archivo del modelo entrenado (`best.pt`).

## 🛠️ Instalación y Configuración

Para facilitar la configuración del entorno, hemos incluido un script que utiliza `uv` para crear un entorno virtual e instalar las dependencias rápidamente.

1.  Abre una terminal en la carpeta `empanadas_app`.
2.  Ejecuta el script de configuración:

    ```bash
    ./setup.sh
    ```

    Este script:
    - Verificará si tienes `uv` instalado.
    - Creará un entorno virtual en `.venv`.
    - Instalará las librerías necesarias (`streamlit`, `ultralytics`, etc.).

## 🤖 Obtener el Modelo

La aplicación necesita el archivo de pesos del modelo entrenado para funcionar.

1.  Ve a tu entorno de entrenamiento (por ejemplo, Google Colab donde ejecutaste el notebook).
2.  Descarga el archivo `best.pt` que se generó al final del entrenamiento.
    - Ruta típica en Colab: `/content/runs/detect/train/weights/best.pt`
3.  **Copia el archivo `best.pt` dentro de esta carpeta (`empanadas_app/`)**.

> **Nota:** Si tu modelo tiene otro nombre, renómbralo a `best.pt` o edita la variable `MODEL_PATH` en el archivo `app.py`.

## 🚀 Ejecución

Una vez configurado el entorno y colocado el modelo:

1.  Activa el entorno virtual (si no lo has hecho aún):

    ```bash
    source .venv/bin/activate
    ```

2.  Inicia la aplicación de Streamlit:

    ```bash
    streamlit run app.py
    ```

3.  Se abrirá automáticamente una pestaña en tu navegador (usualmente en `http://localhost:8501`).

## 📸 Uso

1.  En la interfaz web, haz clic en **"Browse files"** para subir una imagen (`.jpg`, `.png`, etc.).
2.  Verás la imagen cargada en pantalla.
3.  Haz clic en el botón **"Detectar Empanadas"**.
4.  El modelo procesará la imagen y mostrará el resultado con las detecciones marcadas y el conteo de empanadas encontradas.

## 📂 Estructura del Proyecto

- `app.py`: Código fuente de la aplicación web.
- `setup.sh`: Script para automatizar la creación del entorno.
- `requirements.txt`: Lista de dependencias de Python.
- `best.pt`: (Debes agregarlo tú) Archivo del modelo entrenado.

