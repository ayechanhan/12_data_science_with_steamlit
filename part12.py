import streamlit as st

st.header("Session State")

st.subheader("Initialize Session")
st.session_state
if "key" not in st.session_state:
    st.session_state["key"] = 1

st.subheader("Change Session Value")
if "key" in st.session_state:
    st.session_state = 2
st.session_state

st.subheader("Delete Session")
st.session_state
if "key" in st.session_state:
    del st.session_state["key"]
st.session_state

st.subheader("Bulk Delete Session")
for k in st.session_state.keys():
    del st.session_state[k]
st.session_state

st.subheader("Input widget key")
st.session_state
st.text_input("Name", key="name")
st.session_state

st.subheader("Callback")
def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key="my_form"):
    slider_input = st.slider("My Slider", 0, 15, 5, key="my_slider")
    check_box = st.checkbox("Yes or No", key="my_checkbox")
    submit_btn = st.form_submit_button(on_click=form_callback)