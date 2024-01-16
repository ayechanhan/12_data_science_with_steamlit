import streamlit as st
import time

st.header("Status Elements")

st.subheader("Progress")
txt = "% completed"
progress_bar = st.progress(0, text=txt)
for pr in range(100):
    time.sleep(0.1)
    progress_bar.progress(pr+1, text=txt)

st.subheader("Spinner")
with st.spinner("wait for it...."):
    time.sleep(5)
st.write("Completed")

st.subheader("Balloons")
st.balloons()

st.subheader("Snow")
st.snow()

st.subheader("Error")
st.error("This is sample error message")

st.subheader("Warning")
st.warning("This is sample warning message")

st.subheader("Info")
st.info("This is sample information message")

st.subheader("Success")
st.success("This is sample success message")

st.subheader("Exception")
e = RuntimeError("Exp")
st.exception(e)