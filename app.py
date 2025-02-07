import streamlit as st
import random
from PIL import Image
import time

# Configuración de la página
st.set_page_config(page_title="Juego de las Galletas", page_icon="🍪")

# Título
st.title("¡Bienvenido al Juego de las Galletas del Calamar!")
st.write("El objetivo del juego es romper la galleta sin romper las líneas.")

# Subir una imagen de la galleta
st.write("### Imagen de la Galleta")
galleta_img = Image.open('cookie_image.jpg')  # Reemplaza con tu imagen de galleta
st.image(galleta_img, caption="¿Puedes romper la galleta sin tocar los bordes?")

# Juego
st.write("### Instrucciones:")
st.write("Haz clic en la galleta y completa el desafío sin hacer clic fuera de los límites.")
st.write("Si tocas el borde, pierdes.")

# Tiempo para hacer el clic
st.write("### Reloj")
tiempo_restante = st.slider("Tiempo para romper la galleta (segundos)", 5, 30, 10)
st.write(f"Tiempo restante: {tiempo_restante} segundos.")

# Comenzar juego
if st.button("¡Comenzar el Juego!"):
    st.write("Juego comenzando...")
    time.sleep(1)
    st.write(f"¡Corre! Tienes {tiempo_restante} segundos.")
    
    # Contador regresivo
    for i in range(tiempo_restante, 0, -1):
        st.write(f"Tiempo restante: {i} segundos.")
        time.sleep(1)
    
    st.write("¡El tiempo ha terminado!")

    # Resultado
    resultado = random.choice(["¡Ganaste!", "¡Perdiste!"])
    st.write(f"Resultado: {resultado}")
    
    if resultado == "¡Perdiste!":
        st.write("Recuerda, no puedes romper los bordes de la galleta.")
    
# Final
st.write("¡Gracias por jugar!")
