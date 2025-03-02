import streamlit as st
import inhalation_calculations
import pandas as pd

st.set_page_config(
    page_title="Deplastico Microplastics calculator",
    page_icon=":desktop_computer:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.sidebar.header("Welcome")

#st.sidebar.image("logo.png")

st.sidebar.title("FAQ")

st.sidebar.title("Sources")

# ------------------ Main App UI ------------------ #

st.title("""
Complete the fields below to calculate your estimated microplastic exposure
""")
st.markdown("""---""")

# Two column layout for the main app content
col1, col2 = st.columns([1, 1])

# Create input fields for additional details
with col1:
    st.header("Demographic information")
    sex = st.selectbox(
        label="Select your sex",
        options=[
            "Male",
            "Female"
        ],
        key="sex",
    )

    age = st.text_input(
        label="Enter your age",
        key="age",
        value=30
    )

    zip_code = st.text_input(
        label="Enter your zip code",
        max_chars=5,
        value=10011,
        key="zip_code",
    )
    st.header("Enviromental information")
    home_hours = st.slider(
        "How many hours a day do you typically spend at home?",
        min_value=0,
        max_value=24,
        value=12,
        key="home_hours",
    )

    office_hours = st.slider(
        "How many hours a day do you typically spend at in an office?",
        min_value=0,
        max_value=24,
        value=8,
        key="office_hours",
    )

    outdoor_hours = st.slider(
        "How many hours a day do you typically spend at in an outdoor environment?",
        min_value=0,
        max_value=24,
        value=4,
        key="outdoor_hours",
    )
    st.markdown("""---""")

    calculate_button = st.button(label="Calculate exposure")
    if calculate_button:
        with st.spinner("Calculating exposure..."):
            inhalation_results = inhalation_calculations.calculation_inhalation_data(zip_code,home_hours,office_hours,outdoor_hours)
            st.header("Estimated exposure")
            st.title(inhalation_results[0])
            st.caption('mnp')
            st.markdown(f"Exposure by environment in {inhalation_results[4]}, {inhalation_results[5]}")
            chart_data = pd.DataFrame({
                'Environment': ['Home', 'Office', 'Outdoor'],
                'Exposure (mnp)': [inhalation_results[1], inhalation_results[2], inhalation_results[3]]  # Example exposure values
            }
            )
            st.bar_chart(chart_data, x="Environment", y="Exposure (mnp)", color="#ADD8E6", stack=False)
            usage_log = 'usage_log.csv' 
            log_ = pd.DataFrame({
                'sex' : [sex],
                'age': [age],  
                'zip': [zip_code],
                'home' : [home_hours],
                'office' : [office_hours],
                'outdoor' : [outdoor_hours]
            }
            )
            # Append the new row to the usage log
            log_.to_csv(usage_log, mode='a', header=False, index=False)

