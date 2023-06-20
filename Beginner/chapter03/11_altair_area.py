import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_csv("./chapter03/albany.csv")

area = alt.Chart(df).mark_area(color="orange").encode(
    x="Date",
    y="Large Bags"
)

st.altair_chart(area)
