import streamlit as st
from streamlit_lottie import st_lottie
import json

# Function to load Lottie animation
def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load animation
lottie_calc = load_lottie_file("assets/calculator.json")

# Set Page Configuration
st.set_page_config(page_title="Smart Calculator", page_icon="🧮", layout="wide")

# Dark mode theme
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("🔢 Operations Guide")

# Addition
col1, col2 = st.sidebar.columns([1, 4])
with col1:
    st.image("assets/add.png", width=30)  # Addition icon
with col2:
    st.write("**Addition (+)**: Adds two numbers.")

# Subtraction
col1, col2 = st.sidebar.columns([1, 4])
with col1:
    st.image("assets/substraction.png", width=30)  # Subtraction icon
with col2:
    st.write("**Subtraction (-)**: Subtracts second number from first.")

# Multiplication
col1, col2 = st.sidebar.columns([1, 4])
with col1:
    st.image("assets/multiplication.png", width=30)  # Multiplication icon
with col2:
    st.write("**Multiplication (*)**: Multiplies two numbers.")

# Division
col1, col2 = st.sidebar.columns([1, 4])
with col1:
    st.image("assets/divide.png", width=50)  # Division icon
with col2:
    st.write("**Division (/)**: Divides first number by second.")



# Main UI
st.title("🧮 Smart Arithmetic Calculator")
st_lottie(lottie_calc, height=200, key="calc")

# User selects operation
operation = st.radio("Choose an operation:", ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"])

# User input for numbers
num1 = st.number_input("Enter first number:", format="%.2f")
num2 = st.number_input("Enter second number:", format="%.2f")

# Perform Calculation
if st.button("Calculate 🚀"):
    st.write("🧮 **Calculating...**")
    
    if operation == "Addition (+)":
        result = num1 + num2
        st.success(f"{num1} + {num2} = {result}")
    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.success(f"{num1} - {num2} = {result}")
    elif operation == "Multiplication (*)":
        result = num1 * num2
        st.success(f"{num1} × {num2} = {result}")
    elif operation == "Division (/)":
        if num2 == 0:
            st.error("❌ Error: Division by zero is not allowed!")
        else:
            result = num1 / num2
            st.success(f"{num1} ÷ {num2} = {result}")
