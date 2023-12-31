import streamlit as st
import pickle
import pandas as pd
import numpy as np
import xgboost
from xgboost import XGBRegressor

pipe = pickle.load(open('pipe.pkl','rb'))

teams = ['Australia',
 'India',
 'Bangladesh',
 'New Zealand',
 'South Africa',
 'England',
 'West Indies',
 'Afghanistan',
 'Pakistan',
 'Sri Lanka']

cities = ['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'Cape Town',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Manchester',
 'Abu Dhabi',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Cardiff',
 'Christchurch',
 'Trinidad']

st.title('T20 Cricket Score Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Batting Team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Bowling Team', sorted(teams))


# city = st.selectbox('City', sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('No. of Overs Done (>5)')
with col5:
    wickets = st.number_input('Wickets out')

last_five = st.number_input('Runs Scored in last 5 Overs')

if st.button('Predict Score'):
    balls_left = 120 - (overs*6)
    wickets_left = 10 - wickets
    crr = current_score/overs

    input_df = pd.DataFrame(
     {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'current_score': [current_score],'balls_left': [balls_left], 'wicket_left': [wickets_left], 'crr': [crr], 'last_five': [last_five]})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))
    st.header(input_df)
    



