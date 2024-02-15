import streamlit as st
from datetime import datetime, timedelta

# ボタンのラベルと時間の辞書
button_data = {
    "洗顔・スキンケア(15分)": {"hours": 0, "minutes": 15},
    "コーヒータイム(30分)": {"hours": 0, "minutes": 30},
    "着替え(5分)": {"hours": 0, "minutes": 5},
    "食事(30分)": {"hours": 0, "minutes": 30},
    "お弁当作る(20分)": {"hours": 0, "minutes": 20},
    "洗濯機動かす・干す(25分)": {"hours": 0, "minutes": 25},
    "洗濯物取り込む・たたむ(20分)": {"hours": 0, "minutes": 20},
    "化粧(15分)": {"hours": 0, "minutes": 15},
    "掃除機(10分)": {"hours": 0, "minutes": 10},
    "トイレ掃除(10分)": {"hours": 0, "minutes": 10},    
    "片付け(15分)": {"hours": 0, "minutes": 15},
    "お風呂(60分)": {"hours": 0, "minutes": 60},
    "皿洗い(10分)": {"hours": 0, "minutes": 10},
    "歯磨き(5分)": {"hours": 0, "minutes": 5},
    "ゴミ出し(5分)": {"hours": 0, "minutes": 5},
    "ストレッチ(10分)": {"hours": 0, "minutes": 10},
    "読書(30分)": {"hours": 0, "minutes": 30},
    "汎用(5分)": {"hours": 0, "minutes": 5},
    "汎用(10分)": {"hours": 0, "minutes": 10},
    "汎用(30分)": {"hours": 0, "minutes": 30},    
    "汎用(50分)": {"hours": 0, "minutes": 50},
}

# 選択されたボタンの時間を計算する関数
def calculate_selected_time(selected_buttons):
    total_time = timedelta()
    for button in selected_buttons:
        total_time += timedelta(minutes=button_data[button]["minutes"])
    return total_time

# Streamlitアプリの開始
st.title("タスク達成に必要な時間")

# イベント名と開始時間の入力
event_name = st.text_input("イベント名を入力してください")
event_start_time = st.time_input("イベントの開始時間を入力してください")

# ボタンを作成
selected_buttons = st.multiselect("ボタンを選択してください", list(button_data.keys()))

# 選択されたボタンの時間を計算
total_selected_time = calculate_selected_time(selected_buttons)

# 選択されたボタンを表示
st.write(f"選択されたボタン: {', '.join(selected_buttons)}")

# 移動時間の入力
travel_time = st.number_input("イベントまでの移動時間（分）", min_value=0, step=5)

# travel_time が入力されている場合のみ計算
if travel_time is not None:
    total_selected_time += timedelta(minutes=travel_time)

# event_start_timeをdatetimeオブジェクトに変換
current_time = datetime.now()
event_start_datetime = datetime(current_time.year, current_time.month, current_time.day,
                                event_start_time.hour, event_start_time.minute)

# 残りの時間を計算
remaining_time = event_start_datetime - total_selected_time

# 計算された時間を表示
st.write(f"合計時間: {total_selected_time}")

# 残りの時間を表示
st.write(f"{event_name}に間に合うように行動するには、{remaining_time:%H:%M}に動き出さなければなりません！")
