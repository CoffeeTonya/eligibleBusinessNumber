import streamlit as st
import numpy as np
import pandas as pd
import os
import csv
import sys
from glob import glob

filepaths = ['upload_1.csv', 'upload_2.csv', 'upload_3.csv', 'upload_4.csv', 'upload_5.csv', 'upload_6.csv', 'upload_7.csv', 'upload_8.csv']

# filepaths = []
# for i in range(1, 14):
#     filepath = 'upload_' + str(i) + '.csv'
#     filepaths.append(filepath)

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
        names=[
        '一連番号', '登録番号', '事業者処理区分', '訂正区分', '人格区分',
        '国内外区分', '最新履歴', '登録年月日', '更新年月日', '取消年月日',
        '失効年月日', '所在地(法人)', '都道府県コード(法人)', '市区町村コード(法人)', '所在地(公表申出)',
        '都道府県コード(公表申出)', '市区町村コード(公表申出)', '日本語(カナ)', '氏名又は名称',
        '国内において資産の譲渡に係る所在地', '国内において資産の譲渡に係る都道府県コード',
        '国内において資産の譲渡に係る市区町村コード', '主たる屋号', '通称・旧姓'
            ]
    ))
    _df = pd.concat(data_list, axis=0).reset_index()
    _df = _df[['登録番号', '氏名又は名称', '所在地(法人)', '登録年月日']]
    _df = _df.replace(np.nan, '', regex=True)
    df = _df[_df['所在地(法人)'].str.contains(companyAddress, na=False)]
    df = df[df['氏名又は名称'].str.contains(companyName, na=False)]
    st.table(df[df['登録番号'].str.contains(companyNumber, na=False)])


# import streamlit as st
# from streamlit import session_state as _state

# state = _get_state()

# if state.count == None:
#     state.count = 0


# def main():
#     st.title('Counter App')

#     increment_count = st.button('count +')
#     decrement_count = st.button('count -')
#     if increment_count:
#         state.count += 1
#     if decrement_count:
#         state.count -= 1

#     st.write(f'count: {state.count}')


# if __name__ == '__main__':
#     main()