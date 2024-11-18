import streamlit as st
import pandas as pd
import os
import io

# Configuración inicial
st.title("Calculadora de PAPA")
st.write("Esta aplicación te ayudará a calcular tu PAPA global y el PAPA por tipología de asignaturas. Creado por Sebastián Rodríguez Suarez")

# Instrucciones sobre la estructura del archivo CSV
st.write("""
### Estructura del archivo CSV:
El archivo debe contener las siguientes columnas:
1. **Nombre**: Nombre de la materia.
2. **Tipología**: Tipo de materia (puede ser "Obligatoria", "Optativa" o "Libre elección").
3. **Créditos**: Número de créditos de la materia.
4. **Nota**: Nota obtenida en la materia (debe ser un valor entre 0 y 5).

El archivo debe estar en formato CSV y tener un aspecto similar al siguiente:
Nombre,Tipología,Créditos,Nota 
Calculo,Obligatoria,4,4.5 
Física,Optativa,3,3.8 
Programación,Libre elección,2,5.0
""")


# Sección de subida de archivo CSV
uploaded_file = st.sidebar.file_uploader("Sube tu archivo CSV", type=["csv"])

# Verificar si el archivo CSV ha sido subido
if uploaded_file is not None:
    try:
        # Leer el archivo CSV
        materias = pd.read_csv(uploaded_file)

        # Validación de la estructura del archivo CSV
        required_columns = ["Nombre", "Tipología", "Créditos", "Nota"]
        if all(col in materias.columns for col in required_columns):
            st.success("Archivo CSV cargado correctamente.")
        else:
            st.error(f"El archivo CSV debe contener las siguientes columnas: {', '.join(required_columns)}")
    except Exception as e:
        st.error(f"Error al cargar el archivo CSV: {e}")

# Si no hay archivo CSV cargado, trabajar con el archivo por defecto
else:
    # Archivo CSV por defecto
    archivo_csv = "materias.csv"

    # Verificar si el archivo existe, si no, crearlo con las columnas necesarias
    if not os.path.exists(archivo_csv):
        columnas = ["Nombre", "Tipología", "Créditos", "Nota"]
        materias = pd.DataFrame(columns=columnas)
        materias.to_csv(archivo_csv, index=False)
    else:
        # Leer el archivo CSV por defecto
        materias = pd.read_csv(archivo_csv)

# Sección del menú lateral
seccion = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["Agregar Materia", "Calcular PAPA Global", "Calcular PAPA por Tipología"]
)

# 1. Agregar Materias
if seccion == "Agregar Materia":
    st.header("Agregar Materia")
    nombre = st.text_input("Nombre de la materia")
    tipologia = st.selectbox("Tipología de la materia", ["Obligatoria", "Optativa", "Libre elección"])
    creditos = st.number_input("Número de créditos", min_value=1, step=1)
    nota = st.number_input("Nota obtenida", min_value=0.0, max_value=5.0, step=0.1)

    if st.button("Agregar Materia"):
        if nombre and creditos > 0 and 0 <= nota <= 5:
            nueva_materia = {
                "Nombre": nombre,
                "Tipología": tipologia,
                "Créditos": creditos,
                "Nota": nota
            }
            nueva_materia_df = pd.DataFrame([nueva_materia])
            materias = pd.concat([materias, nueva_materia_df], ignore_index=True)
            if uploaded_file is not None:
                # Guardar el archivo CSV actualizado si se cargó un archivo
                materias.to_csv(uploaded_file, index=False)
            else:
                # Si no se cargó archivo CSV, guardar en el archivo local
                materias.to_csv(archivo_csv, index=False)
            st.success("Materia agregada correctamente.")
        else:
            st.error("Por favor, ingresa todos los datos correctamente.")

    st.write("Materias registradas hasta ahora:")
    st.dataframe(materias)

# 2. Calcular PAPA Global
elif seccion == "Calcular PAPA Global":
    st.header("Cálculo del PAPA Global")

    if materias.empty:
        st.warning("No hay materias registradas. Agrega materias en la sección 'Agregar Materia'.")
    else:
        # Cálculo del PAPA Global
        total_creditos = materias["Créditos"].sum()
        if total_creditos > 0:
            papa_global = (materias["Créditos"] * materias["Nota"]).sum() / total_creditos
            st.metric("PAPA Global", f"{papa_global:.2f}")
        else:
            st.error("No hay créditos suficientes para calcular el PAPA.")

        st.write("Materias registradas:")
        st.dataframe(materias)

# 3. Calcular PAPA por Tipología
elif seccion == "Calcular PAPA por Tipología":
    st.header("Cálculo del PAPA por Tipología")

    if materias.empty:
        st.warning("No hay materias registradas. Agrega materias en la sección 'Agregar Materia'.")
    else:
        tipologias = materias["Tipología"].unique()
        for tipologia in tipologias:
            materias_tipologia = materias[materias["Tipología"] == tipologia]
            total_creditos_tipologia = materias_tipologia["Créditos"].sum()

            if total_creditos_tipologia > 0:
                papa_tipologia = (
                    (materias_tipologia["Créditos"] * materias_tipologia["Nota"]).sum() / 
                    total_creditos_tipologia
                )
                st.metric(f"PAPA - {tipologia}", f"{papa_tipologia:.2f}")
            else:
                st.warning(f"No hay créditos suficientes para calcular el PAPA de {tipologia}.")

        st.write("Materias registradas por tipología:")
        st.dataframe(materias)

