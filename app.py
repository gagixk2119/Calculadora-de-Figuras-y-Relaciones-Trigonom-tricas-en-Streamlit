import streamlit as st
import math


st.title("Aplicación Para Calcular Figuras y Relaciones Trigonométricas")

# Selección de figura
figura = st.selectbox("Selecciona una figura geométrica",["Circulo", "Triángulo", "Rectángulo", "Cuadrado"])

# Calculo de circulo
if figura == "Circulo"
radio = st.slider ("Selecciona el radio", 0.0, 10.0, 5.0)

# Area de circulo
area = math.pi * radio**2

# Perimetro de circulo
perimetro = 2 * math.pi * radio**2

# Resultados
st.metric("Área", f"{area:.2f}")
st.metric("Perímetro",f"{perimetro:.2f}")
st.succes("¡Resultadps!")

# Calculo de triángulo
elif figura == "Triángulo"
base = st.slider("Lado a", 0.0, 20.0, 5.0)
altura = st.slider("Lado b", 0.0, 20.0, 5.0)

