import streamlit as st

st.header="Layout Elements"

st.subheader("Side bar")
choice = st.sidebar.radio(
    label="Choose the option",
    options=("audio", "video")
)

if choice == "audio":
    st.audio("./audio.mp3")
    st.write("This is audio")
elif choice == "video":
    st.video("./video.mp4")
    st.write("This is video") 

st.subheader("Columns")
col1, col2 = st.columns(2, gap="small")
col1.audio("./audio.mp3")
col2.video("./video.mp4")

st.subheader("Tabs")
tab1, tab2 = st.tabs(["audio", "video"])
tab1.audio("./audio.mp3")
tab2.video("./video.mp4")

st.subheader("Expend")
exp = st.expander("See Pic")
exp.write("Video and Image")
exp.image("./cat.jpg", width=400)

st.subheader("Container")
container = st.container()
container.write("One")
st.write("Two")
container.write("Three")