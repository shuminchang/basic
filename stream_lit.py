import streamlit as st
import json
import requests

st.title("Basic")

option = st.selectbox("What", ("A", "B", "C", "D"))

st.write("")
st.write("select")
x = st.slider("X", 0, 100, 20)
y = st.slider("Y", 0, 100, 20)

inputs = {"operaion": option, "x": x, "y": y}

if st.button("Calculate"):
    res = requests.post(url = "http://127.0.0.1:8000/calculate", data = json.dumps(inputs))
    st.subheader(f"response = {res.text}")