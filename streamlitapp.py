import streamlit as st
import pandas as pd
import numpy as np
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    # initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
st.title("Stock Dashboard")

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(header=1, usecols = [0,1,2,3,6,7,8,9,10,11,12,13], index_col=["Date", "종목"])

with st.expander("google sheet trading log"):
    st.dataframe(df)

with st.expander("balance"):
    st.dataframe(df)

