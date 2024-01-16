import streamlit as st
import datetime

# Page Config
st.set_page_config(
    page_title="New APP",
    layout="wide"
)

st.header("Stop, Form, Page Config, Echo and Help")

st.subheader("Stop")
email = st.text_input(
    label="Enter your email"
)
if not email:
    st.warning("Please enter your email!!")
    st.stop()
st.success("Go Ahead")

st.subheader("Form")
form = st.form("Basic Form")
name = form.text_input("Name")
age = form.number_input("Age", min_value=18)
birthday = form.date_input("Birthday")
submitted = form.form_submit_button("Submit")
if submitted:
    st.write(name, age, birthday)

st.subheader("Echo")
def addition(a, b):
    return a+b
with st.echo():
    def multiple(a, b):
        return a*b
    a = 10
    b = 20
    sum = addition(a,b)
    multi = multiple(a,b)
    st.write(sum, multi)

st.subheader("Help")
st.help(datetime.time)