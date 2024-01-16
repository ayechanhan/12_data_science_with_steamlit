import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.header("Line Charts, Bar Charts, Pyplot and Map")

df = pd.DataFrame(np.random.rand(10, 2), columns=['prices', 'difference'])

st.subheader("Line Chart")
st.line_chart(df)
# st.line_chart(df, y=['difference'])

st.subheader("Area Chart")
st.area_chart(df)

st.subheader("Bar Chart")
st.bar_chart(df)

st.subheader("Matplotlib Scatter")
fig, ax = plt.subplots()
ax.scatter(np.arange(10), np.arange(10)**2)
st.pyplot(fig)

st.subheader("Histogram")
fig, ax = plt.subplots()
ax.hist(np.random.rand(100), bins=10)
st.pyplot(fig)

st.subheader("Map(Singapore, Japan)")
places = pd.DataFrame({
    "lat": [1.3322362607584395, 35.53109618044182],
    "lon": [103.82093332294794, 139.7571891440467]
})
st.map(places)