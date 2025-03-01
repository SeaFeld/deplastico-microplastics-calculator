import streamlit as st
import inhalation_calculations

st.set_page_config(
    page_title="Deplastico Microplastics calculator",
    page_icon=":desktop_computer:",
    layout="wide",
    initial_sidebar_state="expanded",
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

st.sidebar.header("About")

#st.sidebar.image("logo.png")

st.sidebar.title("FAQ")

st.sidebar.title("Sources")

# ------------------ Main App UI ------------------ #

st.markdown("""
Complete the fields below to calculate your estimated microplastic exposure
""")
st.markdown("""---""")

# Two column layout for the main app content
col1, col2 = st.columns([1, 1])

# Create input fields for additional details
with col1:
    sex = st.selectbox(
        label="Select your sex",
        options=[
            "Male",
            "Female"
        ],
        key="sex",
    )

    age = st.number_input(
        label="Enter your age",
        min_value=0,
        max_value=110,
        key="age",
    )
# Create input fields for internet_facing and authentication
    zip_code = st.number_input(
        label="Enter your zip code",
        min_value=51,
        max_value= 999999,
        key="zip_code",
    )

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
    st.header("Estimated exposure")
    st.title(inhalation_calculations.calculation_inhalation_data(zip_code,home_hours,office_hours,outdoor_hours))
    st.caption('mnp')