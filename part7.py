import streamlit as st
from PIL import Image
import cv2

st.header("Media Elements")

st.subheader("Image Preview")
img = Image.open("./cat.jpg")
# img = cv2.imread("./cat.jpg")
st.image(
    img,
    caption="Huh Cat Meme ",
    width=800,
    channels="RGB"
)

st.subheader("Audio Preview")
st.audio(
    data="./audio.mp3",
    start_time=10
)

st.subheader("Video Preview")
st.video(
    data="video.mp4",
)