import streamlit as st
import pandas as pd
from PIL import Image
import requests
from io import BytesIO

# Loading Image using PIL
url = 'https://github.com/Sren002/PremierLeague_Streamlit/blob/main/PremierLeague_ML/resources/premier_league.jpg?raw=true'
response = requests.get(url)
im = Image.open(BytesIO(response.content))

# configue page
st.set_page_config(
    page_title='English Premier League Predictions',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    page_icon = im)


st.logo(im)
st.html("""
  <style>
    [alt=Logo] {
      height: 6rem;
    }
  </style>
        """)

st.title("English Premier League Predictions")

# load dataset
df = pd.read_csv("https://raw.githubusercontent.com/Sren002/web-scraping-PremierLeagueML/main/predictions.csv")

st.write(df)

st.sidebar.page_link('streamlit_app.py', label='Home')
st.sidebar.page_link('pages/teams.py', label='Teams')
