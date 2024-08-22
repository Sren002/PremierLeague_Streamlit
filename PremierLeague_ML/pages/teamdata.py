import streamlit as st 
import pandas as pd
from PIL import Image
import requests
from io import BytesIO
import matplotlib as plt


# Loading Image using PIL
url = 'https://github.com/Sren002/PremierLeague_Streamlit/blob/main/PremierLeague_ML/resources/premier_league_logo.png?raw=true'
response = requests.get(url)
im = Image.open(BytesIO(response.content))

df = pd.read_csv("https://raw.githubusercontent.com/Sren002/web-scraping-PremierLeagueML/main/matches.csv")

dfML = pd.read_csv("https://raw.githubusercontent.com/Sren002/web-scraping-PremierLeagueML/main/predictions.csv")

team = st.session_state["team"]

# configue page
st.set_page_config(
    page_title=("%s Data Analysis" % team),
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

st.sidebar.page_link('streamlit_app.py', label='Home')
st.sidebar.page_link('pages/teams.py', label='Teams')



data = df.loc[df['Team'] == "%s" % (team)]

for i in range(2024, 2020, -1):
    date = data.loc[(data["Date"].astype(str).str[:4]) == str(i)]
    
    wins = date.loc[date["Result"] == "W"]
    draws = date.loc[date["Result"] == "D"]
    losses = date.loc[date["Result"] == "L"]

    winsNum = len(wins.index)
    drawsNum = len(draws.index)
    lossesNum = len(losses.index)
    total = winsNum + drawsNum + lossesNum

    st.title("%s" % str(i))


