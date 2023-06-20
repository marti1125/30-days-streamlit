import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("./chapter03/avocado.csv")

st.header("Scatter Chart")

scat = px.scatter(
    x=df.Date,
    y=df.AveragePrice,
)

st.plotly_chart(scat)
