import streamlit as st
import numpy as np
import pandas as pd
import os
import csv
import sys
from glob import glob

# filepaths = ['upload_1.csv', 'upload_2.csv', 'upload_3.csv', 'upload_4.csv', 'upload_5.csv', 'upload_6.csv', 'upload_7.csv', 'upload_8.csv', 'upload_9.csv', 'upload_10.csv']

filepaths = []
for i in range(1, 11):
    filepath = 'upload_' + str(i) + '.csv'
    filepaths.append(filepath)

st.set_page_config(
    page_title = "適格事業者番号検索", 
    layout = 'wide', 
    )

companyName = st.sidebar.text_input('事業者名', '')
companyAddress = st.sidebar.text_input('住所', '')
companyNumber = st.sidebar.text_input('登録番号', '')

data_list = []

st.title('適格事業者番号検索')
st.subheader('データ更新日:2023/04/11')
if st.sidebar.button('検索する'):
    for file in filepaths:
        data_list.append(pd.read_csv(
        file,
        header=None,
        names=['登録番号', '氏名又は名称', '所在地(法人)', '登録年月日']
    ))
        
    _df = pd.concat(data_list, axis=0)
    _df = _df.replace(np.nan, '', regex=True)
    df = _df[_df['所在地(法人)'].str.contains(companyAddress, na=False)]
    df = df[df['氏名又は名称'].str.contains(companyName, na=False)]
    st.table(df[df['登録番号'].str.contains(companyNumber, na=False)])