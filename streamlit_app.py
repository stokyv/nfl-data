import streamlit as st
import pandas as pd
import numpy as np
import nfl

st.markdown("# Main page 1🎈")
st.sidebar.markdown("# Main page 🎈")

st.title("NFL DATA ANALYSIS")
st.write("A simple app to download NFL data and apply data analysis.")

def load_data(year):
    filepath = f'data\play_by_play_2022.csv.gz'
    data = pd.read_csv(filepath, compression='gzip', low_memory=False)                
    return data

df = load_data(2022)
# df


option = st.selectbox(
    'Select a team',
     df['home_team'].unique())

'You selected: ', option

df[df.home_team==option]


