#おまじない
import streamlit as st
import numpy as np
import pandas as pd
import folium
from streamlit_folium import folium_static

#ダミーデータの読み込みと表示
df = pd.read_csv('230726_station_test.csv')
#st.dataframe(df)

#すずちゃんカフェデータの読み込み
df1 = pd.read_csv('cafe_test.csv')
#st.dataframe(df1)
#st.map(df1)

#0726ダミーデータの読み込み
df2 = pd.read_csv('230727_cafe2.csv')

#title周り
st.title('駅どこ執事')
st.write('あなたのお住まいの最寄り駅のおすすめを表示します！')


#サイドバー
st.sidebar.write('あなたの「安らぎのある街探し」をお手伝いする駅周辺情報の検索サービスです')
#駅を選ぶ
st.sidebar.write('（１）駅の入力')
option1 = st.sidebar.selectbox(
    '職場の最寄り駅を入力してください',
    df['name']
)
#通勤時間を選ぶ
st.sidebar.write('（２）希望の通勤時間')
option2 = st.sidebar.selectbox(
    '希望の通勤時間を入力してください',
    list(range(15,105,15))
)

if st.sidebar.button('検索！'):
    st.dataframe(df2)
           



#foliumで地図にピン立てる
def AreaMarker_station(df2,m):
    for index, r in df2.iterrows(): 

        # ピンをおく
        folium.Marker(
            location=[r.駅_緯度, r.駅_経度],
            popup='駅',
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

#foliumで地図にピン立てる
def AreaMarker_cafe(df2,m):
    for index, r in df2.iterrows(): 

        # ピンをおく
        folium.Marker(
            location=[r.カフェ_緯度, r.カフェ_経度],
            popup='カフェ',
            icon=folium.Icon(color='red')
            
        ).add_to(m)



# タイトル
st.write('地図でチェック')
# スライダーをつける→今回不要
# rad = st.slider('拠点を中心とした円の半径（km）',
                # value=1,min_value=1, max_value=2)
                
# 半径の距離を表示→今回不要              
# st.subheader("各拠点からの距離{:,}km".format(rad))

# 地図の初期設定
m = folium.Map(location=[34.6924107,135.5016849], zoom_start=15)

# データを地図渡す
AreaMarker_station(df2,m) 
AreaMarker_cafe(df2,m) 

 # 地図情報を表示
folium_static(m)
