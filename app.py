import streamlit as st
import math


st.title("Aplicación Para Calcular Figuras y Relaciones Trigonométricas")

# Selección de figura
figura = st.selectbox("Selecciona una figura geométrica",["Circulo"])

# Widget para ingresar el radio
radio = st.slider ("Selecciona el radio", 0.0, 10.0, 5.0)

# Calculo del área de circulo 
area = math.pi * radio**2

# Mostrar resultado
st.write(f"El área del círculo con radio {radio} es: {area: .2f}")

# Calculo del perímetro de circulo
perimetro = 2 * math.pi * radio 

