import streamlit as st
from datetime import time

st.header("Widget - 2(Multiselect, slider, select_slider, text_input, number_input)")

st.subheader("Multi Select")
option = st.multiselect(
    label="Which places you have been?",
    options = ("Yangon", "Mandalay", "Taung Gyi", "Kalaw"),
    default = ("Yangon")
)

st.subheader("Slider 1")
slider = st.slider(
    label="Your age",
    min_value=18,
    max_value=90,
    value=20,
    step=1
)
st.write(slider)

st.subheader("Slider 2 with range")
slider = st.slider(
    label="Average age",
    min_value=18,
    max_value=90,
    value=(40, 60),
    step=1
)
st.write(slider)

st.subheader("Slider 3 with time range")
slider = st.slider(
    label="Meeting time",
    value= (time(11,30), time(14,30))
)
st.write(slider)

st.subheader("Slider 4 with select slider")
slider = st.select_slider(
    label="Select color",
    options=("Black", "Blue", "Red", "White")
)
st.write(slider)

st.subheader("Input box")
input = st.text_input(
    label="Please enter your email!",
    max_chars=20,
    placeholder="Email"
)
st.write(input)

st.subheader("Password Field")
pwd = st.text_input(
    label="Please enter your password!",
    max_chars=20,
    placeholder="Password",
    type="password"
)

st.subheader("Number input")
num = st.number_input(
    label="Enter your age",
    min_value=18,
    max_value=100,
    step=1
)