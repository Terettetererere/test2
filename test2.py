#pip install streamlit
poetry add streamlit
conda install -c conda-forge streamlit

import streamlit as st
import pandas as pd 
import plotly.express as px

st.title("タイトル")
st.write("何でも書ける")
st.markdown("## マークダウンで書く $x^2$")

df = px.data.iris()
st.write(df.head())
st.table(df.head())
st.write(px.scatter(df,x="sepal_length",y="sepal_width",color="species"))

if st.button('Say hello'):
    st.write('こんにちわ')
else:
    st.write('Goodbye')

agree = st.checkbox('チェックしてください')
if agree:
    st.write('Great!')
