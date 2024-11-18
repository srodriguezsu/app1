import streamlit as st
import pandas as pd
import datetime

# Configuración inicial
st.title("App de Finanzas Personales")
st.write("Esta app te ayudará a gestionar tus finanzas personales. Creada por Sebastian Rodriguez Suarez")

# Configuración de la base de datos (archivo CSV)
archivo_csv = "finanzas.csv"

# Función para cargar datos
try:
    datos = pd.read_csv(archivo_csv)
except FileNotFoundError:
    datos = pd.DataFrame(columns=["Fecha", "Tipo", "Categoría", "Monto", "Descripción"])

# Selección de sección
seccion = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["Registro de Finanzas", "Resumen Semanal", "Resumen Mensual", "Metas de Ahorro"]
)

# 1. Registro de Finanzas
if seccion == "Registro de Finanzas":
    st.header("Registrar Ingresos o Gastos")
    fecha = st.date_input("Fecha", datetime.date.today())
    tipo = st.selectbox("Tipo", ["Ingreso", "Gasto"])
    categoria = st.text_input("Categoría (Ej: Alquiler, Comida, Entretenimiento, etc.)")
    monto = st.number_input("Monto", min_value=0.0, step=0.01)
    descripcion = st.text_area("Descripción")

    if st.button("Registrar"):
        nueva_fila = {"Fecha": fecha, "Tipo": tipo, "Categoría": categoria, "Monto": monto, "Descripción": descripcion}
        nueva_fila = pd.DataFrame([nueva_fila])  # Convertir el diccionario en un DataFrame
        datos = pd.concat([datos, nueva_fila], ignore_index=True)  # Concatenar filas

        datos.to_csv(archivo_csv, index=False)
        st.success("Registro guardado correctamente.")

    st.write("Datos actuales:")
    st.dataframe(datos)

# 2. Resumen Semanal
elif seccion == "Resumen Semanal":
    st.header("Resumen Semanal")
    hoy = datetime.date.today()
    inicio_semana = hoy - datetime.timedelta(days=hoy.weekday())
    fin_semana = inicio_semana + datetime.timedelta(days=6)

    st.write(f"Semana actual: {inicio_semana} - {fin_semana}")
    datos["Fecha"] = pd.to_datetime(datos["Fecha"])
    datos_semana = datos[(datos["Fecha"] >= pd.Timestamp(inicio_semana)) & (datos["Fecha"] <= pd.Timestamp(fin_semana))]

    ingresos = datos_semana[datos_semana["Tipo"] == "Ingreso"]["Monto"].sum()
    gastos = datos_semana[datos_semana["Tipo"] == "Gasto"]["Monto"].sum()
    balance = ingresos - gastos

    st.metric("Ingresos", f"${ingresos:.2f}")
    st.metric("Gastos", f"${gastos:.2f}")
    st.metric("Balance", f"${balance:.2f}")
    st.write("Detalles:")
    st.dataframe(datos_semana)

# 3. Resumen Mensual
elif seccion == "Resumen Mensual":
    st.header("Resumen Mensual")
    mes_actual = datetime.date.today().month
    anio_actual = datetime.date.today().year

    datos["Fecha"] = pd.to_datetime(datos["Fecha"])
    datos_mes = datos[(datos["Fecha"].dt.month == mes_actual) & (datos["Fecha"].dt.year == anio_actual)]

    ingresos = datos_mes[datos_mes["Tipo"] == "Ingreso"]["Monto"].sum()
    gastos = datos_mes[datos_mes["Tipo"] == "Gasto"]["Monto"].sum()
    balance = ingresos - gastos

    st.metric("Ingresos", f"${ingresos:.2f}")
    st.metric("Gastos", f"${gastos:.2f}")
    st.metric("Balance", f"${balance:.2f}")
    st.write("Detalles:")
    st.dataframe(datos_mes)

# 4. Metas de Ahorro
elif seccion == "Metas de Ahorro":
    st.header("Metas de Ahorro")
    meta_ahorro = st.number_input("Establece tu meta de ahorro mensual ($):", min_value=0.0, step=0.01)
    st.write(f"Tu meta de ahorro mensual actual es: ${meta_ahorro:.2f}")
    # Convertir la columna "Fecha" al tipo datetime y manejar errores
    if not datos.empty:  # Solo si el DataFrame no está vacío
        datos["Fecha"] = pd.to_datetime(datos["Fecha"], errors='coerce')
    
        # Eliminar filas con fechas no válidas
        datos = datos.dropna(subset=["Fecha"])

    mes_actual = datetime.date.today().month
    anio_actual = datetime.date.today().year
    datos_mes = datos[(datos["Fecha"].dt.month == mes_actual) & (datos["Fecha"].dt.year == anio_actual)]
    ingresos = datos_mes[datos_mes["Tipo"] == "Ingreso"]["Monto"].sum()
    gastos = datos_mes[datos_mes["Tipo"] == "Gasto"]["Monto"].sum()
    ahorro = ingresos - gastos

    st.metric("Ahorro Actual", f"${ahorro:.2f}")
    diferencia = ahorro - meta_ahorro
    if diferencia >= 0:
        st.success(f"¡Felicidades! Has alcanzado tu meta con ${diferencia:.2f} extra.")
    else:
        st.error(f"Estás por debajo de tu meta por ${-diferencia:.2f}.")

# Guardar datos actualizados
datos.to_csv(archivo_csv, index=False)
