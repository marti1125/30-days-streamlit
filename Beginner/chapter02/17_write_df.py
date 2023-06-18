import streamlit as st
import pandas as pd

st.write(pd.DataFrame(
    {
        "column one": [5.436, 6.372, 3.645, 4.554, 7.26],
        "column two": [99, 55, 75, 41, 37]
    }
))
