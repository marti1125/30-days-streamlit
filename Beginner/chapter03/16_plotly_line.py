import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("./chapter03/albany.csv")

albany_df = df[df["region"] == "Albany"]
al_df = albany_df[albany_df["year"] == 2015]

st.header("Line Chart")

line_chart = px.line(
    x=al_df["Date"],
    y=al_df["Large Bags"],
)
line_chart.update_traces(line_color="orange")

st.plotly_chart(line_chart)
