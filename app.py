from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
import io

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

# Add Title
st.title("📊 EDA Your Data 📈")
st.subheader("A simple EDA WEbUI with Pygwalker in Streamlit")

# You should cache your pygwalker renderer, if you don't want your memory to explode
@st.cache_resource
def get_pyg_renderer(csv_file) -> "StreamlitRenderer":
    df = pd.read_csv(csv_file)
    # If you want to use feature of saving chart config, set `spec_io_mode="rw"`
    return StreamlitRenderer(df, spec="./data/gw_config.json", spec_io_mode="rw")


# Input section
csv_file = st.file_uploader("Upload CSV file", type="csv")

# Submit button
if st.button("Submit"):
    if csv_file is not None:
        renderer = get_pyg_renderer(csv_file)
        renderer.explorer()
    else:
        st.warning("Please upload a CSV file.")