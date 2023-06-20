import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

df = pd.read_csv("./chapter03/albany.csv")

albany_df = df[df["region"] == "Albany"]
al_df = albany_df[albany_df["year"] == 2015]

fig = make_subplots(rows=3, cols=1)

fig.add_trace(
    go.Scatter(
        x=al_df["Date"],
        y=al_df["Total Bags"],
    ), row=1, col=1
)

fig.add_trace(
    go.Scatter(
        x=al_df["Date"],
        y=al_df["Small Bags"],
    ), row=2, col=1
)

fig.add_trace(
    go.Scatter(
        x=al_df["Date"],
        y=al_df["Large Bags"],
    ), row=3, col=1
)

st.header("Line Chart")

st.plotly_chart(fig)
