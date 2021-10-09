import streamlit as st
import pandas as pd 

st.title("タイトル")
st.write("何でも書ける")
st.markdown("## マークダウンで書く $x^2$")

if st.button('Say hello'):
    st.write('こんにちわ')
else:
    st.write('Goodbye')

agree = st.checkbox('チェックしてください')
if agree:
    st.write('Great!')
