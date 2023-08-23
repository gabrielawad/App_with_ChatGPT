import streamlit as st

def temperature_conversion():
    st.subheader("Temperature Conversion")
    options = ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
    selected_option = st.selectbox("Select Conversion", options)
    
    if selected_option == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius", value=0.0)
        fahrenheit = celsius * 9/5 + 32
        st.write(f"{celsius:.2f} °C is equal to {fahrenheit:.2f} °F")
    else:
        fahrenheit = st.number_input("Enter temperature in Fahrenheit", value=32.0)
        celsius = (fahrenheit - 32) * 5/9
        st.write(f"{fahrenheit:.2f} °F is equal to {celsius:.2f} °C")

def length_conversion():
    st.subheader("Length Conversion")
    options = ["Meters to Feet", "Feet to Meters"]
    selected_option = st.selectbox("Select Conversion", options)
    
    if selected_option == "Meters to Feet":
        meters = st.number_input("Enter length in meters", value=0.0)
        feet = meters * 3.281
        st.write(f"{meters:.2f} meters is equal to {feet:.2f} feet")
    else:
        feet = st.number_input("Enter length in feet", value=0.0)
        meters = feet / 3.281
        st.write(f"{feet:.2f} feet is equal to {meters:.2f} meters")

def weight_conversion():
    st.subheader("Weight/Mass Conversion")
    options = ["Kilograms to Pounds", "Pounds to Kilograms"]
    selected_option = st.selectbox("Select Conversion", options)
    
    if selected_option == "Kilograms to Pounds":
        kilograms = st.number_input("Enter weight in kilograms", value=0.0)
        pounds = kilograms * 2.205
        st.write(f"{kilograms:.2f} kilograms is equal to {pounds:.2f} pounds")
    else:
        pounds = st.number_input("Enter weight in pounds", value=0.0)
        kilograms = pounds / 2.205
        st.write(f"{pounds:.2f} pounds is equal to {kilograms:.2f} kilograms")

def volume_conversion():
    st.subheader("Volume Conversion")
    options = ["Liters to Gallons", "Gallons to Liters"]
    selected_option = st.selectbox("Select Conversion", options)
    
    if selected_option == "Liters to Gallons":
        liters = st.number_input("Enter volume in liters", value=0.0)
        gallons = liters * 0.264
        st.write(f"{liters:.2f} liters is equal to {gallons:.2f} gallons")
    else:
        gallons = st.number_input("Enter volume in gallons", value=0.0)
        liters = gallons / 0.264
        st.write(f"{gallons:.2f} gallons is equal to {liters:.2f} liters")

def time_conversion():
    st.subheader("Time Conversion")
    options = ["Hours to Minutes", "Minutes to Hours"]
    selected_option = st.selectbox("Select Conversion", options)
    
    if selected_option == "Hours to Minutes":
        hours = st.number_input("Enter time in hours", value=0.0)
        minutes = hours * 60
        st.write(f"{hours:.2f} hours is equal to {minutes:.2f} minutes")
    else:
        minutes = st.number_input("Enter time in minutes", value=0.0)
        hours = minutes / 60
        st.write(f"{minutes:.2f} minutes is equal to {hours:.2f} hours")

def main():
    st.title("Unit Conversion App")
    
    conversion_options = [
        "Temperature", "Length", "Weight/Mass", "Volume", "Time"
    ]
    selected_conversion = st.selectbox("Select Conversion Type", conversion_options)

    if selected_conversion == "Temperature":
        temperature_conversion()
    elif selected_conversion == "Length":
        length_conversion()
    elif selected_conversion == "Weight/Mass":
        weight_conversion()
    elif selected_conversion == "Volume":
        volume_conversion()
    elif selected_conversion == "Time":
        time_conversion()

if __name__ == "__main__":
    main()
