import streamlit as st;
import numpy as np;
import pandas as pd;
import json;

st.header("Part 2")
st.subheader("DataFrame")
df = pd.DataFrame(np.random.randn(50, 20), columns = ["cols" + str(i) for i in range(20)])
st.subheader("DataFrame with Width and Height customization")
st.dataframe(df, height=200, width=1000)
st.subheader("Handling dataframe in Table")
st.table(df)
st.subheader("Metric with up and down")
st.metric("MMK", value="2100.20", delta="19.10", delta_color="inverse")
st.subheader("Json data with expand option")
f = open("./part2.json")
dt = json.load(f)
st.json(dt, expanded=False)
