import streamlit as st
import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randn(30, 10), columns=('col_no %d' % i for i in range(10)))

st.dataframe(df.style.highlight_min(axis=0))
st.table(df.style.highlight_min(axis=0, color="red"))
