#おまじない
import streamlit as st
import numpy as np
import pandas as pd
import folium
from streamlit_folium import folium_static

#title周り
st.title('駅どこ執事')
st.write('駅どこ執事は、あなたの「安らぎのある街探し」をお手伝いする駅周辺情報の検索サービスです')

#ダミーデータの読み込みと表示
#df = pd.read_csv('230726_station_test.csv')
#st.map(df)

#すずちゃんカフェデータの読み込み
df1 = pd.read_csv('cafe_test.csv')
st.dataframe(df1)
st.map(df1)


#foliumで地図にピン立てる
def AreaMarker(df1,m):
    for index, r in df1.iterrows(): 

        # ピンをおく
        folium.Marker(
            location=[r.lat, r.lon],
            popup=index,
        ).add_to(m)

        # 円を重ねる→今回不要
        # folium.Circle(
        #     radius=rad*10,
        #     location=[r.lat, r.lon],
        #     popup=index,
        #     color="yellow",
        #     fill=True,
        #     fill_opacity=0.07
        # ).add_to(m)

# タイトル
st.title("サンプル地図")
# スライダーをつける→今回不要
# rad = st.slider('拠点を中心とした円の半径（km）',
                # value=1,min_value=1, max_value=2)
                
# 半径の距離を表示→今回不要              
# st.subheader("各拠点からの距離{:,}km".format(rad))

# 地図の初期設定
m = folium.Map(location=[34.6924107,135.5016849], zoom_start=10)

# データを地図渡す
AreaMarker(df1,m) 

 # 地図情報を表示
folium_static(m)

