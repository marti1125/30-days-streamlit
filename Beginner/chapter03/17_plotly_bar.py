import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("./chapter03/albany.csv")

albany_df = df[df["region"] == "Albany"]
al_df = albany_df[albany_df["year"] == 2015]

st.header("Line Chart")

bar_chart = px.bar(
    al_df,
    title="Bar Chart",
    x="Date",
    y="Large Bags",
)

st.plotly_chart(bar_chart)
