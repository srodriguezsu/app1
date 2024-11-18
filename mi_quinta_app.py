import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título y descripción
st.title("Simulador de Crecimiento de Inversiones")
st.write("""
Esta app te permite proyectar el crecimiento de tus inversiones bajo diferentes escenarios. 
Puedes ajustar el monto inicial, las contribuciones periódicas, el rendimiento esperado y la duración de la inversión.
""")

# Parámetros de entrada
st.sidebar.header("Parámetros de Inversión")

# Monto inicial
monto_inicial = st.sidebar.number_input(
    "Monto inicial ($)", min_value=0.0, value=1000.0, step=100.0
)

# Contribución periódica
contribucion_periodica = st.sidebar.number_input(
    "Contribución periódica ($)", min_value=0.0, value=100.0, step=10.0
)

# Frecuencia de contribución
frecuencia = st.sidebar.selectbox(
    "Frecuencia de contribución",
    options=["Mensual", "Anual"]
)
frecuencia_meses = 1 if frecuencia == "Mensual" else 12

# Rendimiento anual esperado
rendimiento_anual = st.sidebar.slider(
    "Rendimiento anual esperado (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1
) / 100

# Duración de la inversión
duracion = st.sidebar.slider(
    "Duración de la inversión (años)", min_value=1, max_value=50, value=10, step=1
)

# Simulación
st.header("Resultados de la Simulación")

# Cálculo del crecimiento de la inversión
def simular_inversion(monto_inicial, contribucion, rendimiento, duracion, frecuencia_meses):
    meses = duracion * 12
    saldo = [monto_inicial]
    for mes in range(1, meses + 1):
        # Interés compuesto
        saldo_final_mes = saldo[-1] * (1 + rendimiento / 12)
        # Agregar contribución
        if mes % frecuencia_meses == 0:
            saldo_final_mes += contribucion
        saldo.append(saldo_final_mes)
    return saldo

# Ejecutar simulación
resultado_simulacion = simular_inversion(
    monto_inicial, contribucion_periodica, rendimiento_anual, duracion, frecuencia_meses
)

# Crear dataframe para mostrar resultados
meses = np.arange(0, duracion * 12 + 1)
df_resultados = pd.DataFrame({
    "Mes": meses,
    "Saldo": resultado_simulacion
})

# Mostrar resultados finales
saldo_final = df_resultados["Saldo"].iloc[-1]
st.metric("Saldo Final", f"${saldo_final:,.2f}")

# Gráfica
st.subheader("Crecimiento de la Inversión")
fig, ax = plt.subplots()
ax.plot(df_resultados["Mes"], df_resultados["Saldo"], label="Saldo acumulado", color="blue")
ax.set_xlabel("Meses")
ax.set_ylabel("Saldo ($)")
ax.set_title("Proyección del Crecimiento de la Inversión")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Mostrar tabla de resultados
st.subheader("Detalles de la Simulación")
st.dataframe(df_resultados)

# Nota al usuario
st.write("""
Nota: Este simulador asume un rendimiento anual constante y no considera impuestos ni inflación.
Para cálculos más precisos, consulta con un asesor financiero.
""")