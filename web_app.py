
import streamlit as st

def main():
    st.title("Personalized Greeting App")

    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello, {name}! Welcome to your personalized greeting app.")

if __name__ == "__main__":
    main()
