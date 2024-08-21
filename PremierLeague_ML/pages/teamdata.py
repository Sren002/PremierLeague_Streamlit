import streamlit as st 
import pandas as pd

st.sidebar.page_link('streamlit_app.py', label='Home')
st.sidebar.page_link('pages/teams.py', label='Teams')

df = pd.read_csv("https://raw.githubusercontent.com/Sren002/web-scraping-PremierLeagueML/main/matches.csv")

dfML = pd.read_csv("https://raw.githubusercontent.com/Sren002/web-scraping-PremierLeagueML/main/predictions.csv")

st.write(st.session_state["team"])