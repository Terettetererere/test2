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

fruit = st.radio(label="好きなフルーツは？",options =["バナナ","りんご","いちご"],index=1)
st.write(fruit)

def f(i):
    play = ('なわとび', '野球', 'ゲーム')
    return play[i]
option = st.selectbox('今日はなにする?', (0,1,2), format_func= f )
st.write('よし ', option, " をしよう！")

options = st.multiselect('何色が好き？',options= ['Green', 'Yellow', 'Red', 'Blue'], default=['Yellow', 'Red'])
st.write('You selected:', options)

age = st.slider('何歳?', min_value=0, max_value=130, value=25)
st.write(age)

from datetime import datetime, date, time
interval = st.slider("計画期間は?", value=(datetime(2019, 1, 1, 9, 30),
datetime(2020, 1, 1, 9, 30)),format="MM/DD/YY - hh:mm")

color = st.select_slider('色を選んでね',options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])

title = st.text_input('お名前は？', value='ななしのごんべえ')

number = st.number_input('数字を入れてね', min_value=1.0, max_value=10.0, value=5.0, step=0.1)

d = st.date_input("誕生日は？",date(2019, 7, 6))

alarm = st.time_input('アラームセット', time(8, 45))

uploaded_file = st.file_uploader("ファイル選択")

add_selectbox = st.sidebar.selectbox("連絡方法は?", ("Email", "Home phone", "Mobile phone"))

with st.form(key='basic_form'):
    n_job = st.number_input("最大ジョブ数", min_value =1, max_value =10000, value= 100)
    n_shipment = st.number_input("最大輸送数", min_value =1, max_value =10000, value= 100)
    submit = st.form_submit_button(label='データ更新')

if submit:
    st.write(n_job, n_shipment)
