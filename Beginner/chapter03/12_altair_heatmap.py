import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_csv("./chapter03/albany.csv")

heat_map = alt.Chart(df).mark_rect().encode(
    alt.Y("AveragePrice:Q"),
    alt.X("Large Bags:Q"),
    alt.Color("AveragePrice:Q"),
    tooltip=["AveragePrice", "type", "Large Bags", "Date"]
).interactive()

st.altair_chart(heat_map)
