import streamlit as st
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("./chapter03/avocado.csv")

st.header("Pie Chart")

pie_chart = go.Figure(
    go.Pie(
        labels=df.type,
        values=df.AveragePrice,
        hoverinfo="label+percent",
        textinfo="value+percent"
    )
)

st.plotly_chart(pie_chart)
