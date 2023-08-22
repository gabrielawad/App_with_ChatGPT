
import streamlit as st

def main():
    st.title("App de saludos personalizados")

    name = st.text_input("Por favor ingrese su nombre:")
    if name:
        st.write(f"¡Hola, {name}! Te damos la bienvenida a tu app de saludos personalizados.")

    ciudad = st.text_input("Por favor escriba el nombre de su lugar de nacimiento:")
    if ciudad:
        st.write(f"¡Hola, {name} de {ciudad}! Te damos la bienvenida a tu app de saludos personalizados.")


if __name__ == "__main__":
    main()
