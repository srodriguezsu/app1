import streamlit as st
import pandas as pd
import os

# Configuración inicial
st.title("Calculadora de PAPA")
st.write("Esta aplicación te ayudará a calcular tu PAPA global y el PAPA por tipología de asignaturas.")

# Archivo CSV para almacenar la información de materias
archivo_csv = "materias.csv"

# Verificar si el archivo existe, si no, crearlo con las columnas necesarias
if not os.path.exists(archivo_csv):
    columnas = ["Nombre", "Tipología", "Créditos", "Nota"]
    materias = pd.DataFrame(columns=columnas)
    materias.to_csv(archivo_csv, index=False)
else:
    # Leer el archivo CSV
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
    tipologia = st.selectbox("Tipología de la materia", ["Obligatoria", "Electiva", "Libre elección"])
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
