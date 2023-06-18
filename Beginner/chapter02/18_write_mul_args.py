import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=("col_no %d" % i for i in range(10))
)

st.write("Here is our data", df, "Data is in dataframe format. \n", "\nWrite is Super function")
