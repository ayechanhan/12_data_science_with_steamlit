import streamlit as st;
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt

st.text("This is a text.")

st.write("This is **just** a **_test_** ")

df = pd.read_csv("./addresses.csv")
dic = {"a": 10, "b": 11, "c": 12}
fig, ax = plt.subplots()
ax.scatter(np.arange(5), np.arange(5) ** 2)
# st.title("This is the title")
# st.header("Header")
# st.subheader("Sub")

code = '''
    def func():
        print(np.arange(10))
'''
st.code(code, language="python")
