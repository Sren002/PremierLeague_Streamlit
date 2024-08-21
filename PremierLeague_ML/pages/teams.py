import streamlit as st
import pandas as pd
import math

df = pd.read_csv("https://raw.githubusercontent.com/Sren002/web-scraping-PremierLeagueML/main/matches.csv")


st.sidebar.page_link('streamlit_app.py', label='Home')
st.sidebar.page_link('pages/teams.py', label='Teams')


teams = df["Team"].unique()

# make sure if there is an uneven # of teams one isnt cut out by 
# using floor and ceiling
team1 = teams[:math.ceil(len(teams)/2)]
team2 = teams[math.floor(len(teams)/2):]

left, right = st.columns(2)   
with left:   
    # add element on the left side  
    for team in team1: 
        button = st.button(team)
        if button:
            st.session_state["team"] = team
            st.switch_page("pages/teamdata.py")
with right:     
    # add element on the right side
    for team in team2: 
        button = st.button(team)
        if button:
            st.session_state["team"] = team
            st.switch_page("pages/teamdata.py")

#st.radio('Teams', options=teams, 
#          horizontal=True)