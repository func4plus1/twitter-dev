import streamlit as st
import pandas as pd
import twint 

st.markdown('Twitter Sentiment')

query = st.text_input('Search','Happiness')

c = twint.Config()

c.Limit = 1000
c.Search = query 
c.Pandas = True

twint.run.Search(c)

Tweets_df = twint.storage.panda.Tweets_df
