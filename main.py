import streamlit as st
import pandas as pd
import numpy as np

st.write('hello world')

x = st.text_input("favorite Movie?")
st.write(f"your favorite movie is: {x}")

isClicked = st.button('click me!')
st.write('## This is an h2 :)')

data = pd.read_csv("netflix_titles.csv")
st.write(data)
chartData = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["America", "Barbados", "Canada"]
)

st.bar_chart(chartData)
st.line_chart(chartData)
