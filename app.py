import streamlit as st
import math
import matplotlib.pyplot as plt


st.title("Aplicación Para Calcular Figuras y Relaciones Trigonométricas")

# Selección de figura
figura = st.selectbox("Selecciona una figura geométrica",["Circulo", "Triángulo", "Rectángulo", "Cuadrado"])

# Calculo de circulo
if figura == "Circulo":
   radio = st.slider ("Selecciona el radio", 0.0, 10.0, 5.0)
# Area de circulo
   area = math.pi * radio**2
# Perimetro de circulo
   perimetro = 2 * math.pi * radio**2
# Resultados
   st.metric("Área", f"{area:.2f}")
   st.metric("Perímetro",f"{perimetro:.2f}")
   st.success("¡Resultadps!")

# Calculo de triángulo
elif figura == "Triángulo":
   base = st.slider("Lado a", 0.0, 20.0, 5.0)
   altura = st.slider("Lado b", 0.0, 20.0, 5.0)
   lado_a = st.slider("Lado a", 0.0, 20.0, 5.0)
   lado_b = st.slider("Lado b", 0.0, 20.0, 5.0)
   lado_c = st.slider("Lado c", 0.0, 20.0, 5.0)
#Area de triangulo
   area = 0.5 * base * altura
# Perímetro
   perimetro = lado_a + ladp_b + lado_c
# resultados
   st.metric("Área",f"{area:.2f}")
   st.metric("Perímetro",f"{perimetro:.2f}")
   st.success("¡Resultados!")

# Rectángulo
elif figura == "Rectángulo":
   base = st.slider("Selecciona la base", 0.0, 20.0, 5.0)
   altura = st.slider("Selecciona la altura", 0.0, 20.0, 5.0)
# Área de rectángulo
   area = base * altura
# Perímetro de rectángulo
   perimetro = 2 * (base + altura)
# Resultados
   st.metric("Área", f"{area:.2f}")
   st.metric("Perímetro", f"{perimetro:.2f}")
   st.success("¡Resultados!")

# Cuadrado
elif figura == "Cuadrado":
   lado = st.slider("Selecciona el lado", 0.0, 20.0, 5.0)
# Area de cuadrado
   area = lado**2
# Perímetro de cuadrado
   perimetro = 4 * lado
# Resultados
   st.metric("Área",f"{area:.2f}")
   st.metric("Perímetro",f"{perimetro:.2f}")
   st.success("¡Resultados!")

   

