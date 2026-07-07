import streamlit as st
st.title("MultiPage Streamlit app")
st.write("Choose the right application from below to use it for free")

st.set_page_config(page_title="Assistant AI", layout="centered")
st.title("Assistant AI")


st.page_link("Pages/breast_cancer.py", label="Breast Cancer")
st.page_link("Pages/page2.py", label="Page 2")