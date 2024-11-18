import streamlit as st

# Título de la app
st.title("Conversor Universal")

# Autor
st.write("Esta app fue elaborada por “Sebastian Rodriguez Suarez”.")

# Selección de categoría
categoria = st.selectbox(
    "Selecciona una categoría:",
    [
        "Temperatura",
        "Longitud",
        "Peso/Masa",
        "Volumen",
        "Tiempo",
        "Velocidad",
        "Área",
        "Energía",
        "Presión",
        "Tamaño de Datos"
    ]
)

# Diccionario de conversiones
if categoria == "Temperatura":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        [
            "Celsius a Fahrenheit",
            "Fahrenheit a Celsius",
            "Celsius a Kelvin",
            "Kelvin a Celsius"
        ]
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if st.button("Convertir"):
        if conversion == "Celsius a Fahrenheit":
            resultado = (valor * 9 / 5) + 32
        elif conversion == "Fahrenheit a Celsius":
            resultado = (valor - 32) * 5 / 9
        elif conversion == "Celsius a Kelvin":
            resultado = valor + 273.15
        elif conversion == "Kelvin a Celsius":
            resultado = valor - 273.15
        st.write(f"Resultado: {resultado}")

elif categoria == "Longitud":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        [
            "Pies a metros",
            "Metros a pies",
            "Pulgadas a centímetros",
            "Centímetros a pulgadas"
        ]
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if st.button("Convertir"):
        if conversion == "Pies a metros":
            resultado = valor * 0.3048
        elif conversion == "Metros a pies":
            resultado = valor / 0.3048
        elif conversion == "Pulgadas a centímetros":
            resultado = valor * 2.54
        elif conversion == "Centímetros a pulgadas":
            resultado = valor / 2.54
        st.write(f"Resultado: {resultado}")

elif categoria == "Peso/Masa":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        [
            "Libras a kilogramos",
            "Kilogramos a libras",
            "Onzas a gramos",
            "Gramos a onzas"
        ]
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if st.button("Convertir"):
        if conversion == "Libras a kilogramos":
            resultado = valor * 0.453592
        elif conversion == "Kilogramos a libras":
            resultado = valor / 0.453592
        elif conversion == "Onzas a gramos":
            resultado = valor * 28.3495
        elif conversion == "Gramos a onzas":
            resultado = valor / 28.3495
        st.write(f"Resultado: {resultado}")

elif categoria == "Volumen":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        [
            "Galones a litros",
            "Litros a galones",
            "Pulgadas cúbicas a centímetros cúbicos",
            "Centímetros cúbicos a pulgadas cúbicas"
        ]
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if st.button("Convertir"):
        if conversion == "Galones a litros":
            resultado = valor * 3.78541
        elif conversion == "Litros a galones":
            resultado = valor / 3.78541
        elif conversion == "Pulgadas cúbicas a centímetros cúbicos":
            resultado = valor * 16.3871
        elif conversion == "Centímetros cúbicos a pulgadas cúbicas":
            resultado = valor / 16.3871
        st.write(f"Resultado: {resultado}")

elif categoria == "Tiempo":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        [
            "Horas a minutos",
            "Minutos a segundos",
            "Días a horas",
            "Semanas a días"
        ]
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if st.button("Convertir"):
        if conversion == "Horas a minutos":
            resultado = valor * 60
        elif conversion == "Minutos a segundos":
            resultado = valor * 60
        elif conversion == "Días a horas":
            resultado = valor * 24
        elif conversion == "Semanas a días":
            resultado = valor * 7
        st.write(f"Resultado: {resultado}")

elif categoria == "Velocidad":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        [
            "Millas por hora a kilómetros por hora",
            "Kilómetros por hora a metros por segundo",
            "Nudos a millas por hora",
            "Metros por segundo a pies por segundo"
        ]
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if st.button("Convertir"):
        if conversion == "Millas por hora a kilómetros por hora":
            resultado = valor * 1.60934
        elif conversion == "Kilómetros por hora a metros por segundo":
            resultado = valor / 3.6
        elif conversion == "Nudos a millas por hora":
            resultado = valor * 1.15078
        elif conversion == "Metros por segundo a pies por segundo":
            resultado = valor * 3.28084
        st.write(f"Resultado: {resultado}")

# Puedes continuar con las categorías restantes con la misma estructura.
