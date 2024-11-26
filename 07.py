import streamlit as st
import pandas as pd
import numpy as np

# Membuat DataFrame dengan data acak
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y']
)

# Menampilkan line chart
st.line_chart(df)

# Menampilkan bar chart
st.bar_chart(df)

# Menampilkan area chart
st.area_chart(df)
