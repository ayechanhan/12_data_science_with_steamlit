import streamlit as st
import datetime
from PIL import Image
import numpy as np
from io import StringIO

st.header("Widget 3 (Text Area, Date Input, Time Input, File Upload, Camera Input, Color Pick)")

st.subheader("Text Area")
st.text_area(
    label="Write Something",
    height=150,
    max_chars=150,
    placeholder="Write here"
)

st.subheader("Date Input")
st.date_input(
    label="Enter your birthdate",
)

st.subheader("Time Input")
st.time_input(
    label="Enter your meal time",
)

st.subheader("File Upload")
upload_file = st.file_uploader(
    label="Upload here",
)
if upload_file:
    st.write(upload_file.type)
    if "image" in upload_file.type:
        img = Image.open(upload_file)
        st.write(np.array(img).shape)
    elif upload_file.type == "text/plain":
        stringio = StringIO(upload_file.getvalue().decode("utf-8"))
        stringdata = stringio.read()
        st.write(stringdata)

st.subheader("Camera Input")
picture = st.camera_input("Take a pic!")
if picture:
    img = Image.open(picture)
    st.write(np.array(img).shape)

st.subheader("Color Picker")
color = st.color_picker("Pick a color")
if color:
    st.write(f"You selected the color: {color}")
