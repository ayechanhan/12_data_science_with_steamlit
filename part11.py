import streamlit as st
import pandas as pd
import numpy as np
import time

st.header("Mutation")

st.subheader("Add Rows")
df = pd.DataFrame(np.random.randn(10, 2), columns=["col1", "col2"])
my_table = st.table(df)

df2 = pd.DataFrame(
    np.random.randn(1, 2), columns=["col1", "col2"]
)
my_table.add_rows(df2)

st.subheader("Add Charts")
chart = st.line_chart(df)
chart.add_rows(df2)

chart = st.line_chart(df)
for i in range(50):
    time.sleep(1)
    df2 = pd.DataFrame(
        np.random.randn(1,2),
        columns = ["col1", "col2"]
    )
    chart.add_rows(df2)
