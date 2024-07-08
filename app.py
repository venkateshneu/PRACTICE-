import streamlit as st

st.title("Hello, Streamlit!")
st.write("Welcome to my app.")
value = st.slider("Pick a number", 0, 100)
st.write("You picked:", value)
