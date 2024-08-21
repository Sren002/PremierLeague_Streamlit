import streamlit as st
import pandas as pd

# configue page
st.set_page_config(
    page_title='English Premier League Predictions',
    layout = 'wide',
    initial_sidebar_state = 'expanded')


st.title("English Premier League Predictions")

# load dataset
df = pd.read_csv("https://raw.githubusercontent.com/Sren002/web-scraping-PremierLeagueML/main/predictions.csv")

st.write(df)

st.sidebar.page_link('streamlit_app.py', label='Home')
st.sidebar.page_link('pages/teams.py', label='Teams')
