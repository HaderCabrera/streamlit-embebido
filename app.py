import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Configuración responsive
st.set_page_config(
    page_title="Dashboard Ejemplo",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        /* ESTILOS PARA EMBED EN STREAMLIT CLOUD */
        html, body {
            margin: 0 !important;
            padding: 0 !important;
            border: 0 !important;
            outline: 0 !important;
        }
        
        .stApp, .main, .block-container {
            margin: 0 !important;
            padding: 0 !important;
            border: 0 !important;
            outline: 0 !important;
        }
        
        /* ESTO ES CLAVE PARA STREAMLIT CLOUD */
        [data-testid="stAppViewContainer"] {
            border: 0 !important;
            outline: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        
        /* Eliminar cualquier sombra o borde del contenedor principal */
        div[data-testid="stApp"] {
            border: 0 !important;
            outline: 0 !important;
            box-shadow: none !important;
        }
        
        /* Fondo transparente para embed */
        .stApp {
            background: transparent !important;
        }
    </style>
""", unsafe_allow_html=True)

# Datos de ejemplo
def generar_datos():
    np.random.seed(42)
    fechas = pd.date_range("2023-01-01", periods=30)
    datos = pd.DataFrame({
        "Fecha": fechas,
        "Ventas": np.random.randint(100, 1000, size=30),
        "Clientes": np.random.randint(10, 200, size=30),
        "Región": np.random.choice(["Norte", "Sur", "Este", "Oeste"], 30)
    })
    return datos

# Gráficos
datos = generar_datos()

st.title("📊 Dashboard de Ventas")
st.write("Datos generados aleatoriamente para pruebas")

col1, col2 = st.columns(2)
with col1:
    fig1 = px.line(datos, x="Fecha", y="Ventas", title="Ventas Diarias")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.bar(datos, x="Región", y="Clientes", color="Región", title="Clientes por Región")
    st.plotly_chart(fig2, use_container_width=True)

# Tabla responsive
st.subheader("📝 Datos Completos")
st.dataframe(datos, use_container_width=True)
