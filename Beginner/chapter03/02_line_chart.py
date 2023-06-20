import streamlit as st
import pandas as pd
import numpy as np

st.title("Area")

df = pd.DataFrame(
    np.random.randn(80, 4),
    columns=["C1", "C2", "C3", "C4"]
)

st.line_chart(df)
