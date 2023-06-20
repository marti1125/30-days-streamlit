import streamlit as st

st.title("Graphviz")

st.graphviz_chart(
    """
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Result Forecasting"
        "New Data" -> "Model"
    }
    """
)