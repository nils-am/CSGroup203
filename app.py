import streamlit as st

for color in ("red", "orange", "green", "blue", "purple"):
	st.markdown(f"<span style='color: {color}'>Hello, world!</span>", unsafe_allow_html=True)
