# Import necessary libraries
import streamlit as st
import wikipedia

# App title and header
st.title("Country Information App")
st.header("Select a Continent and Country")

# Dictionary mapping continents to countries
countries_by_continent = {
    "Asia": ["Japan", "India", "China"],  # Add more countries as needed
    "Africa": ["Nigeria", "Egypt", "South Africa"],
    "Europe": ["Germany", "France", "United Kingdom"],
    "North America": ["USA", "Canada", "Mexico"],
    "South America": ["Brazil", "Argentina", "Colombia"],
    "Oceania": ["Australia", "New Zealand"]
}

# Dropdown for selecting a continent
continent = st.selectbox("Select Continent", list(countries_by_continent.keys()))

# Dropdown for selecting a country based on the continent selection
country = st.selectbox("Select Country", countries_by_continent.get(continent, []))

# Fetch country information from Wikipedia
page = wikipedia.page(country)
capital = page.summary.split("Capital: ")[1].split("\n")[0]
size = page.summary.split("Area: ")[1].split(" km²")[0]
population = page.summary.split("Population: ")[1].split("\n")[0]

# Get the main tourist attractions using the `wikipedia` library's content method
tourist_attractions = wikipedia.page(country + " tourist attractions").content
attractions_list = []
for line in tourist_attractions.split("\n"):
    if line.startswith("*"):
        attractions_list.append(line.strip("*").strip())

# Display the fetched information
st.subheader("Country Information")
st.write(f"Capital: {capital}")
st.write(f"Size (square kilometres): {size} km²")
st.write(f"Population: {population}")

st.subheader("Five Main Tourist Attractions")
for i, attraction in enumerate(attractions_list[:5]):
    st.write(f"{i+1}. {attraction}")
