import streamlit as st
import wikipedia

def main():
    st.title("Country Capital Lookup")

    # Get a list of countries from Wikipedia
    countries = wikipedia.page("List of countries and capitals with currency and language").links

    # Create a dropdown for country selection
    selected_country = st.selectbox("Select a country", countries)

    # Retrieve the capital of the selected country from Wikipedia
    try:
        country_page = wikipedia.page(selected_country)
        capital = None
        for line in country_page.content.split("\n"):
            if "Capital" in line:
                capital = line.split(":")[1].strip()
                break
        if capital:
            st.success(f"The capital of {selected_country} is {capital}.")
        else:
            st.error("Capital information not found.")
    except wikipedia.exceptions.PageError:
        st.error("Country information not found.")

if __name__ == "__main__":
    main()
