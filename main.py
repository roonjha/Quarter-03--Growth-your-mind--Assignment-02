import streamlit as st
import time

# Define conversion factors globally
conversion_factors = {
    'Length': {
        'meters': 1, 'kilometers': 0.001, 'centimeters': 100, 'millimeters': 1000,
        'miles': 0.000621371, 'yards': 1.09361, 'feet': 3.28084, 'inches': 39.3701,
        'nautical miles': 0.000539957
    },
    'Weight': {
        'grams': 1, 'kilograms': 0.001, 'milligrams': 1000, 'pounds': 0.00220462,
        'ounces': 0.035274, 'tons': 0.00000110231, 'carats': 5, 'stones': 0.000157473
    },
    'Volume': {
        'liters': 1, 'milliliters': 1000, 'cubic meters': 0.001, 'cubic centimeters': 1000,
        'gallons': 0.264172, 'quarts': 1.05669, 'pints': 2.11338, 'cups': 4.22675,
        'fluid ounces': 33.814, 'barrels': 0.00628981
    },
    'Temperature': {
        'Celsius': lambda x: x, 'Fahrenheit': lambda x: (x * 9/5) + 32, 'Kelvin': lambda x: x + 273.15
    },
    'Energy': {
        'joules': 1, 'kilojoules': 0.001, 'calories': 0.239006, 'kilocalories': 0.000239006,
        'BTU': 0.000947817, 'electronvolts': 6.242e+18, 'ergs': 1e+7
    },
    'Pressure': {
        'pascals': 1, 'kilopascals': 0.001, 'bar': 0.00001, 'atm': 0.00000986923,
        'psi': 0.000145038, 'torr': 0.00750062, 'mmHg': 0.00750062
    },
    'Speed': {
        'm/s': 1, 'km/h': 3.6, 'mph': 2.23694, 'knots': 1.94384, 'ft/s': 3.28084,
        'mach': 0.00293858
    },
    'Time': {
        'seconds': 1, 'minutes': 0.0166667, 'hours': 0.000277778, 'days': 0.0000115741,
        'weeks': 0.00000165344, 'months': 0.000000380257, 'years': 0.0000000316881,
        'decades': 0.00000000316881, 'centuries': 0.000000000316881
    },
    'Power': {
        'watts': 1, 'kilowatts': 0.001, 'horsepower': 0.00134102, 'BTU/hr': 3.41214,
        'ergs/sec': 1e+7
    },
    'Data Storage': {
        'bytes': 1, 'kilobytes': 0.001, 'megabytes': 0.000001, 'gigabytes': 0.000000001,
        'terabytes': 0.000000000001, 'bits': 8, 'kilobits': 0.008, 'megabits': 0.000008,
        'gigabits': 0.000000008, 'petabytes': 0.000000000000001
    },
    'Area': {
        'square meters': 1, 'square kilometers': 0.000001, 'square miles': 0.000000386102,
        'square feet': 10.7639, 'square inches': 1550, 'hectares': 0.0001, 'acres': 0.000247105
    }
}

# Function to perform unit conversion
def convert_units(value, from_unit, to_unit, category):
    if category == 'Temperature':
        return conversion_factors[category][to_unit](value) if from_unit == 'Celsius' else None
    return value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])

# Set page config
st.set_page_config(page_title="Growth Mind Challenge - Assignment No. 02", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Main title styling */
        .main-title {
            font-size: 36px;
            font-weight: bold;
            color: #2E86C1;
            text-align: center;
            margin-bottom: 20px;
        }
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #2E86C1 !important;
            padding: 20px !important;
            color: white !important;
        }
        .sidebar-title {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        .sidebar-info {
            font-size: 16px;
            line-height: 1.6;
        }
        /* Button styling */
        .stButton button {
            background-color: #2E86C1 !important;
            color: white !important;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
            width: 100%;
        }
        .stButton button:hover {
            background-color: #1B4F72 !important;
        }
        /* Input and select box styling */
        .stNumberInput, .stSelectbox {
            width: 100%;
        }
        /* Result styling */
        .stSuccess {
            font-size: 20px;
            font-weight: bold;
            color: #28B463;
        }
        /* Reset button styling */
        .reset-button {
            background-color: #E74C3C !important;
            color: white !important;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
            width: 100%;
        }
        .reset-button:hover {
            background-color: #B03A2E !important;
        }
    </style>
""", unsafe_allow_html=True)

# Typewriter effect for the title
def typewriter_effect(text, delay=50):
    placeholder = st.empty()
    typed_text = ""
    for char in text:
        typed_text += char
        placeholder.markdown(f'<div class="main-title">{typed_text}</div>', unsafe_allow_html=True)
        time.sleep(delay / 1000)  # Convert delay to seconds

# Initialize session state
if "show_title" not in st.session_state:
    st.session_state.show_title = False
if "result" not in st.session_state:
    st.session_state.result = None

# Display the title with typewriter effect
if not st.session_state.show_title:
    typewriter_effect("Growth Mind Challenge - Assignment No. 02", delay=50)
    st.session_state.show_title = True

# Sidebar for unit information
with st.sidebar:
    st.markdown('<div class="sidebar-title">Unit Conversion Information</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="sidebar-info">
            <p>This app allows you to convert between various units across multiple categories, including:</p>
            <ul>
                <li>Length</li>
                <li>Weight</li>
                <li>Volume</li>
                <li>Temperature</li>
                <li>Energy</li>
                <li>Pressure</li>
                <li>Speed</li>
                <li>Time</li>
                <li>Power</li>
                <li>Data Storage</li>
                <li>Area</li>
            </ul>
            <p>Select a category and units to perform the conversion.</p>
        </div>
    """, unsafe_allow_html=True)

# Main converter interface
st.title("Unit Converter")
category = st.selectbox("Select Category", list(conversion_factors.keys()), index=0)
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From Unit", list(conversion_factors[category].keys()))
with col2:
    to_unit = st.selectbox("To Unit", list(conversion_factors[category].keys()))
value = st.number_input("Enter Value to Convert", value=0.0, step=0.1)

# Convert and Reset buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, category)
        st.success(f"Converted Value: {result} {to_unit}")
        st.session_state.result = result  # Store result in session state
with col2:
    if st.button("Reset", key="reset", help="Click to reset inputs", use_container_width=True):
        st.session_state.result = None  # Clear result
        st.session_state.show_title = False  # Reset title animation
        st.rerun()  # Refresh the app

# Display conversion result in the sidebar
if st.session_state.result is not None:
    st.sidebar.subheader("Conversion Result")
    st.sidebar.write(f"{value} {from_unit} = {st.session_state.result} {to_unit}")