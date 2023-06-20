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
    y="Date",
    x="Large Bags",
    color="Large Bags",
    orientation="h",
)

st.plotly_chart(bar_chart)
