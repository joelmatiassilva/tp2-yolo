import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os

st.set_page_config(page_title="Detector de Empanadas", page_icon="🥟")

st.title("🥟 Detector de Empanadas con YOLOv11")
st.write("Sube una imagen para detectar empanadas usando tu modelo entrenado.")

# Configuración de modelos
current_dir = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(current_dir, "modelos")

# Diccionario de modelos disponibles
model_options = {
    "Modelo v1": "best_mauri_v1.pt",
    "Modelo v2": "best_dovi_v2.pt"
}

# Selección de modelo
st.subheader("1. Configuración del Modelo")
selected_model_name = st.selectbox(
    "Selecciona la versión del modelo a utilizar:",
    list(model_options.keys())
)

MODEL_PATH = os.path.join(MODELS_DIR, model_options[selected_model_name])

# Verificar si el modelo existe
if not os.path.exists(MODEL_PATH):
    st.error(f"No se encontró el archivo del modelo en '{MODEL_PATH}'.")
    st.stop()

# Cargar el modelo seleccionado
try:
    model = YOLO(MODEL_PATH)
    st.success(f"Modelo '{selected_model_name}' cargado exitosamente.")
except Exception as e:
    st.error(f"Error al cargar el modelo: {e}")
    st.stop()

st.divider()
st.subheader("2. Detección")

# Subir imagen
uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Mostrar imagen original
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen subida', use_column_width=True)
    
    if st.button('Detectar Empanadas'):
        with st.spinner('Detectando...'):
            try:
                # Realizar inferencia
                results = model.predict(image)
                
                # Visualizar resultados
                # results[0].plot() devuelve un array numpy con la imagen anotada
                res_plotted = results[0].plot()
                
                # Convertir de BGR a RGB (YOLO usa OpenCV que es BGR)
                res_image = Image.fromarray(res_plotted[..., ::-1])
                
                st.success("¡Detección completada!")
                st.image(res_image, caption='Resultado de la detección', use_column_width=True)
                
                # Mostrar conteo si es útil
                boxes = results[0].boxes
                if len(boxes) > 0:
                    st.info(f"Se detectaron {len(boxes)} objetos.")
                else:
                    st.warning("No se detectaron empanadas.")
                    
            except Exception as e:
                st.error(f"Ocurrió un error durante la inferencia: {e}")

