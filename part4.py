import streamlit as st
import pandas as pd
import numpy as np
import time

st.header("Widgets - 1(Button, Download Button, Checkbox, Radio, Selectbox)")

st.subheader("Button")
btn = st.button("Click Me!!")
if btn:
    st.text("You've clicked the button!!!")

st.subheader("Download CSV Button")
df = pd.DataFrame(np.random.randn(10, 2), columns=["col1", "col2"])
data = df.to_csv().encode("utf-8")
st.download_button(
    label="Download CSV File",
    data = data,
    file_name="file.csv",
    mime="text/csv"
)

st.subheader("Download Text File")
st.download_button(
    label="Download Text File",
    data = "Hello World!!"
)

st.subheader("Download Image")
file = open("./cat.jpg", "rb")
st.download_button(
    label="Download Image",
    data = file,
    file_name="huh.jpg",
    mime="image/jpg"
)

st.subheader("Checkbox")
cb = st.checkbox("I agree")
if cb:
    st.write("Agreement Done!")

st.subheader("Options")
option = st.radio("Order your food", options=("Pizza", "Burger", "Pasta"), index=1)
if option == "Pizza":
    st.text("You ordered Pizza")
elif option == "Burger":
    st.text("You ordered Burger")
elif option == "Pasta":
    st.text("You ordered Pasta")

st.subheader("Select Box")
selectbox = st.selectbox(
    label = "Where do you live?",
    options = ("Singapore", "Japan")
)
if selectbox == "Singapore":
    st.text("You live in Singapore")
elif selectbox == "Japan":
    st.text("You live in Japan")