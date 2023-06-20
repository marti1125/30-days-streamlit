import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_csv("./chapter03/albany.csv")

box_plot = alt.Chart(df).mark_boxplot().encode(
    x="Date",
    y="Large Bags"
)

st.altair_chart(box_plot)
