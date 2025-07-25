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
        /* ELIMINAR BORDE DE STREAMLIT CLOUD EMBED */
        ._streamlitAppContainer_nim44_1._embed_nim44_18 {
            border: 0 !important;
            border-radius: 0 !important;
            border-width: 0 !important;
            padding-bottom: 0 !important;
            overflow: hidden !important;
        }
        
        /* También puede venir con otros nombres de clase similares */
        [class*="streamlitAppContainer"][class*="embed"] {
            border: 0 !important;
            border-radius: 0 !important;
            border-width: 0 !important;
            padding-bottom: 0 !important;
        }
        
        /* Estilos adicionales para asegurar que no haya bordes */
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
