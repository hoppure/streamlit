import streamlit as st
import pandas as pd
import numpy as np
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(header=1, use_col = [1,2,3,4,5,6,7,])

with st.expander("google sheet trading log")
    st.write(df)


# page = []

st.title("Stock Dashboard")


