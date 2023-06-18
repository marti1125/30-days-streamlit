import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(np.random.randn(10, 2), columns=["a", "b"])
chart = alt.Chart(df).mark_circle().encode(x="a", y="b", tooltip=["a", "b"])

st.write(chart)
