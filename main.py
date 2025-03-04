import streamlit as st
import time

# Define conversion factors globally
conversion_factors = {
    'Length': {'meters': 1, 'kilometers': 0.001, 'miles': 0.000621371, 'feet': 3.28084},
    'Weight': {'grams': 1, 'kilograms': 0.001, 'pounds': 0.00220462, 'ounces': 0.035274},
    'Volume': {'liters': 1, 'milliliters': 1000, 'gallons': 0.264172, 'cups': 4.22675},
    'Temperature': {'Celsius': lambda x: x, 'Fahrenheit': lambda x: (x * 9/5) + 32, 'Kelvin': lambda x: x + 273.15},
    'Energy': {'joules': 1, 'kilojoules': 0.001, 'calories': 0.239006, 'BTU': 0.000947817},
    'Pressure': {'pascals': 1, 'bar': 0.00001, 'atm': 0.00000986923, 'psi': 0.000145038},
    'Speed': {'m/s': 1, 'km/h': 3.6, 'mph': 2.23694, 'knots': 1.94384},
    'Time': {'seconds': 1, 'minutes': 0.0166667, 'hours': 0.000277778, 'days': 0.0000115741},
    'Power': {'watts': 1, 'kilowatts': 0.001, 'horsepower': 0.00134102},
    'Data Storage': {'bytes': 1, 'kilobytes': 0.001, 'megabytes': 0.000001, 'gigabytes': 0.000000001}
}

def convert_units(value, from_unit, to_unit, category):
    if category == 'Temperature':
        return conversion_factors[category][to_unit](value) if from_unit == 'Celsius' else None
    return value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])

# Set page config
st.set_page_config(page_title="Growth Your Mind - Project 02", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #ADD8E6 !important; /* Light blue */
            padding: 20px !important;
        }
        /* Center the title and button */
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            gap: 10px; /* Reduce space between elements */
        }
        /* Typewriter effect styling */
        .typewriter {
            font-size: 24px;
            font-weight: bold;
            color: black;
            text-align: center;
        }
        /* Blue button styling */
        .blue-button {
            background-color: blue !important;
            color: white !important;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .blue-button:hover {
            background-color: darkblue !important;
        }
        /* Compact layout */
        .stButton button {
            width: 100%;
        }
        .stNumberInput, .stSelectbox {
            width: 100%;
        }
        /* Result styling */
        .stSuccess {
            font-size: 20px;
            font-weight: bold;
            color: green;
        }
    </style>
""", unsafe_allow_html=True)

# Typewriter effect for the button text
def typewriter_effect(text, delay=50):
    placeholder = st.empty()
    typed_text = ""
    for char in text:
        typed_text += char
        placeholder.markdown(f'<div class="center"><button class="blue-button">{typed_text}</button></div>', unsafe_allow_html=True)
        time.sleep(delay / 1000)  # Convert delay to seconds

# Initial page setup
if "show_title" not in st.session_state:
    st.session_state.show_title = False

# Display the button with typewriter effect
if not st.session_state.show_title:
    typewriter_effect("Start Unit Calculation", delay=50)
    if st.button("Start Unit Calculation", key="start", help="Click to begin conversion", use_container_width=True):
        st.session_state.show_title = True

# Display the title and converter after clicking the button
if st.session_state.show_title:
    st.markdown('<div class="center"><div class="typewriter">Growth Your Mind and Project 02</div></div>', unsafe_allow_html=True)

    st.sidebar.title("Unit Information")
    st.sidebar.write("Select a category and units to convert.")

    # Main converter interface
    st.title("Unit Converter")
    col1, col2 = st.columns(2)  # Split into two columns for compact layout
    with col1:
        category = st.selectbox("Select Category", list(conversion_factors.keys()), index=0)
        from_unit = st.selectbox("From Unit", list(conversion_factors[category].keys()))
    with col2:
        to_unit = st.selectbox("To Unit", list(conversion_factors[category].keys()))
        value = st.number_input("Enter Value to Convert", value=0.0, step=0.1)

    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, category)
        st.success(f"Converted Value: {result} {to_unit}")

        # Display conversion result in the sidebar
        st.sidebar.subheader("Conversion Result")
        st.sidebar.write(f"{value} {from_unit} = {result} {to_unit}")