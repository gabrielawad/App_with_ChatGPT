#pip install wikipedia

# Import necessary libraries
import streamlit as st
#import wikipedia

# App title and header
st.title("Country Information App")
st.header("Select a Continent and Country")

# Dictionary mapping continents to countries
countries_by_continent = {
    "Asia": ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", 
             "Bhutan", "Brunei", "Cambodia", "China", "Cyprus", "Georgia", 
             "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", 
             "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", 
             "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", 
             "North Korea", "Oman", "Pakistan", "Palestine", "Philippines", 
             "Qatar", "Russia", "Saudi Arabia", "Singapore", "South Korea", 
             "Sri Lanka", "Syria", "Taiwan", "Tajikistan", "Thailand", 
             "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", 
             "Uzbekistan", "Vietnam", "Yemen"],
    "Americas": ["Antigua and Barbuda", "Argentina", "Bahamas", "Barbados", 
                 "Belize", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", 
                 "Costa Rica", "Cuba", "Dominica", "Dominican Republic", 
                 "Ecuador", "El Salvador", "Grenada", "Guatemala", "Guyana", 
                 "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", 
                 "Panama", "Paraguay", "Peru", "Saint Kitts and Nevis", 
                 "Saint Lucia", "Saint Vincent and the Grenadines", 
                 "Suriname", "Trinidad and Tobago", "United States", 
                 "Uruguay", "Venezuela"],
    "Africa": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", 
               "Burundi", "Cabo Verde", "Cameroon", "Central African Republic",
               "Chad", "Comoros", "Congo, Democratic Republic of the", 
               "Congo, Republic of the", "Cote d'Ivoire", "Djibouti", "Egypt", 
               "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", 
               "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", 
               "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", 
               "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", 
               "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", 
               "Seychelles", "Sierra Leone", "Somalia", "South Africa", 
               "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", 
               "Zambia", "Zimbabwe"],
    "Europe": ["Albania", "Andorra", "Austria", "Belarus", "Belgium", 
               "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", 
               "Czech Republic", "Denmark", "Estonia", "Finland", "France", 
               "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", 
               "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", 
               "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", 
               "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", 
               "Romania", "Russia", "San Marino", "Serbia", "Slovakia", 
               "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", 
               "United Kingdom", "Vatican City"],
    "Oceania": ["Australia", "Fiji", "Kiribati", "Marshall Islands", 
                "Micronesia", "Nauru", "New Zealand", "Palau", 
                "Papua New Guinea", "Samoa", "Solomon Islands", 
                "Tonga", "Tuvalu", "Vanuatu"]
}}

# Dropdown for selecting a continent
continent = st.selectbox("Select Continent", list(countries_by_continent.keys()))

# Dropdown for selecting a country based on the continent selection
country = st.selectbox("Select Country", countries_by_continent.get(continent, []))
"""
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
"""
