import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Ciclo de Conversión de Efectivo",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para el modo oscuro y métricas
def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

# Aunque Streamlit tiene modo oscuro nativo, forzamos algunos estilos para asegurar el "look premium"
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    .metric-card {
        background-color: #262730;
        border: 1px solid #464b59;
        border-radius: 5px;
        padding: 15px;
        color: white;
    }
    .result-card-positive {
        background-color: rgba(255, 75, 75, 0.1);
        border: 1px solid #ff4b4b;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
    }
    .result-card-negative {
        background-color: rgba(0, 204, 150, 0.1);
        border: 1px solid #00cc96;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# Sidebar: Explicación y Conceptos (Funcionalidad 1)
# -------------------------------------------------------------
with st.sidebar:
    st.title("📚 Ciclo de Conversión de Efectivo")
    st.markdown("""
    Esta aplicación ilustra, con fines pedagógicos, el cálculo del **Ciclo de Conversión de Efectivo (CCC)**.
    
    ### Fórmula:
    """)
    st.latex(r'''
    CCC = DI + DCC - DCP
    ''')
    
    st.markdown("""
    **Donde:**
    
    *   🟢 **DI** = Días de Inventario
    *   🟠 **DCC** = Días de Cuentas por Cobrar
    *   🟣 **DCP** = Días de Cuentas por Pagar
    
    ---
    
    **¿Qué mide?**
    El CCC mide cuántos días tarda una empresa en convertir sus inversiones en inventario y cuentas por cobrar en efectivo, después de pagar a sus proveedores.
    """)

# -------------------------------------------------------------
# Sección Principal: Funcionalidad 1
# -------------------------------------------------------------
st.title("💰 Ciclo de Conversión de Efectivo (CCC)")

st.subheader("🎛️ Controles de Variables")

# Definición de columnas para los sliders
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🟢 Días de Inventario")
    di = st.slider("DI (Días)", min_value=0, max_value=100, value=60, help="Tiempo promedio que el inventario permanece en la empresa.")
    st.markdown(f"<p style='color: #2ecc71; font-size: 20px; font-weight: bold; text-align: center;'>{di} días</p>", unsafe_allow_html=True)

with col2:
    st.markdown("### 🟠 Días de Cuentas por Cobrar")
    dcc = st.slider("DCC (Días)", min_value=0, max_value=100, value=30, help="Tiempo promedio para cobrar ventas a crédito.")
    st.markdown(f"<p style='color: #ff9f43; font-size: 20px; font-weight: bold; text-align: center;'>+{dcc} días</p>", unsafe_allow_html=True)

with col3:
    st.markdown("### 🟣 Días de Cuentas por Pagar")
    dcp = st.slider("DCP (Días)", min_value=0, max_value=100, value=45, help="Tiempo promedio para pagar a proveedores.")
    st.markdown(f"<p style='color: #9b59b6; font-size: 20px; font-weight: bold; text-align: center;'>-{dcp} días</p>", unsafe_allow_html=True)

# -------------------------------------------------------------
# Cálculo y Resultados
# -------------------------------------------------------------
ccc = di + dcc - dcp

st.divider()

st.subheader("Resultado:")

# Mostrar una métrica grande
st.markdown(f"""
    <h1 style='text-align: center; color: {'#ff4b4b' if ccc > 0 else '#00cc96'}; font-size: 3.5rem;'>
        = {ccc} días
    </h1>
    <p style='text-align: center;'>Ciclo de Conversión de Efectivo</p>
""", unsafe_allow_html=True)

# Mensaje Dinámico
if ccc > 0:
    st.markdown(f"""
    <div class="result-card-positive">
        <h3>🔴 CCC Positivo ({ccc} días)</h3>
        <p>La empresa necesita <b>{ccc} días adicionales</b> para convertir sus inversiones en efectivo. 
        El efectivo queda 'amarrado' en el ciclo operativo.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    # Caso negativo o cero
    st.markdown(f"""
    <div class="result-card-negative">
        <h3>🟢 CCC Negativo ({ccc} días)</h3>
        <p>La empresa cobra <b>{abs(ccc)} días antes</b> de pagar a sus proveedores. 
        Esto representa un financiamiento operativo favorable.</p>
    </div>
    """, unsafe_allow_html=True)

