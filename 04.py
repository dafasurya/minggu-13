import streamlit as st

st.checkbox("yes")
st.button("Click")
st.write("Pick your gender")
gender = st.radio("", ["Male", "Female"], index=0)
st.write("Pick your gender")
gender_dropdown = st.selectbox(" ", ["Male", "Female"])
st.write("choose a planet")
planet = st.selectbox("Choose an option", ["Mercury", "Venus", "Earth", "Mars", "Jupiter"])
st.write("Pick a mark")
mark = st.slider(" ", 0, 100, 50)
st.write("Bad", " " * 20, "Good", " " * 20, "Excellent")
st.write("Pick a number")
number = st.slider(" ", 0, 50, 9)