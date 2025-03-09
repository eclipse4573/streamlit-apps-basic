'''
Create an interactive web app using streamlit that acts as a study companion for students.
This app will provide study schedules, multimedia learning resources.
'''

import streamlit as st
import pandas as pd

st.title('Study Companion')
# st.video('video.mp4', loop = True)
# st.audio('audio.mp3')

data = {
    'Monday': ['Maths', 'Science'],
    'Tuesday': ['English', 'History'],
    'Wednesday': ['Maths', 'French'],
    'Thursday': ['Political Science', 'Science'],
    'Friday': ['French', 'Economics']
}

df = pd.DataFrame(data)
st.table(df)
st.dataframe(df)
