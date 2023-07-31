import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import folium

df = pd.read_csv("dummy data.csv")

# 地図の中心を設定（最初の地点を中心に表示）
center_lat, center_lon = df["latitude"].iloc[0], df["longitude"].iloc[0]


st.title('駅どこ執事(仮)')
st.write("### 安心して住める街をあなたに")


station = st.sidebar.selectbox(label="仕事の最寄り駅を入力してください",
                               options=df[df["category"] == "station"]["name"])
st.sidebar.number_input("検索したい駅までの時間を入力してください", 0, 120, 0)
submit = st.sidebar.button("検索")

# データを地図に渡す関数を作成する


def AreaMarker(df, m):
    for index, r in df.iterrows():

        # ピンをおく
        folium.Marker(
            location=[r.latitude, r.longitude],
            popup=r["name"],  # rは非整数なのでilocを用いたデータの特定はできない
        ).add_to(m)


# おすすめを表示
if submit == True:
    st.write("おすすめのカフェ")
    st.write(df.loc[df['category'] == 'cafe', 'name'])

# 地図を表示
if submit == True:
    m = folium.Map(location=[center_lat, center_lon], zoom_start=14)
    AreaMarker(df, m)  # データを地図渡す
    folium_static(m)  # 地図情報を表示
