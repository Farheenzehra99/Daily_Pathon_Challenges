import streamlit as st
import os

# Check if "assets" folder exists
print("Current Directory:", os.getcwd())
print("Assets Folder Exists:", os.path.exists("assets"))

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
txt_col1, txt_col2 = st.sidebar.columns([1, 4])
with txt_col1:
    st.write("➕")  # Addition icon
with txt_col2:
    st.write("**Addition (+)**: Adds two numbers.")

# Subtraction
txt_col1, txt_col2 = st.sidebar.columns([1, 4])
with txt_col1:
    st.write("➖")  # Subtraction icon
with txt_col2:
    st.write("**Subtraction (-)**: Subtracts second number from first.")

# Multiplication
txt_col1, txt_col2 = st.sidebar.columns([1, 4])
with txt_col1:
    st.write("✖️")  # Multiplication icon
with txt_col2:
    st.write("**Multiplication (*)**: Multiplies two numbers.")

# Division
txt_col1, txt_col2 = st.sidebar.columns([1, 4])
with txt_col1:
    st.write("➗")  # Division icon
with txt_col2:
    st.write("**Division (/)**: Divides first number by second.")

# Main UI
st.title("🧮 Smart Arithmetic Calculator")

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
