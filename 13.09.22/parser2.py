import streamlit as st
import json

# data = json.load("doctors.json")

# st.table(st.json(data))


df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.table(df)