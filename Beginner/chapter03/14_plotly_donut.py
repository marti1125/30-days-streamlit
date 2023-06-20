import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("./chapter03/avocado.csv")

st.header("Donut Chart")

donut_chart = px.pie(
    names=df.type,
    values=df.AveragePrice,
    hole=0.5,
)

st.plotly_chart(donut_chart)
