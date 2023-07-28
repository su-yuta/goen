import pandas as pd
import streamlit as st
from streamlit_folium import st_folium
import folium

df = pd.read_csv("dummy data.csv")

# 地図の中心を設定（最初の地点を中心に表示）
center_lat, center_lon = df["latitude"].iloc[0], df["longitude"].iloc[0]


st.title('駅どこ執事(仮)')
st.write("### 安心して住める街をあなたに")


station = st.sidebar.text_input("仕事の最寄り駅を入力してください", "駅名")
st.sidebar.number_input("検索したい駅までの時間を入力してください", 0, 120, 0)
submit = st.sidebar.button("検索")

# おすすめを表示
if submit == True:
    st.write("おすすめのカフェ")
    st.write(df.loc[df['category'] == 'cafe', 'name'])

# 地図を表示
if submit == True:
    st.map(df)
