# import streamlit as st

# # 🖥 Set Page Configuration
# st.set_page_config(page_title="Even or Odd Checker", page_icon="🔢", layout="wide")

# # 🔄 Reset Function
# def reset_page():
#     st.session_state["num"] = ""
#     st.rerun()

# # 🎨 Custom CSS for Styling
# st.markdown(
#     """
#     <style>
#         /* Gradient Heading */
#         .gradient-text {
#             font-size: 70px;
#             font-weight: bold;
#             text-align: center;
#             background: linear-gradient(45deg, #ff6ec4, #7873f5);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             margin-bottom: 30px;
#         }

#         /* Sidebar Title */
#         .sidebar-title {
#             font-size: 35px;
#             font-weight: bold;
#             background: linear-gradient(45deg, #ff6ec4, #7873f5);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             margin-bottom: 10px;
#         }

#         /* Sidebar Instructions */
#         .sidebar-instructions {
#             font-size: 22px;
#             line-height: 1.6;
#             color: white;
#             margin-bottom: 15px;
#         }

#         /* Input Box Styling */
#         input {
#             font-size: 20px !important;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # 🎨 Gradient Title
# st.markdown('<p class="gradient-text">🔢 Even or Odd Checker</p>', unsafe_allow_html=True)

# # 🎯 Sidebar
# with st.sidebar:
#     st.markdown('<p class="sidebar-title">📌 Instructions</p>', unsafe_allow_html=True)
#     st.markdown('<p class="sidebar-instructions">1️⃣ Enter a number in the input box.</p>', unsafe_allow_html=True)
#     st.markdown('<p class="sidebar-instructions">2️⃣ Click the "Check" button.</p>', unsafe_allow_html=True)
#     st.markdown('<p class="sidebar-instructions">3️⃣ See if it\'s Even or Odd.</p>', unsafe_allow_html=True)

# # 📝 User Input
# num = st.text_input("Enter a number:", key="num")

# # ✅ Check Number Button
# if st.button("Check 🔍"):
#     try:
#         number = int(num)
#         if number % 2 == 0:
#             st.success(f"✅ {number} is an Even number! 🎉")
#         else:
#             st.warning(f"⚠️ {number} is an Odd number! 🔥")
#     except ValueError:
#         st.error("❌ Please enter a valid number!")

# # 🔄 Reset Option (Moved to Bottom)
# st.markdown('<p class="sidebar-title">🔄 Want to Try Again?</p>', unsafe_allow_html=True)
# if st.button("🔄 Reset", on_click=reset_page):
#     pass


import streamlit as st

# 🖥 Set Page Configuration
st.set_page_config(page_title="Even or Odd Checker", page_icon="🔢", layout="wide")

# 🔄 Reset Function (Fixed)
def reset_page():
    st.session_state.clear()  # Clear all stored session values
    st.rerun()  # Proper way to refresh Streamlit UI in new versions

# 🎨 Custom CSS for Styling (Fixed Title Size)
st.markdown(
    """
    <style>
        /* Gradient Heading */
        .gradient-text {
            font-size: 40px !important;
            font-weight: bold;
            text-align: center;
            background: linear-gradient(45deg, #ff6ec4, #7873f5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 30px;
        }

        /* Sidebar Title */
        .sidebar-title {
            font-size: 40px !important;
            font-weight: bold;
            text-align: center;
            background: linear-gradient(45deg, #ff6ec4, #7873f5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }

        /* Sidebar Instructions */
        .sidebar-instructions {
            font-size: 22px;
            line-height: 1.6;
            color: white;
            margin-bottom: 15px;
        }

        /* Input Box Styling */
        input {
            font-size: 20px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎨 Gradient Title (Fixed Bigger Size)
st.markdown('<h1 class="gradient-text">🔢 Even or Odd Checker</h1>', unsafe_allow_html=True)

# 🎯 Sidebar
with st.sidebar:
    st.markdown('<p class="sidebar-title">📌 Instructions</p>', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-instructions">1️⃣ Enter a number in the input box.</p>', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-instructions">2️⃣ Click the "Check" button.</p>', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-instructions">3️⃣ See if it\'s Even or Odd.</p>', unsafe_allow_html=True)

# 📝 User Input
num = st.text_input("Enter a number:", key="num")

# ✅ Check Number Button
if st.button("Check 🔍"):
    try:
        number = int(num)
        if number % 2 == 0:
            st.success(f"✅ {number} is an Even number! 🎉")
        else:
            st.warning(f"⚠️ {number} is an Odd number! 🔥")
    except ValueError:
        st.error("❌ Please enter a valid number!")

# 🔄 Reset Option (Fixed)
st.markdown('<p class="sidebar-title">🔄 Want to Try Again?</p>', unsafe_allow_html=True)
if st.button("🔄 Reset"):
    reset_page()
st.rerun()
