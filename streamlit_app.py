import streamlit as st
import random

# Título de la aplicación
st.title("Generador de Ejercicios de Cinemática")

# Descripción
st.write("""
### Bienvenido a la aplicación de cinemática.
Aquí puedes generar problemas de cinemática básicos y verificar tus respuestas.
""")

# Función para generar un ejercicio
def generar_ejercicio():
    tipo_problema = random.choice(['velocidad', 'desplazamiento', 'aceleración'])
    
    if tipo_problema == 'velocidad':
        # Generar valores aleatorios
        distancia = random.uniform(50, 200)  # en metros
        tiempo = random.uniform(5, 20)  # en segundos
        velocidad = distancia / tiempo
        
        # Mostrar el problema
        st.write(f"Calcula la **velocidad** en m/s, si la distancia es de {distancia:.2f} metros y el tiempo es de {tiempo:.2f} segundos.")
        return velocidad, 'velocidad'
    
    elif tipo_problema == 'desplazamiento':
        # Generar valores aleatorios
        velocidad = random.uniform(10, 30)  # en m/s
        tiempo = random.uniform(5, 15)  # en segundos
        desplazamiento = velocidad * tiempo
        
        # Mostrar el problema
        st.write(f"Calcula el **desplazamiento** en metros, si la velocidad es de {velocidad:.2f} m/s y el tiempo es de {tiempo:.2f} segundos.")
        return desplazamiento, 'desplazamiento'
    
    elif tipo_problema == 'aceleración':
        # Generar valores aleatorios
        velocidad_inicial = random.uniform(0, 10)  # en m/s
        velocidad_final = random.uniform(20, 50)  # en m/s
        tiempo = random.uniform(5, 15)  # en segundos
        aceleración = (velocidad_final - velocidad_inicial) / tiempo
        
        # Mostrar el problema
        st.write(f"Calcula la **aceleración** en m/s², si la velocidad inicial es de {velocidad_inicial:.2f} m/s, la velocidad final es de {velocidad_final:.2f} m/s, y el tiempo es de {tiempo:.2f} segundos.")
        return aceleración, 'aceleración'

# Generar un nuevo ejercicio
if st.button('Generar ejercicio'):
    solucion_correcta, tipo_problema = generar_ejercicio()
    
    # Espacio para que el usuario ingrese su respuesta
    respuesta = st.number_input(f'Introduce tu respuesta para {tipo_problema}:', format="%.2f")
    
    # Botón para verificar la respuesta
    if st.button('Verificar respuesta'):
        # Verificación con un margen de error pequeño
        margen_error = 0.1
        if abs(respuesta - solucion_correcta) < margen_error:
            st.success(f"¡Correcto! La respuesta es {solucion_correcta:.2f}")
        else:
            st.error(f"Incorrecto. La respuesta correcta es {solucion_correcta:.2f}")

